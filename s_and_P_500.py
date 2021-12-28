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
st.write(sector_unique)
st.write("總共有的分類",len(sector_unique))

sector=df.groupby("GICS Sector")
#@st.write(sector)
st.title("sector_first")
st.write(sector.first())

st.title("sector_describe描述統計")
st.write(sector.describe()) #描述統計

st.title("groupby GICS Sector中再找出屬於Health Care類別的項目")
st.write(sector.get_group('Health Care')) #groupby GICS Sector中再找出Health Care群

#df['Symbol'] 抓取股票代號 資料的Symbol欄位
#st.write(list(df.Symbol))

@st.cache
#https://pypi.org/project/yfinance/
data=yf.download(
    # tickers list or string as well
    tickers=list(df.Symbol),
    
    # use "period" instead of start/end
    # valid periods: 1d,5d,1mo,3mo,6mo,1y,2y,5y,10y,ytd,max
    # (optional, default is '1mo')
    period="ytd",
    
    # fetch data by interval (including intraday if period < 60 days)
    # valid intervals: 1m,2m,5m,15m,30m,60m,90m,1h,1d,5d,1wk,1mo,3mo
    # (optional, default is '1d')   
    interval="1mo",
    
    # group by ticker (to access via data['SPY'])
    # (optional, default is 'column')
    #group_by="ticker",
    group_by = 'ticker',
    # adjust all OHLC automatically
    # (optional, default is False)
    auto_adjust=True,
    # download pre/post regular market hours data
    # (optional, default is False)
    prepost = True,

    # use threads for mass downloading? (True/False/Integer)
    # (optional, default is True)
    threads = True,
    # proxy URL scheme use use when downloading?
    # (optional, default is None)
    proxy = None
)

data

#data['ABT'] 查詢ABT的一年分每日股價資料
df=pd.DataFrame(data['ABT'].Close)
df['Date']=df.index
df