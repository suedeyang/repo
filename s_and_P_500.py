from pkg_resources import ResolutionError
import streamlit as st
import pandas as pd
import yfinance as yf

@st.cache
def load_data():
    url="https://en.wikipedia.org/wiki/List_of_S%26P_500_companies"
    html=pd.read_html(url,header=0)
    df=html[0]
    return df

df=load_data()
#st.dataframe(df )
sector_unique=df['GICS Sector'].unique()
sector=df.groupby("GICS Sector")
st.write(sector.first())
st.write(sector.describe()) #描述統計
st.write(sector.get_group('Health Care'))

#df['Symbol']
list(df.Symbol)