import streamlit as st
import requests # library that allows us to request data through APIs

st.title("Crypto Monitoring App")
st.subheader("Find the latest cryptocurrency price updates")

crypto = st.selectbox("Select a cryptocurrency:", options=[
    "",
    "Bitcoin",
    "Litecoin",
])

if crypto == "Bitcoin":
    url="https://min-api.cryptocompare.com/data/price?fsym=BTC&tsyms=USD"
    response = requests.get(url).json()
    btc_price = response["USD"]
    st.success(f"The current price of {crypto} is US${btc_price:.2f}.")

elif crypto == "Litecoin":
    url="https://min-api.cryptocompare.com/data/price?fsym=LTC&tsyms=USD"
    response = requests.get(url).json()
    ltc_price = response["USD"]
    st.success(f"The current price of {crypto} is US${ltc_price:.2f}.")