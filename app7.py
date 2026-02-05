import streamlit as st
import pandas as pd # data manipulation
import plotly.express as px # data visualization

# This code can be found at github.com/studentgreg/hci-spring2026

st.set_page_config(layout="wide",
                   page_title="Data Dashboard",
                   page_icon=":bar_chart:")

st.title("Data Dashboard")

st.sidebar.title("Load Data")
uploadedFile = st.sidebar.file_uploader("Choose a CSV file",
                                        type=["csv"])

if uploadedFile is not None:
    df = pd.read_csv(uploadedFile) # Reading uploaded file from the user
    st.sidebar.success("Data successfully loaded.")
else:
    st.sidebar.info("A default dataset will be used.")
    df = pd.read_csv("biscayne_bay_water_quality2.csv") # default dataset

tab1, tab2, tab3 = st.tabs(["Tables","Charts","Map"])