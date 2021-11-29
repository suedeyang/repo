import yfinance as yf
import streamlit as st
import pandas as pd

tickerSymbol = 'GOOGL'
tickerData = yf.Ticker(tickerSymbol)
tickerDf=tickerData.history(period='1d',start='2010-5-31',end='2021-11-29')
#Open High Low Close Volume Dividends Stock Splits
#print(tickerData)

st.write("""
# Closing price

""")

st.line_chart(tickerDf.Close)


st.line_chart(tickerDf.Volume) 