# In Week #3, we will start designing interfaces using streamlit package
# To run your app, please go to the terminal and run:
#   streamlit run app1.py
#   or
#   python -m streamlit run app1.py

import streamlit as st

st.title("Registration Form")
st.header("You're invited to the 2026 FIU Reception")
st.subheader("Please fill out the form below")

st.divider()

first_name = st.text_input("Enter your first name:",
                           placeholder="First Name")
last_name = st.text_input("Enter your last name:",
                          placeholder="Last Name")
year_of_birth = st.text_input("Enter your year of birth:",
                                placeholder="Ex.: 1998")
start_year_fiu = st.text_input("Enter the year you started at FIU:",
                                placeholder="Ex.: 2022")

if first_name and last_name and year_of_birth and start_year_fiu:
    st.success(f"{first_name}, you have been registered successfully!")