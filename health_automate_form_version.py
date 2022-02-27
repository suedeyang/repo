import streamlit as st
import streamlit.components.v1 as components
import requests
import pyautogui
import time

fp=open("db.txt",'r')
stu_list=fp.readlines()


#The ID of this base is appdbFYpupPu5iPPc.
KEY=""
endpoint='https://api.airtable.com/v0/appdbFYpupPu5iPPc/harm-data'

injured_part=['頭','頸','肩','胸','腹','背','眼','顏面','口腔','耳鼻喉','上肢','腰','下肢','臀部','會陰部']
trauma_type=['擦傷','割裂刺傷','壓夾傷','挫創傷','扭傷','灼燙傷','叮咬傷','骨折','舊傷','外科其它']
Internal_Medicine_type=['發燒','暈眩','噁心嘔吐','頭痛','牙痛','胃痛','腹痛','腹瀉','經痛','氣喘','流鼻血','疹癢','眼疾','內科其它']
treat_method=['傷口處理','冰敷','熱敷','休息觀察','通知家長','家長帶回','校方送醫','衛生教育','處理其他']
injured_places=['操場','遊戲運動器材','普通教室','專科教室','走廊','樓梯','地下室','體育館活動中心','廁所','校外','其他']
rest_time=[5,10,15,20,25,30,45,60,75,90,120,150,180,240,300,360,420,480,540,600]
body_temperature=[]
obseravtion_time=[]
get_hurt_places=[]


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
    print(r.status_code) #HTTP status code
    return r.status_code




form = st.form("basic_data",clear_on_submit=True)
#st.sidebar.title("龍華國小傷病管理系統")
form.title("1.填寫基本資料")
grade=form.selectbox('年級',range(0,7))
classes=form.selectbox('班級',range(0,16))
numbers=form.selectbox('座號',range(0,35))
basic_data=str(grade)+str(classes).zfill(2)+str(numbers).zfill(2)
form.write(basic_data)
#body_temperature = None
#obseravtion_time=None
#get_hurt_places=None
submit1=form.form_submit_button("Submit")
if submit1:
    if not basic_data+"\n" in stu_list:
        form.error("龍華國小沒這位小朋友喔")
    else:
        fp.close()
        st.write(grade,"年",classes,"班",numbers,"號 小朋友開始登記受傷資料")
        form2 = st.form("my_form2",clear_on_submit=True)   
    
        form2.header("受傷部位")
        injured_area = form2.multiselect('',injured_part)
        injured_part_result=[] #受傷部位結果之串列
        for i in injured_area:
            selected_number=injured_part.index(i)
            injured_part_result.append(selected_number)
        form2.write('------------')
        form2.header("外傷")
        trauma = form2.multiselect('',trauma_type)
        trauma_result=[]
        for i in trauma:
            selected_number=trauma_type.index(i)
            trauma_result.append(selected_number)
        form2.write('------------')
        form2.header("內科")
        Internal_Medicine = form2.multiselect('',Internal_Medicine_type)
        Internal_Medicine_result=[]
        for i in Internal_Medicine:
            selected_number=Internal_Medicine_type.index(i)
            Internal_Medicine_result.append(selected_number)
        form2.write('------------')
        form2.header("處置作為")
        treat_method_choice = form2.multiselect('',treat_method)
        treat_method_result=[]
        for i in treat_method_choice:
            selected_number=treat_method.index(i)
            treat_method_result.append(selected_number)
        form2.write("-------")

        if form2.form_submit_button("輸入完畢"):
            if not injured_part_result  and not trauma_result and not Internal_Medicine_result and not treat_method_result:
                form2.error("請先輸入基本資料與傷病資料")    
            else:         
            #if st.button(basic_data+"  輸入完畢 提交資料"):
                x=add_to_airtable(basic_data,str(injured_part_result),str(trauma_result),str(Internal_Medicine_result),str(treat_method_result),str(body_temperature),str(obseravtion_time),str(get_hurt_places))
                if x > 300:
                    st.error("資料寫入失敗，清除資料重新登記")
                    time.sleep(3)
                    #pyautogui.hotkey("ctrl","F5")
                else:
                    st.success("資料寫入成功!!")
                    st.balloons()
                    time.sleep(1)
                    #pyautogui.hotkey("ctrl","F5")
        
        
        #pass
with st.expander("補充資料"):
    colx,coly,colz=st.columns(3)
    if colx.checkbox("記錄體溫"):
       body_temperature.append(st.slider("體溫",34.0,40.0,36.0,0.1))
    if coly.checkbox("紀錄休息觀察時間"):
       obseravtion_time.append(st.selectbox("休息觀察時間",rest_time))
    if colz.checkbox("紀錄受傷地點"):       
       get_hurt_places.append(st.selectbox("受傷地點",injured_places))


#st.write("體溫：",body_temperature[0],)





    
   


st.write(basic_data)

