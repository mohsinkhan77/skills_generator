import streamlit as st
import google.generativeai as genai
#import os

# Configure the Google Generative AI API
genai.configure(api_key="AIzaSyAaVRtDjAjUd7NpCxM-2Qc696xphpfw35c")  

# Initialize the GenerativeModel with the desired model name
model = genai.GenerativeModel(model_name='gemini-1.5-flash')  # Use the appropriate model name

# Define the Streamlit app
def main():
    # Set the title and description
    st.title("Skills and Companies Recommender") #to set the title for the app
    st.subheader("Developed by Mohsin") #its a subheading
    st.write("Enter the job role to get recommendations.") #suggesting an user what needs to be done with this line of code

    # Get user input for job role
    job_role = st.text_input("Enter a job role:") #input space to enter text

    # Define the prompt based on the job role input
    prompt = f'''What are the skills required for a {job_role}? Also, list the top 10 companies to apply to?d
    skills: name skills without description.'''

    # Generate text based on the prompt and user input
    if st.button("Generate"):
        with st.spinner("Generating recommendations..."):
            try:
                response = model.generate_content(prompt)
                st.subheader("Generated Recommendations:")
                st.write(response.text)
            except Exception as e:
                st.error("An error occurred while generating recommendations.")
                st.write(f"Error details: {e}")

# Run the app
if __name__ == "__main__":
    main()
