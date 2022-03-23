import streamlit as st
import pandas as pd
import time
import re

reload_html_string = '''
<head>
        <meta http-equiv="refresh" content="0" />
</head>
'''



df=pd.read_csv('id.txt', sep=',')
proxy_list=df.proxy_key.tolist()
st.text(df)
st.title("龍華國小研習簽到")
input_result=st.text_input("請輸入身分證號，輸入完畢請按鍵盤ENTER鍵",max_chars=10)

if input_result:
    if input_result[0] == "0":
        if input_result in proxy_list:
            index_number=proxy_list.index(input_result)
            ID=df.ID_number[index_number].upper()
            success_message=f'{ID} 簽到成功'
            st.success(success_message)
            time.sleep(1)
            st.markdown(reload_html_string, unsafe_allow_html=True)
        else:
            st.error('感應扣未註冊')




