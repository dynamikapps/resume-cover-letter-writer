# Resume and Cover Letter Writer

The Resume and Cover Letter Writer is a powerful web application that simplifies the process of creating professional resumes and cover letters. Built using CrewAI and Streamlit, this app generates personalized application documents based on the user's information and target job description.

## Features

- **Resume Generation**: Create tailored resumes that highlight your skills, experience, and qualifications.
- **Cover Letter Creation**: Generate compelling cover letters that demonstrate your fit and enthusiasm for the role.
- **Job Search**: Search for relevant job openings using the Indeed API and seamlessly add job descriptions to your application.
- **Customizable Templates**: Choose from a variety of professionally designed resume and cover letter templates.
- **Download Options**: Download your generated documents in Word or PDF format for easy sharing and printing.
- **User-Friendly Interface**: Enjoy a clean and intuitive user interface that makes the resume and cover letter writing process a breeze.

## Installation

1. Clone the repository:
git clone https://github.com/your-username/resume-cover-letter-writer.git

2. Navigate to the project directory:
cd resume-cover-letter-writer

3. Create a conda environment:
conda create --name myenv python=3.9

4. Activate the environment:
conda activate myenv

5. Install the required dependencies:
pip install -r requirements.txt

6. Set up environment variables:
- Create a `.env` file in the project root directory.
- Add the following variables to the `.env` file:
  ```
  RAPIDAPI_KEY=your_rapidapi_key
  RAPIDAPI_HOST=your_rapidapi_host
  ```
- Replace `your_rapidapi_key` and `your_rapidapi_host` with your actual RapidAPI credentials.

## Usage

1. Run the Streamlit application:
streamlit run main.py

2. Open the application in your web browser.

3. Use the sidebar to navigate between the "Resume Writer" and "Job Search" tabs.

4. In the "Resume Writer" tab:
- Fill in the required information, including name, email, website, phone, work experience, education, and skills.
- Provide the target job description.
- Select whether you want to generate a resume, cover letter, or both.
- Click on the "Generate" button to create the resume and/or cover letter.
- Copy the generated content or download it as a Word or PDF file.

5. In the "Job Search" tab:
- Enter job keywords and location to search for relevant job openings.
- Click on the "Search Jobs" button to retrieve job listings.
- Select a job from the search results to view its details.
- Click on the "Add Job Description" button to automatically populate the job description in the "Resume Writer" tab.
- Optionally, click on the "Apply on Indeed" button to be redirected to the Indeed job posting.

## Contributing

Contributions are welcome! If you have any ideas, suggestions, or bug reports, please open an issue or submit a pull request. Make sure to follow the project's code of conduct.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more information.

## Acknowledgements

- [CrewAI](https://www.crewai.com/) - AI-powered tools for building intelligent applications.
- [Streamlit](https://streamlit.io/) - Framework for building interactive web applications.
- [Indeed API](https://www.indeed.com/publisher) - Job search and aggregation API.

## Contact

For any inquiries or feedback, please contact [handy@dynamikapps.com](mailto:handy@dynamikapps.com).