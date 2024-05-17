# Resume and Cover Letter Writer

The Resume and Cover Letter Writer is a powerful web application that utilize AI agents t0 simplify the process of creating professional resumes and cover letters. Built using CrewAI and Streamlit, this app generates personalized application documents based on the user's information, target job description, and customizable templates.

## Features

- **Resume Generation**: Create tailored resumes that highlight your skills, experience, and qualifications using customizable templates.
- **Cover Letter Creation**: Generate compelling cover letters that demonstrate your fit and enthusiasm for the role using customizable templates.
- **Job Search**: Search for relevant job openings using the Indeed API and seamlessly add job descriptions to your application.
- **Customizable Templates**: Utilize the provided resume and cover letter templates in markdown format to ensure consistent structure and formatting.
- **Download Options**: Download your generated documents in Word or PDF format for easy sharing and printing.
- **User-Friendly Interface**: Enjoy a clean and intuitive user interface that makes the resume and cover letter writing process a breeze.

## Installation

1. Clone the repository:
   ```
   git clone https://github.com/dynamikapps/resume-cover-letter-writer
   ```

2. Navigate to the project directory:
   ```
   cd resume-cover-letter-writer
   ```

3. Create a conda environment:
   ```
   conda create --name myenv python=3.9
   ```

4. Activate the environment:
   ```
   conda activate myenv
   ```

5. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```

6. Set up environment variables:
   - Create a `.env` file in the project root directory.
   - Add the following variables to the `.env` file:
     ```
     OPENAI_API_KEY=your-openai-key
     GROQ_API_KEY=your-groq-key
     GROQ_MODEL_NAME=your-groq-model-name
     RAPIDAPI_KEY=your-rapid-key
     RAPIDAPI_HOST=your-rapid-host
     ```
   - Replace `your_api_key`, `your-groq-key`, `your-groq-model-name`, `your-rapid-key`, and `your-rapid-host` with your actual API credentials.

## Usage

1. Run the Streamlit application:
   ```
   streamlit run main.py
   ```

2. Open the application in your web browser.

3. Use the sidebar to navigate between the "Resume Writer" and "Job Search" tabs.

4. In the "Resume Writer" tab:
   - Fill in the required information, including name, email, website, phone, work experience, education, and skills.
   - Provide the target job description.
   - Select whether you want to generate a resume, cover letter, or both.
   - Click on the "Generate" button to create the resume and/or cover letter based on the provided templates.
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
- [Indeed API](https://rapidapi.com/mantiks-mantiks-default/api/indeed12/pricing) - Job search and aggregation API.

## Contact

For any inquiries or feedback, please contact [handy@dynamikapps.com](mailto:handy@dynamikapps.com).