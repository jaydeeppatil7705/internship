import streamlit as st
import google.generativeai as genai
st.title("welcome to generative ai app")
user_input = st.text_area("Enter your prompt here")
genai.configure(api_key = "AIzaSyB2gInwZdSlyqBOe_FMmUCFH6v2dm9XC1w")

model = genai.GenerativeModel("models/gemini-2.5-flash")

if user_input:
    response = model.generate_content(user_input)    
    st.write("Generated Text:")
    st.write(response.text)


