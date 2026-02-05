import streamlit as st

st.title("Temperature Converter")

temp_input = st.number_input("Enter temperature value:")
conv_type = st.selectbox("Select conversion type:",
                         ("Celsius to Fahrenheit",
                          "Fahrenheit to Celsius"))

if conv_type == "Celsius to Fahrenheit":
    result = temp_input * 9/5 + 32
    if result < 60.0:
        st.snow()
    else:
        st.balloons()
else:
    result = (temp_input - 32) * 5/9
    if result < 15.5:
        st.snow()
    else:
        st.balloons()
st.success(f"{temp_input} degrees {conv_type} is {result:.2f} degrees.")
