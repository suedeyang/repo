import streamlit as st
import requests
#import pyautogui
import time
import smtplib
from email.mime.text import MIMEText
import pandas as pd
import datetime
<<<<<<< Updated upstream


=======
>>>>>>> Stashed changes

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
st.markdown(pre_html_code,unsafe_allow_html=True)
'''

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

#找出老師的電子郵件信箱
def find_class_teachers(classes_of_student):
    url="http://school.kh.edu.tw/view/index.php?WebID=180&MainType=103&SubType=0&MainMenuId=69026&SubMenuId=0&NowMainId=69026&NowSubId=0"
    html=pd.read_html(url,header=0)
    df=html[0]
    df.drop(['NO.'],axis=1)
    df=df.fillna("")
    final_class_result_list=[]
    
    classes=list(df.職稱)
    for i in classes:
        i=i.replace("-","0")
        if len(i) == 4:
            i=i.replace("0","",1)
            final_class_result_list.append(str(i))
        else:
            final_class_result_list.append(str(i))
    
    index_number=final_class_result_list.index(classes_of_student)
    return df.Email[index_number],df.姓名[index_number]

#寄送班級導師電子郵件
def send_gmail(basic_data,teachers_email,teachers_name,injured_area,trauma,pre_get_hurt_places,Internal_Medicine,treat_method_choice,body_temperature,pre_obseravtion_time):
    dt=datetime.datetime.now()
    gmail_addr='suedeyang@mail.lhps.kh.edu.tw'
    gmail_pwd='uy9wwd7r'
    email_msg=f'{teachers_name}老師您好：\n貴班{basic_data}小朋友於健康中心登記傷病，特此通知，登載資料如下：\n時間：{dt.strftime("%Y/%m/%d %H:%M:%S")}\n受傷部位：{injured_area}\n外傷種類：{trauma}\n受傷地點：{pre_get_hurt_places}\n症狀：{Internal_Medicine}\n處置作為：{treat_method_choice}\n記錄體溫：{body_temperature}\n紀錄休息觀察時間：{pre_obseravtion_time}\n\n若有任何問題勿回信，請直接與健康中心聯絡'
    
    mime_text=MIMEText(email_msg,'plain','utf-8')
    mime_text['Subject']=f'{basic_data}傷病資料'
    mime_text['From']='龍華國小健康中心'
    mime_text['to']=f'{basic_data}班級老師{teachers_name}'
    #mime_text['Cc']='副本收件者'
    mime_text=mime_text.as_string() #送出之前要先轉換為字串
    #send_gmail(gmail_addr,gmail_pwd,to_addrs,mime_text) #注意msg的格式
    
    smtp_gmail=smtplib.SMTP('smtp.gmail.com',587) #587為ttl的port
    smtp_gmail.ehlo() #打招呼說hello
    smtp_gmail.starttls()
    smtp_gmail.login(gmail_addr,gmail_pwd) #https://myaccount.google.com/lesssecureapps 低安全性登入要打開
    status=smtp_gmail.sendmail(gmail_addr,teachers_email,mime_text)
    if not status:  #因為成功的話 回傳的dic會是空的
        st.success("導師通知信 寄送成功")
    else:
        st.error('導師通知信 寄信失敗 不過沒關係，不需要重新登記')
    smtp_gmail.quit()

#資料寫入airtable
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


injured_part=['頭','脖子','肩','胸','肚子','背','眼','臉','嘴巴(含牙齒)','耳鼻喉','手','腰','腳','屁股','會陰部']
trauma_type=['擦傷','割裂刺傷','壓夾傷','挫撞傷','扭傷','灼燙傷','叮咬傷','骨折','舊傷']
Internal_Medicine_type=['發燒','暈眩','噁心嘔吐','頭痛','牙痛','胃痛','腹痛','腹瀉','經痛','氣喘','流鼻血','疹癢','眼疾']
treat_method=['傷口處理','冰敷','熱敷','休息觀察','通知家長','家長帶回','校方送醫','衛生教育','其他']
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
classes_of_student=str(grade)+str(classes).zfill(2)

pre_obseravtion_time=[]
pre_get_hurt_places=[]
body_temperature=[]
obseravtion_time=0
get_hurt_places=0

with st.sidebar.expander("補充資料(體溫、時間)"):
    #colx,coly,colz=st.columns(3)
    if st.checkbox("記錄體溫"):
       body_temperature.append(st.slider("體溫",34.0,40.0,36.0,0.1))
       
    if st.checkbox("紀錄休息觀察時間"):
       #obseravtion_time.append(st.selectbox("休息觀察時間",rest_time))
       pre_obseravtion_time=st.selectbox("休息觀察時間",rest_time)
       obseravtion_time=rest_time.index(pre_obseravtion_time)+1

if grade == 0 or classes == 0 or numbers == 0:
    st.error("先在左邊 輸入班級、姓名、座號")
    #st.image("https://pic.pimg.tw/c41666/1560907397-2167670633_n.png",caption='身體部位圖')
if not grade == 0 and not classes == 0 and not numbers == 0:
    if basic_data+"\n" in stu_list:
        messages=f"{grade}年{classes}班{numbers}號 資料驗證正確，登記完傷病資料請按藍色按鈕送出"
        st.success(messages)
        fp.close()

        st.header("部位")
        injured_area = st.multiselect('',injured_part)
        injured_part_result=[] #受傷部位結果之串列
        for i in injured_area:
            selected_number=injured_part.index(i)
            injured_part_result.append(selected_number)       

        st.header("外傷種類")
        trauma = st.multiselect('',trauma_type)
        trauma_result=[]
        for i in trauma:
            selected_number=trauma_type.index(i)
            trauma_result.append(selected_number)

<<<<<<< Updated upstream
        if trauma:
            st.header("受傷地點(外傷需點選)")
            pre_get_hurt_places=st.selectbox("",injured_places)
            get_hurt_places=injured_places.index(pre_get_hurt_places)


        st.write('------------')
=======
>>>>>>> Stashed changes
        st.header("症狀")
        Internal_Medicine = st.multiselect('',Internal_Medicine_type)
        Internal_Medicine_result=[]
        for i in Internal_Medicine:
            selected_number=Internal_Medicine_type.index(i)
            Internal_Medicine_result.append(selected_number)

<<<<<<< Updated upstream
        st.write('------------')
=======
        #if st.checkbox("紀錄受傷地點"):
        st.header("受傷地點(外傷需點選)")
        pre_get_hurt_places=st.selectbox("受傷地點",injured_places)
        get_hurt_places=injured_places.index(pre_get_hurt_places)

>>>>>>> Stashed changes
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
                    teachers_email,teachers_name=find_class_teachers(classes_of_student)
                    send_gmail(basic_data,teachers_email,teachers_name,injured_area,trauma,pre_get_hurt_places,Internal_Medicine,treat_method_choice,body_temperature,pre_obseravtion_time)
                    st.balloons()
                    #time.sleep(2)
                    #pyautogui.hotkey("ctrl","F5")
                    st.markdown(reload_html_string, unsafe_allow_html=True)
<<<<<<< Updated upstream
                       
=======
                                        
>>>>>>> Stashed changes
    else:
        messages=f"龍華國小沒有{grade}年{classes}班{numbers}號 這位小朋友喔!!"
        st.error(messages)
        


