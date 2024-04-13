import streamlit as st
from dotenv import load_dotenv
from pathlib import Path
from agents import ResumeAgent, CoverLetterAgent
import datetime
from utils import download_word, download_pdf

# Load environment variables
load_dotenv()

def clear_session_state():
    st.session_state.clear()

def main():
    st.title("✍️ Resume and Cover Letter Writer")
    
    # User information
    name = st.text_input("Name")
    email = st.text_input("Email")
    website = st.text_input("Website")
    phone = st.text_input("Phone")
    work_experience = st.text_area("Work Experience")
    education = st.text_area("Education")
    skills = st.text_area("Skills")
    
    # Job description
    job_description = st.text_area("Job Description")
    
    # Output selection
    generate_resume = st.checkbox("Generate Resume")
    generate_cover_letter = st.checkbox("Generate Cover Letter")
    
    # Generate and Clear buttons
    col1, col2 = st.columns(2)
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
    
    # Display generated resume
    if "generated_resume" in st.session_state and st.session_state.generated_resume:
        st.subheader("Generated Resume")
        st.text_area("Resume", value=st.session_state.generated_resume)
        
        # Download options for resume
        if st.button("Download Resume (Word)"):
            timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
            download_word(st.session_state.generated_resume, f"resume_{timestamp}.docx")
        if st.button("Download Resume (PDF)"):
            timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
            download_pdf(st.session_state.generated_resume, f"resume_{timestamp}.pdf")
    
    # Display generated cover letter
    if "generated_cover_letter" in st.session_state and st.session_state.generated_cover_letter:
        st.subheader("Generated Cover Letter")
        st.text_area("Cover Letter", value=st.session_state.generated_cover_letter)
        
        # Download options for cover letter
        if st.button("Download Cover Letter (Word)"):
            timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
            download_word(st.session_state.generated_cover_letter, f"cover_letter_{timestamp}.docx")
        if st.button("Download Cover Letter (PDF)"):
            timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
            download_pdf(st.session_state.generated_cover_letter, f"cover_letter_{timestamp}.pdf")

if __name__ == "__main__":
    main()