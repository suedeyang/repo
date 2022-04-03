import streamlit as st
import streamlit.components.v1 as components
import pandas as pd
import time
import re
import requests
#KEY=''
#endpoint='https://api.airtable.com/v0/appCY8QfugFWkKMvH/id'

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
            success_message=f'{ID} 簽到成功'
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
            with open('appendSomething.txt', 'a') as f:
                f.write(f'{st.session_state.input_box}\n')
            success_message=f'{st.session_state.input_box.upper()} 簽到成功'
            st.success(success_message)
            st.session_state.input_box = '' #清空

df=pd.read_csv('id.txt', sep=',')
proxy_list=df.proxy_key.tolist()
#st.markdown('# 龍華國小教師進修簽到 #')
input_result=st.text_input("",max_chars=10,key='input_box',on_change=reset_box)
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




#autofocus的問題 https://discuss.streamlit.io/t/why-does-my-text-input-not-focus-with-script-in-component-html-when-sessionstore-is-unchanged/18289