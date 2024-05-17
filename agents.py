import os
from crewai import Agent, Task, Crew, Process
from pydantic import BaseModel
from tools import ResumeFormattingTool, CoverLetterFormattingTool
# from langchain_groq import ChatGroq


class ResumeAgent(Agent, BaseModel):
    name: str
    email: str
    website: str
    phone: str
    work_experience: str
    education: str
    skills: str
    job_description: str
    role: str = "Resume Writer"
    goal: str = "Generate a tailored resume based on the user's information and job description."
    backstory: str = "As a seasoned resume writer, I excel at crafting compelling resumes that highlight the candidate's strengths and align with the target job requirements."

    def __init__(self, **data):
        BaseModel.__init__(self, **data)
        Agent.__init__(
            self,
            name=data['name'],
            email=data['email'],
            website=data['website'],
            phone=data['phone'],
            work_experience=data['work_experience'],
            education=data['education'],
            skills=data['skills'],
            job_description=data['job_description'],
            role=self.role,
            goal=self.goal,
            backstory=self.backstory,
            tools=[ResumeFormattingTool()],
            # llm=ChatGroq(
            #     api_key=os.getenv("GROQ_API_KEY"),
            #     model=os.getenv("GROQ_MODEL_NAME")
            # ),
            verbose=True
        )

    def generate_resume(self):
        with open("templates/resume_template.md", "r") as file:
            template = file.read()

        task = Task(
            description=(
                f"Create a highly detailed and comprehensive resume for {self.name} based on their work experience, education, skills, and the job description:\n\n"
                f"Name: {self.name}\n"
                f"Email: {self.email}\n"
                f"Website: {self.website}\n"
                f"Phone: {self.phone}\n\n"
                f"Work Experience:\n{self.work_experience}\n\n"
                f"Education:\n{self.education}\n\n"
                f"Skills:\n{self.skills}\n\n"
                f"Job Description:\n{self.job_description}\n\n"
                "Generate a compelling and detailed resume that highlights the candidate's relevant experience, qualifications, and achievements for the target job. Include the following sections:\n"
                "1. Summary: A brief overview of the candidate's professional background and key strengths.\n"
                "2. Work Experience: Detailed descriptions of the candidate's work history, including job titles, company names, dates of employment, and key responsibilities and accomplishments for each role.\n"
                "3. Education: A list of the candidate's educational qualifications, including degrees, certifications, and relevant coursework.\n"
                "4. Skills: A comprehensive list of the candidate's technical skills, soft skills, and any other relevant abilities.\n"
                "5. Projects: Descriptions of any notable projects the candidate has worked on, highlighting their contributions and the project outcomes.\n"
                "6. Awards and Achievements: A list of any awards, honors, or special recognition the candidate has received.\n"
                "Ensure that the resume is well-structured, visually appealing, and tailored to the target job description."
            ),
            expected_output=template,
            agent=self
        )

        crew = Crew(agents=[self], tasks=[task], process=Process.sequential)
        result = crew.kickoff()
        formatted_resume = ResumeFormattingTool()._run(result)
        return formatted_resume


class CoverLetterAgent(Agent, BaseModel):
    name: str
    email: str
    website: str
    phone: str
    work_experience: str
    education: str
    skills: str
    job_description: str
    role: str = "Cover Letter Writer"
    goal: str = "Generate a personalized cover letter based on the user's information and job description."
    backstory: str = "As an experienced cover letter writer, I specialize in crafting compelling cover letters that showcase the candidate's fit for the target role and company."

    def __init__(self, **data):
        BaseModel.__init__(self, **data)
        Agent.__init__(
            self,
            name=data['name'],
            email=data['email'],
            website=data['website'],
            phone=data['phone'],
            work_experience=data['work_experience'],
            education=data['education'],
            skills=data['skills'],
            job_description=data['job_description'],
            role=self.role,
            goal=self.goal,
            backstory=self.backstory,
            tools=[CoverLetterFormattingTool()],
            # llm=ChatGroq(
            #     api_key=os.getenv("GROQ_API_KEY"),
            #     model=os.getenv("GROQ_MODEL_NAME")
            # ),
            verbose=True
        )

    def generate_cover_letter(self):
        with open("templates/cover_letter_template.md", "r") as file:
            template = file.read()

        task = Task(
            description=(
                f"Write a highly personalized and compelling cover letter for {self.name} based on their work experience, education, skills, and the job description:\n\n"
                f"Name: {self.name}\n"
                f"Email: {self.email}\n"
                f"Website: {self.website}\n"
                f"Phone: {self.phone}\n\n"
                f"Work Experience:\n{self.work_experience}\n\n"
                f"Education:\n{self.education}\n\n"
                f"Skills:\n{self.skills}\n\n"
                f"Job Description:\n{self.job_description}\n\n"
                "Generate an engaging and detailed cover letter that demonstrates the candidate's enthusiasm, relevant experience, and fit for the target job and company. Include the following elements:\n"
                "1. Opening: A strong opening paragraph that captures the reader's attention and expresses the candidate's interest in the position.\n"
                "2. Relevant Experience: Detailed examples of how the candidate's work experience aligns with the requirements of the target job, showcasing their accomplishments and the value they can bring to the role.\n"
                "3. Skills and Qualifications: A discussion of the candidate's relevant skills and qualifications, highlighting how they match the job requirements and can contribute to the company's success.\n"
                "4. Enthusiasm and Interest: Expressions of the candidate's genuine enthusiasm for the role and the company, demonstrating their knowledge of the company's mission and values.\n"
                "5. Closing: A strong closing paragraph that reiterates the candidate's interest, thanks the reader for their consideration, and expresses a desire for an interview.\n"
                "Ensure that the cover letter is well-written, persuasive, and tailored to the specific job and company."
            ),
            expected_output=template,
            agent=self
        )

        crew = Crew(agents=[self], tasks=[task], process=Process.sequential)
        result = crew.kickoff()
        formatted_cover_letter = CoverLetterFormattingTool()._run(result)
        return formatted_cover_letter
