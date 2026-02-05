import streamlit as st
import pandas as pd # data manipulation
import plotly.express as px # data visualization


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

with tab1:
    st.header("Raw Data")
    st.dataframe(df) # streamlit displays pandas dataframes

    st.header("Summary Statistics")
    st.dataframe(df.describe())

with tab2:
    st.header("Charts")
    with st.expander("Line Chart"):
        col1, col2 = st.columns([4,1])
        with col1:
            parameter_selected = st.selectbox(
                "Select a parameter:",
                df.columns
            )
        with col2:
            colorSelected = st.color_picker(
                "Pick a color:",
                "#6495ED"
            )
        fig1 = px.line(df,
                       x="Time",
                       y=parameter_selected,
                       title=f"{parameter_selected} over Time"
            )
        fig1.update_traces(line_color=colorSelected)
        st.plotly_chart(fig1) # streamlit displays plotly charts

    with st.expander("3D Plot"):
        fig2 = px.scatter_3d(df,
                             x="Longitude",
                             y="Latitude",
                             z="Total Water Column (m)",
                             color="Temperature (c)"
        )
        fig2.update_scenes(zaxis_autorange="reversed")
        st.plotly_chart(fig2)