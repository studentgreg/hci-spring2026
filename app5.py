import streamlit as st
import pandas as pd # to manipulate data in tabular format
import numpy as np # numerical computing library
from datetime import time

st.title("Simple Dashboard")

basic_plots = st.checkbox("Basic Plots")
if basic_plots:
    table = pd.DataFrame(
        np.random.randn(20,3),
        columns=["A","B","C"]
    )
    st.dataframe(table)
    st.line_chart(table)

sliders = st.checkbox("Sliders")
if sliders:
    age = st.slider("How old are you?",18,120,20)
    someRange = st.slider("Select a range",
                          0.0, 200.0, (25., 50.))
    dentistAppointment = st.slider("Select a time",
                                   value=(time(10,30),time(12,30)))

st.divider()

tab1, tab2, tab3 = st.tabs(["About Us","Mission","Contact Us"])
with tab1:
    st.write("We are CAP 4104 students at FIU.")

with tab2:
    st.write("Our mission is to use HCI principles effectively.")

with tab3:
    st.write("Office hours are Wednesdays in INV1 455 at 2pm.")