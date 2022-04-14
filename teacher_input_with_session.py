import streamlit as st
import streamlit.components.v1 as components
import pandas as pd
import time
import re
import requests
import os
#KEY=''
#endpoint='https://api.airtable.com/v0/appCY8QfugFWkKMvH/id'

alphaTable = {'A': 1, 'B': 10, 'C': 19, 'D': 28, 'E': 37, 'F': 46,
            'G': 55, 'H': 64, 'I': 39, 'J': 73, 'K': 82, 'L': 2, 'M': 11,
            'N': 20, 'O': 48, 'P': 29, 'Q': 38, 'R': 47, 'S': 56, 'T': 65,
            'U': 74, 'V': 83, 'W': 21, 'X': 3, 'Y': 12, 'Z': 30}


def add_to_airtable(id):
    #Python requests headers
    headers={
        "Authorization": f'Bearer {KEY}', #注意前面的,
        "Content-Type" : "application/json"
    }

    data= {
    "records": [
            {
            "fields": {
                "ID": id ,
                }
            }
        ]
    }
    r=requests.post(endpoint,json=data,headers=headers)
    #print(r.status_code) #HTTP status code
    return r.status_code

def reset_box():
    if st.session_state.input_box.isdigit():
        if st.session_state.input_box in proxy_list:
            index_number=proxy_list.index(st.session_state.input_box)
            ID=df.ID_number[index_number].upper()
            
            with open('appendSomething.txt', 'a') as f:
                f.write(f'{ID}\n')
            success_message=f'{ID} 簽到成功，下一位老師請繼續簽到'
            st.success(success_message)
            st.session_state.input_box = '' #清空
        else:
            st.error('電梯感應扣未註冊，請改輸入身分證號')
            time.sleep(1)
            st.session_state.input_box = '' #清空
    else:
        id_check=re.fullmatch("^[A-Z][12][0-9]{8}$",st.session_state.input_box.upper())
        if id_check == None:
            st.error('身分證字號輸入錯誤，請重新輸入')
            st.session_state.input_box = '' #清空 
        
        else:
            sum = alphaTable[st.session_state.input_box.upper()[0]] + int(st.session_state.input_box[1]) * 8 + int(st.session_state.input_box[2]) * 7 + int(st.session_state.input_box[3]) * 6 + int(st.session_state.input_box[4]) * 5 + int(st.session_state.input_box[5]) * 4 + int(st.session_state.input_box[6]) * 3 + int(st.session_state.input_box[7]) * 2 + int(st.session_state.input_box[8]) * 1 + int(st.session_state.input_box[9])
            if sum % 10 != 0:
                st.error('身分證字號驗證錯誤，請重新輸入')
                st.session_state.input_box = '' #清空
            else:
                with open('appendSomething.txt', 'a') as f:
                    f.write(f'{st.session_state.input_box.upper()}\n')
                success_message=f'{st.session_state.input_box.upper()} 簽到成功，下一位老師請繼續簽到'
                st.success(success_message)
                st.session_state.input_box = '' #清空


def check_login(id):
    with open('appendSomething.txt',r) as f :
        txt=f.readlines()
        if id +"\n" in txt:
            return True
        elif id in txt:
            return True
        else:
            return False

df=pd.read_csv('id.txt', sep=',')
proxy_list=df.proxy_key.tolist()
#st.markdown('# 龍華國小教師進修簽到 #')
input_result=st.text_input("請在下方框框中簽到",max_chars=10,key='input_box',on_change=reset_box)
st.markdown('### **感應電梯磁扣** or **直接輸入身分證字號(輸入完畢按ENTER)** ###', unsafe_allow_html=False)

#autofocus程式碼，要放在文字輸入框產生後再執行比較不會出錯
components.html(
    f"""
        <div>some hidden container</div>
        <script>
            var input = window.parent.document.querySelectorAll("input[type=text]");
            for (var i = 0; i < input.length; ++i) {{
                input[i].focus();
            }}
    </script>
    """,
    height=1
)
if os.path.isfile("appendSomething.txt"):
    with open("appendSomething.txt",'r') as count_f:
        checked_numbers=count_f.readlines()
        st.write("目前累計簽到人數：",len(checked_numbers))
        st.write("最近5筆簽到資料：")
        if len(checked_numbers) < 5:
            end_point=-len(checked_numbers) - 1
            for i in range(-1,end_point,-1):
                st.write(checked_numbers[i])
        else:
            for i in range(-1,-6,-1): 
                st.write(checked_numbers[i])
else:
    st.write("目前累計簽到人數：0")

#autofocus的問題 https://discuss.streamlit.io/t/why-does-my-text-input-not-focus-with-script-in-component-html-when-sessionstore-is-unchanged/18289