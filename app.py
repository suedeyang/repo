import pandas as pd
import streamlit as st
from datetime import time
import datetime

st.header("滑桿使用")
age = st.slider('How old are you?', 0, 130, 25)
st.write("你的年齡是",age)

values=st.slider('設定一個年齡',0.0,100.0,(25.0,75.0),0.5)
st.write('範圍是',values[0],"到",values[1])

appointment=st.slider('排定你的約會時間',value=(time(11,30),time(12,45)))
st.write("You're scheduled for:",appointment)

start_time=st.slider("你何時要開始呢?",value=datetime.datetime.now(),format="MM/DD/YY - hh:mm")
st.write("開始時間為...",start_time)