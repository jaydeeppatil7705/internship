import streamlit as st
st.title("some basic commands like sliders")
age = st.slider("Enter your age", 1, 100)
city = st.selectbox("Select your city", ["New York", "Jalgaon","Los Angeles", "Chicago", "Houston", "Phoenix"])
if st.button("Submit"):
    st.write("Your age is", age)
    st.write("Your city is", city)  


