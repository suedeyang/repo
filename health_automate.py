import streamlit as st
import requests
#import pyautogui
import time

st.set_page_config(
	    layout="centered",  # Can be "centered" or "wide". In the future also "dashboard", etc.
	    initial_sidebar_state="auto",  # Can be "auto", "expanded", "collapsed"
	    page_title="龍華國小傷病登記系統",  # String or None. Strings get appended with "• Streamlit". 
	    page_icon=None,  # String, anything supported by st.image, or None.
        )


reload_html_string = '''
<head>
        <meta http-equiv="refresh" content="2" />
</head>
'''
pre_html_code='''
<!doctype html>
<html>
<head>
<link href="https://cdn.jsdelivr.net/npm/bootstrap@5.1.1/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-F3w7mX95PdgyTmZZMECAngseQB83DfGTowi0iMjiWaeVhAn4FJkqJByhZMI3AhiU" crossorigin="anonymous">
</head>
<body>
<script src="https://cdn.jsdelivr.net/npm/@popperjs/core@2.10.1/dist/umd/popper.min.js" integrity="sha384-W8fXfP3gkOKtndU4JGtKDvXbO53Wy8SZCQHczT5FMiiqmQfUpWbYdTil/SxwZgAN" crossorigin="anonymous"></script>
<script src="https://cdn.jsdelivr.net/npm/bootstrap@5.1.1/dist/js/bootstrap.min.js" integrity="sha384-skAcpIdS7UcVUC05LJ9Dxay8AXcDYfBJqt1CJ85S/CFujBsIzCIv+l9liuYLaMQ/" crossorigin="anonymous"></script>
</body>
'''
#st.markdown(pre_html_code,unsafe_allow_html=True)


button_color_code='''
<style>
div.stButton > button:first-child {
    background-color: #0048ff;
    color:#ffffff;
    font-weight:bold;
}
div.stButton > button:hover {
    background-color: #ffffff;
    color:#0048ff;
    font-weight:bold;
    }
</style>
'''
st.markdown(button_color_code, unsafe_allow_html=True)





fp=open("db.txt",'r')
stu_list=fp.readlines()

#The ID of this base is appdbFYpupPu5iPPc.
KEY=""
endpoint='https://api.airtable.com/v0/appdbFYpupPu5iPPc/harm-data'
endpoint2='https://api.airtable.com/v0/appdbFYpupPu5iPPc/harm-data-history'
def add_to_airtable(basic_data,injured_part_result,trauma_result,Internal_Medicine_result,treat_method_result,body_temperature,obseravtion_time,get_hurt_places):
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
                "get_hurt_places":get_hurt_places,
                "obseravtion_time":obseravtion_time,
                "body_temperature":body_temperature,
                }
            }
        ]
    }
    r=requests.post(endpoint,json=data,headers=headers)
    r2=requests.post(endpoint2,json=data,headers=headers)
    print(r.status_code) #HTTP status code
    print(r2.status_code) #HTTP status code
    return r.status_code,r2.status_code


injured_part=['頭','頸','肩','胸','腹','背','眼','顏面','口腔','耳鼻喉','上肢','腰','下肢','臀部','會陰部']
trauma_type=['擦傷','割裂刺傷','壓夾傷','挫創傷','扭傷','灼燙傷','叮咬傷','骨折','舊傷']
Internal_Medicine_type=['發燒','暈眩','噁心嘔吐','頭痛','牙痛','胃痛','腹痛','腹瀉','經痛','氣喘','流鼻血','疹癢','眼疾']
treat_method=['傷口處理','冰敷','熱敷','休息觀察','通知家長','家長帶回','校方送醫','衛生教育']
injured_places=['','操場','遊戲運動器材','普通教室','專科教室','走廊','樓梯','地下室','體育館活動中心','廁所','校外']
rest_time=[5,10,15,20,25,30,45,60,75,90,120,150,180,240,300,360,420,480,540,600]

#st.sidebar.title("龍華國小傷病管理系統")
st.sidebar.title("1.填寫基本資料")
grade=st.sidebar.selectbox('年級',range(0,7))
if grade == 4:
    classes=st.sidebar.selectbox('班級',range(0,18))
else:
    classes=st.sidebar.selectbox('班級',range(0,16))
numbers=st.sidebar.selectbox('座號',range(0,36))
#body_temperature = None
#obseravtion_time=None
#get_hurt_places=None
basic_data=str(grade)+str(classes).zfill(2)+str(numbers).zfill(2)


body_temperature=[]
obseravtion_time=0
get_hurt_places=0

with st.sidebar.expander("補充資料(體溫、時間、地點)"):
    #colx,coly,colz=st.columns(3)
    if st.checkbox("記錄體溫"):
       body_temperature.append(st.slider("體溫",34.0,40.0,36.0,0.1))
       
    if st.checkbox("紀錄休息觀察時間"):
       #obseravtion_time.append(st.selectbox("休息觀察時間",rest_time))
       pre_obseravtion_time=st.selectbox("休息觀察時間",rest_time)
       obseravtion_time=rest_time.index(pre_obseravtion_time)+1

if grade == 0 or classes == 0 or numbers == 0:
    st.error("先在左邊 輸入班級、姓名、座號")
    st.image("https://pic.pimg.tw/c41666/1560907397-2167670633_n.png",caption='身體部位圖')
if not grade == 0 and not classes == 0 and not numbers == 0:
    if basic_data+"\n" in stu_list:
        messages=f"{grade}年{classes}班{numbers}號 資料驗證正確，登記完傷病資料請按藍色按鈕送出"
        st.success(messages)    
        #html_string = f"<h2>{grade}年{classes}班{numbers}號 小朋友開始登記傷病資料</h>"
        #st.markdown(html_string, unsafe_allow_html=True)
        #st.write(grade,"年",classes,"班",numbers,"號 小朋友開始登記受傷資料")
        fp.close()


        st.header("受傷部位")
        injured_area = st.multiselect('',injured_part)
        injured_part_result=[] #受傷部位結果之串列
        for i in injured_area:
            selected_number=injured_part.index(i)
            injured_part_result.append(selected_number)

        #if st.checkbox("紀錄受傷地點"):
        st.header("受傷地點")
        pre_get_hurt_places=st.selectbox("受傷地點",injured_places)
        get_hurt_places=injured_places.index(pre_get_hurt_places)
        

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
        
        st.write("-------")
        if not injured_part_result  and not trauma_result and not Internal_Medicine_result and not treat_method_result:
            #st.error("請輸入傷病資料")    
            st.empty()
        else:
            if st.button(basic_data+"  輸入完畢 送出資料"):
                x1,x2=add_to_airtable(basic_data,str(injured_part_result),str(trauma_result),str(Internal_Medicine_result),str(treat_method_result),str(body_temperature),obseravtion_time,get_hurt_places)
                #st.write("資料寫入中")
                if x1 > 300 or x2 > 300:
                    st.error("資料寫入失敗，網路部份出了問題，清除資料重新登記")
                    #time.sleep(3)
                    #pyautogui.hotkey("ctrl","F5")
                    st.markdown(reload_html_string, unsafe_allow_html=True)
                else:
                    st.success("資料寫入成功!!")
                    st.balloons()
                    #time.sleep(2)
                    #pyautogui.hotkey("ctrl","F5")
                    st.markdown(reload_html_string, unsafe_allow_html=True)
                    
                    
    else:
        messages=f"龍華國小沒有{grade}年{classes}班{numbers}號 這位小朋友喔!!"
        st.error(messages)
        


