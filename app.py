import pandas as pd
import streamlit as st
from datetime import time
import datetime
from PIL import Image

st.header("滑桿slider使用")
age = st.slider('How old are you?', 0, 130, 25)
st.write("你的年齡是",age)

values=st.slider('設定一個年齡',0.0,100.0,(25.0,75.0),0.5)
st.write('範圍是',values[0],"到",values[1])

appointment=st.slider('排定你的約會時間',value=(time(11,30),time(12,45)))
st.write("You're scheduled for:",appointment)

start_time=st.slider("你何時要開始呢?",value=datetime.datetime.now(),format="MM/DD/YY - hh:mm")
st.write("開始時間為...",start_time)



st.header("滑桿選擇器select slider使用")
st.caption("間斷/名義變量的滑桿選擇器")
color=st.select_slider("你喜歡的顏色",['red','green','blue','yellow'])
st.write("youur favorite color is ",color)

start_color, end_color = st.select_slider(
    'Select a range of color wavelength',
    options=['red', 'orange', 'yellow', 'green', 'blue', 'indigo', 'violet'],
    value=('red', 'blue'))
st.write('You selected wavelengths between', start_color, 'and', end_color)


st.header("數字/文字/文字區塊 date time 輸入器")
title = st.text_input('Movie title','',5,'',"password",'輔助說明')
st.write(title)

number = st.number_input('Insert a number',0,100,50,1,'%i')
st.write('The current number is ', number)


txt = st.text_area('Text to analyze')
st.write('Sentiment:', txt)


#d = st.date_input("When's your birthday",datetime.datetime.now())
d = st.date_input("When's your birthday",datetime.date(2019,7,6))
st.write('Your birthday is:', d)

t = st.time_input('Set an alarm for', datetime.time(8, 45))
st.write('Alarm is set for', t)


st.header("檔案上傳")
uploaded_file = st.file_uploader("Choose a file")
if uploaded_file is not None:
    # To read file as bytes:
    bytes_data = uploaded_file.getvalue()
    st.write(bytes_data)
    # To convert to a string based IO:
    #stringio = StringIO(uploaded_file.getvalue().decode("utf-8"))
    #st.write(stringio)
    # To read file as string:
    #string_data = stringio.read()
    #st.write(string_data)
    # Can be used wherever a "file-like" object is accepted:
    dataframe = pd.read_csv(uploaded_file)
    st.write(dataframe)

uploaded_files=st.file_uploader("Choose a CSV file",accept_multiple_files=True)
for uploaded_file in uploaded_files:
    bytes_data=uploaded_file.read()
    st.write('filename is :',uploaded_file.name)
    st.write(bytes_data)

st.header("顏色選擇器")
color = st.color_picker('Pick A Color', '#00f900')
st.write('The current color is', color)

st.title('Media elements')
image=Image.open('sunrise.jpg')#要先使用image.open
st.image(image,caption='山邊的日出')



#video_file = open('myvideo.mp4', 'rb')
#video_bytes = video_file.read()
#st.video(video_bytes)
st.video('https://youtu.be/FVsvrFAWDTM') 