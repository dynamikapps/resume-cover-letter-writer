import streamlit as st
from dotenv import load_dotenv
from pathlib import Path
from agents import ResumeAgent, CoverLetterAgent
import datetime
import os
from utils import download_word, download_pdf
from indeed_api import IndeedAPIClient
from utils import download_word, download_pdf, display_html_description

# Load environment variables
load_dotenv()


def clear_session_state():
    st.session_state.clear()


def main():
    st.set_page_config(
        page_title="⚡️ Resume and Cover Letter Writer", layout="wide")

    # Initialize Indeed API client
    api_key = os.getenv("RAPIDAPI_KEY")
    api_host = os.getenv("RAPIDAPI_HOST")
    indeed_client = IndeedAPIClient(api_key, api_host)

    # Sidebar tabs
    tab = st.sidebar.radio("Select Tab", ["Resume Writer", "Job Search"])

    if tab == "Resume Writer":
        # User Information form
        st.sidebar.title("User Information")
        name = st.sidebar.text_input("Name")
        email = st.sidebar.text_input("Email")
        website = st.sidebar.text_input("Website")
        phone = st.sidebar.text_input("Phone")
        work_experience = st.sidebar.text_area("Work Experience")
        education = st.sidebar.text_area("Education")
        skills = st.sidebar.text_area("Skills")
        job_description = st.sidebar.text_area("Job Description")

        # Output selection
        generate_resume = st.sidebar.checkbox("Generate Resume")
        generate_cover_letter = st.sidebar.checkbox("Generate Cover Letter")

        # Generate and Clear buttons
        col1, col2 = st.sidebar.columns(2)
        with col1:
            generate_button = st.button("Generate")
        with col2:
            clear_button = st.button("Clear")

        if clear_button:
            clear_session_state()

        if generate_button:
            with st.spinner("Generating..."):
                if generate_resume:
                    # Generate resume
                    resume_agent = ResumeAgent(
                        name=name,
                        email=email,
                        website=website,
                        phone=phone,
                        work_experience=work_experience,
                        education=education,
                        skills=skills,
                        job_description=job_description
                    )
                    resume = resume_agent.generate_resume()
                    st.session_state.generated_resume = resume

                if generate_cover_letter:
                    # Generate cover letter
                    cover_letter_agent = CoverLetterAgent(
                        name=name,
                        email=email,
                        website=website,
                        phone=phone,
                        work_experience=work_experience,
                        education=education,
                        skills=skills,
                        job_description=job_description
                    )
                    cover_letter = cover_letter_agent.generate_cover_letter()
                    st.session_state.generated_cover_letter = cover_letter
    elif tab == "Job Search":
        # Job search form
        st.sidebar.title("Job Search")
        job_query = st.sidebar.text_input("Job Keywords")
        job_location = st.sidebar.text_input("Location")
        search_button = st.sidebar.button("Search Jobs")

        if search_button or "jobs" in st.session_state:
            with st.spinner("Searching for jobs..."):
                try:
                    if search_button:
                        # Perform job search
                        search_results = indeed_client.search_jobs(job_query, job_location)
                        jobs = search_results.get("hits", [])
                        st.session_state.jobs = jobs
                    else:
                        jobs = st.session_state.jobs

                    if jobs:
                        selected_job_index = st.sidebar.selectbox("Select a Job", range(len(jobs)), format_func=lambda i: jobs[i]["title"])
                        selected_job = jobs[selected_job_index]
                        selected_job_id = selected_job["id"]

                        # Get job details
                        job_details = indeed_client.get_job_details(selected_job_id)
                        job_description = job_details.get("description", "")
                        job_url = job_details.get("indeed_final_url", "")

                        st.sidebar.subheader("Job Details")
                        st.sidebar.markdown(f"**Company:** {selected_job['company_name']}")
                        st.sidebar.markdown(f"**Title:** {selected_job['title']}")
                        st.sidebar.markdown(f"**Location:** {selected_job['location']}")
                        if selected_job.get("salary"):
                            salary_type = selected_job["salary"].get("type", "").capitalize()
                            salary_min = selected_job["salary"].get("min", "")
                            salary_max = selected_job["salary"].get("max", "")
                            st.sidebar.markdown(f"**Salary:** {salary_min} - {salary_max} ({salary_type})")

                        st.sidebar.subheader("Job Description")
                        display_html_description(job_description)

                        # Add Job Description button
                        if st.sidebar.button("Add Job Description"):
                            st.session_state.job_description = job_description
                            st.sidebar.success("Job description added to the form.")

                        # Apply on Indeed button
                        if job_url:
                            if st.sidebar.button("Apply on Indeed"):
                                st.sidebar.markdown(f'<a href="{job_url}" target="_blank">Apply on Indeed</a>', unsafe_allow_html=True)
                    else:
                        st.sidebar.warning("No jobs found. Please refine your search.")
                except Exception as e:
                    st.sidebar.error(f"An error occurred while searching for jobs: {str(e)}")

    # Main page layout
    st.title("📝 Generated Documents")

    # Display generated resume
    if "generated_resume" in st.session_state and st.session_state.generated_resume:
        st.subheader("Resume")
        st.text_area(
            "Resume", value=st.session_state.generated_resume, height=400)

        # Download options for resume
        col1, col2 = st.columns(2)
        with col1:
            if st.button("Download Resume (Word)"):
                timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
                download_word(st.session_state.generated_resume,
                              f"resume_{timestamp}.docx")
        with col2:
            if st.button("Download Resume (PDF)"):
                timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
                download_pdf(st.session_state.generated_resume,
                             f"resume_{timestamp}.pdf")

    # Display generated cover letter
    if "generated_cover_letter" in st.session_state and st.session_state.generated_cover_letter:
        st.subheader("Cover Letter")
        st.text_area("Cover Letter",
                     value=st.session_state.generated_cover_letter, height=400)

        # Download options for cover letter
        col1, col2 = st.columns(2)
        with col1:
            if st.button("Download Cover Letter (Word)"):
                timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
                download_word(st.session_state.generated_cover_letter,
                              f"cover_letter_{timestamp}.docx")
        with col2:
            if st.button("Download Cover Letter (PDF)"):
                timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
                download_pdf(st.session_state.generated_cover_letter,
                             f"cover_letter_{timestamp}.pdf")


if __name__ == "__main__":
    main()
