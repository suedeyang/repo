import streamlit as st
import streamlit.components.v1 as components
import pandas as pd
import time
import re
import requests

KEY=''
endpoint='https://api.airtable.com/v0/appCY8QfugFWkKMvH/id'

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


reload_html_string = '''
<head>
        <meta http-equiv="refresh" content="0" />
</head>
'''

df=pd.read_csv('id.txt', sep=',')
proxy_list=df.proxy_key.tolist()
st.title("龍華國小研習簽到")
input_result=st.text_input("請 感應電梯磁扣 或 輸入身分證號後按ENTER鍵",max_chars=10)

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

if input_result:
    if input_result.isdigit():
        if input_result in proxy_list:
            index_number=proxy_list.index(input_result)
            ID=df.ID_number[index_number].upper()
            airtable_response=add_to_airtable(ID)
            if airtable_response > 300:
                st.error('網路傳送失敗，請重新簽到')
                time.sleep(1)
                st.markdown(reload_html_string, unsafe_allow_html=True)
            else:
                success_message=f'{ID} 簽到成功'
                st.success(success_message)
                time.sleep(0.5)
                st.markdown(reload_html_string, unsafe_allow_html=True)
        else:
            st.error('電梯感應扣未註冊，請改輸入身分證號')
            time.sleep(1)
            st.markdown(reload_html_string, unsafe_allow_html=True)
    else:
        id_check=re.fullmatch("^[A-Z][12][0-9]{8}$",input_result.upper())
        if id_check == None:
            st.error('身分證字號輸入錯誤，請重新輸入')
            time.sleep(1)
            st.markdown(reload_html_string, unsafe_allow_html=True)
        else:
            airtable_response=add_to_airtable(input_result.upper())
            if airtable_response > 300:
                st.error('網路傳送失敗，請重新簽到')
                time.sleep(1)
                st.markdown(reload_html_string, unsafe_allow_html=True)
            else:
                success_message=f'{input_result.upper()} 簽到成功'
                st.success(success_message)
                time.sleep(0.5)
                st.markdown(reload_html_string, unsafe_allow_html=True)



#autofocus的問題 https://discuss.streamlit.io/t/why-does-my-text-input-not-focus-with-script-in-component-html-when-sessionstore-is-unchanged/18289