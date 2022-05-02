import requests
import streamlit as st
import pandas as pd
import datetime 
import time
from streamlit.state.session_state import Value
from streamlit_autorefresh import st_autorefresh

#st_autorefresh(interval=600000) # 2000 milliseconds (2 seconds)

#with open('style.css') as f:
#    st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)


st.markdown('<h1 style="font-family: Noto Sans TC, sans-serif;margin-top:-1em;font-size: 5rem;text-align:center;">龍華國小環境指數</h1>', unsafe_allow_html=True)

st.markdown("""
<link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap@5.1.1/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-F3w7mX95PdgyTmZZMECAngseQB83DfGTowi0iMjiWaeVhAn4FJkqJByhZMI3AhiU" crossorigin="anonymous">
<link href="https://fonts.googleapis.com/css2?family=Noto+Sans+TC:wght@500&display=swap" rel="stylesheet">
<style>
body{
  font-family: 'Noto Sans TC', sans-serif;
}
</style>
""", unsafe_allow_html=True)

new_url_AQI="https://data.epa.gov.tw/api/v2/aqx_p_432?api_key=1a533517-0c08-4d8f-9948-f3706970a4e5&format=json&filters=SiteName,EQ,左營"
url_UVI="https://data.epa.gov.tw/api/v2/uv_s_01?api_key=1a533517-0c08-4d8f-9948-f3706970a4e5&format=json&filters=sitename,eq,高雄&limit=1"

def get_aqi_data():
    aqi_data=requests.get(new_url_AQI).json()['records']
    return aqi_data

def get_uvi_data():    
    uvi_datas=requests.get(url_UVI).json()['records']
    return uvi_datas

aqidata=aqi_data=requests.get(new_url_AQI).json()['records'][0]['aqi']
st.write(aqi_data)
uvi_data=requests.get(url_UVI).json()['records'][0]['uvi']
st.write(uvi_data)


def display_data():
    aqidata=get_aqi_data()
    uvidata=get_uvi_data()
    AQI=aqidata[0]['aqi']
    AQI_STATUS=aqidata[0]['status']
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

    UVI=round(float(uvidata[0]['uvi']),1)
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
    
    #print(aqi_update_time[11:16])
    #print(uvi_update_time[11:16])
    cola,colb=st.columns(2) 
    cola.markdown(f'<h1 style="font-family: Noto Sans TC, sans-serif;text-shadow: 2px 2px 8px #000000;font-size: 12rem;color:{aqi_font_color};text-align:center;"><strong>{AQI}</strong></h1>', unsafe_allow_html=True)
    cola.markdown(f'<h1 style="font-family: Noto Sans TC, sans-serif;margin-top: -1em;text-align:center;">空氣品質AQI {AQI_STATUS}</h1>',unsafe_allow_html=True )
    colb.markdown(f'<h1 style="font-family: Noto Sans TC, sans-serif;text-shadow: 2px 2px 8px #000000;font-size: 12rem;color:{uvi_font_color};text-align:center;"><strong>{UVI}</strong></h1>', unsafe_allow_html=True)
    colb.markdown(f'<h1 style="font-family: Noto Sans TC, sans-serif;margin-top: -1em;text-align:center;">紫外線{uvi_status}</h1>',unsafe_allow_html=True )
    st.markdown(' --- ')

#data=get_data()
#display_data()

#display_data()