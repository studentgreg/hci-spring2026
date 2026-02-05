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
