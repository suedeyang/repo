import requests
import streamlit as st
import pandas as pd
import datetime 
import time
from streamlit.state.session_state import Value
from streamlit_autorefresh import st_autorefresh

st_autorefresh(interval=600000) # 2000 milliseconds (2 seconds)
st.markdown("""
<link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap@5.1.1/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-F3w7mX95PdgyTmZZMECAngseQB83DfGTowi0iMjiWaeVhAn4FJkqJByhZMI3AhiU" crossorigin="anonymous">
<link href="https://fonts.googleapis.com/css2?family=Noto+Sans+TC:wght@500&display=swap" rel="stylesheet">
<style>
body{
  font-family: 'Noto Sans TC', sans-serif;
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
        if uvi_data['SiteName'] == '橋頭':
            #print(uvi_data)
            return uvi_data



def display_data():
    aqidata=get_aqi_data()
    uvidata=get_uvi_data()
    AQI=aqidata['AQI']
    #AQI_STATUS=aqidata['Status']
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
    #else:
    #    uvi_font_color = "#B34FA2"
    #    uvi_status="危險級"
    #pm2_5=float(aqidata['PM2.5'])
    #pm2_5_AVG=float(aqidata['PM2.5_AVG'])
    #pm2_5_delta=pm2_5-pm2_5_AVG
#
    #pm10=float(aqidata['PM10'])
    #pm10_AVG=float(aqidata['PM10_AVG'])
    #pm10_delta=pm10-pm10_AVG
#
    #ozone=float(aqidata['O3'])
    #ozone_AVG=float(aqidata['O3_8hr'])
    #ozone_delta=ozone-ozone_AVG
    #
    #sitename=aqidata['SiteName']
    #pollutant=aqidata['Pollutant']
    #aqi_update_time=aqidata['ImportDate']
    #uvi_update_time=uvidata['PublishTime']
    #
    ##print(aqi_update_time[11:16])
    #print(uvi_update_time[11:16])
    #cola,colb=st.columns(2) 
    st.markdown(f'<h1 style="font-family: Noto Sans TC, sans-serif;font-size: 3rem;text-align:center;"><strong>AQI空氣指數</h1>', unsafe_allow_html=True)
    st.markdown(f'<h1 style="margin:-20px 0px 10px 0;font-family: Noto Sans TC, sans-serif;text-shadow: 2px 2px 8px #000000;font-size: 8rem;color:{aqi_font_color};text-align:center;"><strong>{AQI}</strong></h1>', unsafe_allow_html=True)
    st.markdown("----")
    st.markdown(f'<h1 style="font-family: Noto Sans TC, sans-serif;font-size: 3rem;text-align:center;"><strong>紫外線指數</h1>', unsafe_allow_html=True)
    #cola.markdown(f'<h1 style="font-family: Noto Sans TC, sans-serif;margin-top: -1em;text-align:center;">空氣品質AQI {AQI_STATUS}</h1>',unsafe_allow_html=True )
    st.markdown(f'<h1 style="margin:-20px 0px 10px 0;font-family: Noto Sans TC, sans-serif;text-shadow: 2px 2px 8px #000000;font-size: 8rem;color:{uvi_font_color};text-align:center;"><strong>{UVI}</strong></h1>', unsafe_allow_html=True)
    #colb.markdown(f'<h1 style="font-family: Noto Sans TC, sans-serif;margin-top: -1em;text-align:center;">紫外線{uvi_status}</h1>',unsafe_allow_html=True )

#data=get_data()
#display_data()

display_data()
