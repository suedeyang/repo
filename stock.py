import twstock
import streamlit as st
#twstock.__update_codes()

stock=twstock.Stock('2330')
st.line_chart(stock.price,stock.high)