import streamlit as st

st.set_page_config(layout="wide",
                   page_title="FIU Newsletter",
                   page_icon=":newspaper:")
st.title("FIU Newsletter")
st.subheader("Sign up for our newsletter below!")

st.sidebar.title("Contact Us")
selected_method=st.sidebar.selectbox("How do you want to be contacted?",
                     ("","Email", "Phone", "Text"))
if selected_method:
    userInfo=st.sidebar.text_input(f"Enter your {selected_method} information:")

# Let's create a better form
with st.form("Registration",clear_on_submit=True):
    first_name=st.text_input("First Name:")
    last_name=st.text_input("Last Name:")
    age=st.number_input("Age:")
    major=st.selectbox("Major:",
                       ("", "CS","Cybersecurity","IT", "Data Science and AI"))
    level=st.selectbox("Level:",
                   ("", "Freshman", "Sophomore", "Junior", "Senior"))
    submit_button=st.form_submit_button("Submit")
    if first_name and last_name and age and major and level and submit_button:
        st.success(f"Thank you {first_name} {last_name} for signing up!")
    else:
        st.info("Please fill out all the fields.")