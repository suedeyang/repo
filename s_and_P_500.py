import streamlit as st
import pandas as pd
import yfinance as yf
import matplotlib.pyplot as plt
import base64


st.title('S&P 500 App')
st.sidebar.header('User Input Feature')

@st.cache
def load_data():
    url="https://en.wikipedia.org/wiki/List_of_S%26P_500_companies"
    html=pd.read_html(url,header=0)
    df=html[0]
    return df

df=load_data()
#st.dataframe(df )
#sector_unique=df['GICS Sector'].unique()
#st.write(sector_unique)
#st.write("總共有的分類",len(sector_unique))

sector=df.groupby("GICS Sector")
sorted_sector_unique=sorted(df['GICS Sector'].unique() )
selected_sector=st.sidebar.multiselect('Sector',sorted_sector_unique,sorted_sector_unique)

#篩選資料
df_selected_sector=df[(df['GICS Sector'].isin(selected_sector))]


st.header('Display Companies in Selected Sector')
st.write('Data Dimension:'+str(df_selected_sector.shape[0])+"rows and"+str(df_selected_sector.shape[1])+' columns.')
st.dataframe(df_selected_sector)

#@st.write(sector)
#st.title("sector_first")
#st.write(sector.first())

#st.title("sector_describe描述統計")
#st.write(sector.describe()) #描述統計
#
#st.title("groupby GICS Sector中再找出屬於Health Care類別的項目")
#st.write(sector.get_group('Health Care')) #groupby GICS Sector中再找出Health Care群

#df['Symbol'] 抓取股票代號 資料的Symbol欄位
#st.write(list(df.Symbol))

#https://pypi.org/project/yfinance/
data = yf.download(
    # tickers list or string as well
    tickers=list(df_selected_sector[:10].Symbol),
    
    # use "period" instead of start/end
    # valid periods: 1d,5d,1mo,3mo,6mo,1y,2y,5y,10y,ytd,max
    # (optional, default is '1mo')
    period="ytd",
    
    # fetch data by interval (including intraday if period < 60 days)
    # valid intervals: 1m,2m,5m,15m,30m,60m,90m,1h,1d,5d,1wk,1mo,3mo
    # (optional, default is '1d')   
    interval="1d",
    
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

#data['ABT'] 查詢ABT的一年分每日股價資料
#df=pd.DataFrame(data['ABT'].Close)
#df['Date']=df.index

# Plot Closing Price of Query Symbol
def price_plot(symbol):
  df = pd.DataFrame(data[symbol].Close)
  df['Date'] = df.index
  plt.fill_between(df.Date, df.Close, color='skyblue', alpha=0.3)
  plt.plot(df.Date, df.Close, color='skyblue', alpha=0.8)
  plt.xticks(rotation=90)
  plt.title(symbol, fontweight='bold')
  plt.xlabel('Date', fontweight='bold')
  plt.ylabel('Closing Price', fontweight='bold')
  st.set_option('deprecation.showPyplotGlobalUse', False)#影片中沒有這行 加上這行才不會有警告訊息
  return st.pyplot()
  

#price_plot('AAPL')
num_company=st.sidebar.slider('Number of Companies',1,5)
if st.button('Show Plots'):
    st.header('Stock Closing Price')
    for i in list(df_selected_sector.Symbol)[:num_company]:
        price_plot(i)