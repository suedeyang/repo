from urllib import response
import streamlit as st
import streamlit.components.v1 as components
import requests
import pyautogui
import time

#The ID of this base is appdbFYpupPu5iPPc.
KEY=""
endpoint='https://api.airtable.com/v0/appdbFYpupPu5iPPc/harm-data'

def add_to_airtable(basic_data,injured_part_result,trauma_result,Internal_Medicine_result,treat_method_result):
    #Python requests headers
    headers={
        "Authorization": f'Bearer {KEY}', #注意前面的,
        "Content-Type" : "application/json"
    }

    data= {
    "records": [
            {
            "fields": {
                "ID": basic_data ,
                "injured_area":injured_part_result,
                "trauma": trauma_result,
                "Internal_Medicine":Internal_Medicine_result,
                "treat_method":treat_method_result,
                }
            }
        ]
    }
    r=requests.post(endpoint,json=data,headers=headers)
    print(r.status_code) #HTTP status code
    return r.status_code

injured_part=['頭','頸','肩','胸','腹','背','眼','顏面','口腔','耳鼻喉','上肢','腰','下肢','臀部','會陰部']
trauma_type=['擦傷','割裂刺傷','壓夾傷','挫創傷','扭傷','灼燙傷','叮咬傷','骨折','舊傷','外科其它']
Internal_Medicine_type=['發燒','暈眩','噁心嘔吐','頭痛','牙痛','胃痛','腹痛','腹瀉','經痛','氣喘','流鼻血','疹癢','眼疾','內科其它']
treat_method=['傷口處理','冰敷','熱敷','休息觀察','通知家長','家長帶回','校方送醫','衛生教育','處理其他']
injured_places=['操場','遊戲運動器材','普通教室','專科教室','走廊','樓梯','地下室','體育館活動中心','廁所','校外','其他']
rest_time=[5,10,15,20,25,30,45,60,75,90,120,150,180,240,300,360,420,480,540,600]

#st.sidebar.title("龍華國小傷病管理系統")
st.sidebar.title("1.填寫基本資料")
grade=st.sidebar.selectbox('年級',range(0,7))
classes=st.sidebar.selectbox('班級',range(0,16))
numbers=st.sidebar.selectbox('座號',range(0,35))
basic_data=str(grade)+str(classes).zfill(2)+str(numbers).zfill(2)


with st.sidebar.expander("補充資料"):
    #colx,coly,colz=st.columns(3)
    if st.checkbox("記錄體溫"):
       body_temperature=st.slider("體溫",34.0,40.0,36.0,0.1)
    if st.checkbox("紀錄休息觀察時間"):
       obseravtion_time=st.selectbox("休息觀察時間",range(0,240,5),index=0)
    if st.checkbox("紀錄受傷地點"):
       get_hurt_places=st.selectbox("受傷地點",injured_places)

if grade == 0 or classes == 0 or numbers == 0:
    st.sidebar.error("請先輸入正確的基本資料")
    st.image("https://pic.pimg.tw/c41666/1560907397-2167670633_n.png",caption='身體部位圖')
if not grade == 0 and not classes == 0 and not numbers == 0:
    st.write(grade,"年",classes,"班",numbers,"號 小朋友開始登記資料")

    st.header("受傷部位")
    injured_area = st.multiselect('',injured_part)
    injured_part_result=[] #受傷部位結果之串列
    for i in injured_area:
        selected_number=injured_part.index(i)
        injured_part_result.append(selected_number)

    st.write('------------')
    st.header("外傷")
    trauma = st.multiselect('',trauma_type)
    trauma_result=[]
    for i in trauma:
        selected_number=trauma_type.index(i)
        trauma_result.append(selected_number)

    st.write('------------')
    st.header("內科")
    Internal_Medicine = st.multiselect('',Internal_Medicine_type)
    Internal_Medicine_result=[]
    for i in Internal_Medicine:
        selected_number=Internal_Medicine_type.index(i)
        Internal_Medicine_result.append(selected_number)

    st.write('------------')
    st.header("處置作為")
    treat_method_choice = st.multiselect('',treat_method)
    treat_method_result=[]
    for i in treat_method_choice:
        selected_number=treat_method.index(i)
        treat_method_result.append(selected_number)
    if not injured_part_result  and not trauma_result and not Internal_Medicine_result and not treat_method_result:
        st.error("請輸入資料")    
    else:
        if st.button(basic_data+"  輸入完畢 提交資料"):
            x=add_to_airtable(basic_data,str(injured_part_result),str(trauma_result),str(Internal_Medicine_result),str(treat_method_result))
            #st.write("資料寫入中")
            if x > 300:
                st.error("資料寫入失敗，清除資料重新登記")
                time.sleep(3)
                pyautogui.hotkey("ctrl","F5")
            else:
                st.success("資料寫入成功!!")
                st.balloons()
                time.sleep(2)
                pyautogui.hotkey("ctrl","F5")