
import requests
import streamlit as st
from PIL import Image
import numpy as np
#
import cv2
import io

# https://steam.oxxostudio.tw/category/python/spider/line-notify.html
# https://notify-bot.line.me/doc/en/

token =""
#sent_to_LINE_Nofity(teachers_name)
headers = {
    "Authorization": "Bearer " + token  # Bearer後要有一個空白
}

data = {
    'message': "測試訊息\n\n\n"
}

img_file_buffer = st.file_uploader("Upload an image")

if img_file_buffer is not None:
    img = Image.open(img_file_buffer)
    st.image(img)
    img_byte_arr = io.BytesIO()
    img.save(img_byte_arr, format='JPEG', subsampling=0, quality=100)
    img_byte_arr = img_byte_arr.getvalue()
    files = {'imageFile': img_byte_arr}


button=st.button("按鈕")
if button:
    #files = {'imageFile': image}
    response_result = requests.post("https://notify-api.line.me/api/notify", headers=headers, data=data,files=files)
    print(response_result)

