import requests
import streamlit as st
import pandas as pd
import datetime 
import time
from streamlit_autorefresh import st_autorefresh

st_autorefresh(interval=600000) # 2000 milliseconds (2 seconds)

st.markdown("""
<link href="https://cdn.jsdelivr.net/npm/bootstrap@5.1.1/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-F3w7mX95PdgyTmZZMECAngseQB83DfGTowi0iMjiWaeVhAn4FJkqJByhZMI3AhiU" crossorigin="anonymous">
<style>
.big-font {
    font-size:300px !important;
}
</style>
""", unsafe_allow_html=True)


url='https://data.epa.gov.tw/api/v1/aqx_p_432?limit=1000&api_key=9be7b239-557b-4c10-9775-78cadfc555e9&sort=ImportDate%20desc&format=json'
url2='https://data.epa.gov.tw/api/v1/uv_s_01?limit=1000&api_key=9be7b239-557b-4c10-9775-78cadfc555e9&sort=ImportDate%20desc&format=json'

def get_data():
    raw_data=requests.get(url)
    datas=raw_data.json()['records']#要寫成data.json()['stats']解析才會正確
    for data in datas:
        if data['SiteName'] == '左營':
            return data


def display_data():
    data=get_data()
    AQI=data['AQI']
    Site=data['SiteName']

    col1,col2=st.columns(2) 
    col1.title("偵測站位置")
    col2.title(Site) 

    col3,col4=st.columns(2) 
    col3.title("AQI空氣指數")
    col4.title(AQI)

    col5,col6=st.columns(2) 
    col5.title("主要汙染物")
    col6.title(data['Pollutant'])

    col7,col8=st.columns(2) 
    col7.title("發布時間:")
    col8.title(data['ImportDate'])

    

st.markdown('<h1 class="display-1"><strong>龍華國小環境指數</strong></h1>', unsafe_allow_html=True)
st.markdown(' --- ')
#data=get_data()
#display_data()

display_data()

