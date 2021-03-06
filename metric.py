import requests
import streamlit as st
import pandas as pd
import datetime 
import time
from streamlit.state.session_state import Value
from streamlit_autorefresh import st_autorefresh
st.set_page_config(layout="wide")
st_autorefresh(interval=600000) # 2000 milliseconds (2 seconds)
st.markdown("""

<link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap@5.1.1/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-F3w7mX95PdgyTmZZMECAngseQB83DfGTowi0iMjiWaeVhAn4FJkqJByhZMI3AhiU" crossorigin="anonymous">
<link href="https://fonts.googleapis.com/css2?family=Noto+Sans+TC:wght@500&display=swap" rel="stylesheet">
<style>
body{
  font-family: 'Noto Sans TC', sans-serif;margin-top: -1em;
}
</style>
""", unsafe_allow_html=True)


url_AQI='https://data.epa.gov.tw/api/v1/aqx_p_432?limit=1000&api_key=9be7b239-557b-4c10-9775-78cadfc555e9&sort=ImportDate%20desc&format=json'
url_UVI="https://data.epa.gov.tw/api/v1/uv_s_01?limit=40&api_key=9be7b239-557b-4c10-9775-78cadfc555e9&sort=ImportDate%20desc&format=json"

def get_aqi_data():
    aqi_raw_data=requests.get(url_AQI)
    aqi_datas=aqi_raw_data.json()['records']#要寫成data.json()['stats']解析才會正確
    for aqi_data in aqi_datas:
        if aqi_data['SiteName'] == '左營':
            #print(aqi_data)
            return aqi_data
def get_uvi_data():    
    uvi_raw_data=requests.get(url_UVI)
    uvi_datas=uvi_raw_data.json()['records']
    for uvi_data in uvi_datas:
        if uvi_data['SiteName'] == '高雄':
            #print(uvi_data)
            return uvi_data



def display_data():
    aqidata=get_aqi_data()
    uvidata=get_uvi_data()
    AQI=aqidata['AQI']
    AQI_STATUS=aqidata['Status']
    if int(AQI) < 50 :
        aqi_font_color = "#009865"
    elif int(AQI) < 100:
        aqi_font_color = "#FFFB26"
    elif int(AQI) < 150:
        aqi_font_color = "#FF9835"
    elif int(AQI) < 200:
        aqi_font_color = "#CA0034"
    else :
        aqi_font_color = "#670099"

    UVI=round(float(uvidata['UVI']),1)
    #UVI=round(float(2),1)
    if UVI < 2 :
        uvi_font_color = "#A7CD20"
        uvi_status="低量級"
    elif UVI < 5 :
        uvi_font_color = "#FFA500"
        uvi_status="中量級"
    elif UVI < 7 :
        uvi_font_color = "#F39800"
        uvi_status="高量級"
    elif UVI < 10 :
        uvi_font_color = "#EA1904"
        uvi_status="過量級"
    else:
        uvi_font_color = "#B34FA2"
        uvi_status="危險級"
    pm2_5=float(aqidata['PM2.5'])
    pm2_5_AVG=float(aqidata['PM2.5_AVG'])
    pm2_5_delta=pm2_5-pm2_5_AVG

    pm10=float(aqidata['PM10'])
    pm10_AVG=float(aqidata['PM10_AVG'])
    pm10_delta=pm10-pm10_AVG

    ozone=float(aqidata['O3'])
    ozone_AVG=float(aqidata['O3_8hr'])
    ozone_delta=ozone-ozone_AVG
    
    sitename=aqidata['SiteName']
    pollutant=aqidata['Pollutant']
    aqi_update_time=aqidata['ImportDate']
    uvi_update_time=uvidata['PublishTime']
    
    #print(aqi_update_time[11:16])
    #print(uvi_update_time[11:16])
    
    col1,col2,col3,col4,col5,col6,col7,col8=st.columns(8)
    
    col1.metric("PM2.5數值",value=aqidata['PM2.5'],delta=pm2_5_delta)
    col2.metric("PM10數值",value=aqidata['PM10'],delta=pm10_delta)
    col3.metric("臭氧",value=aqidata['O3'],delta=ozone_delta)
    col4.metric("AQI數據更新時間",value=aqi_update_time[11:16])
    col5.metric("UVI數據更新時間",value=uvi_update_time[11:16])
    col6.metric("主要汙染物",pollutant)
    col7.metric("測站位置",sitename)
    col8.metric("",value="")
    
#data=get_data()
#display_data()

display_data()
