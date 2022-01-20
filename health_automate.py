import streamlit as st
import streamlit.components.v1 as components
import datetime

injured_part=['頭','頸','肩','胸','腹','背','眼','顏面','口腔','耳鼻喉','上肢','腰','下肢','臀部','會陰部']
trauma_type=['擦傷','割裂刺傷','壓夾傷','挫創傷','扭傷','灼燙傷','叮咬傷','骨折','舊傷','外科其它']
Internal_Medicine_type=['發燒','暈眩','噁心嘔吐','頭痛','牙痛','胃痛','腹痛','腹瀉','經痛','氣喘','流鼻血','疹癢','眼疾','內科其它']
treat_method=['傷口處理','冰敷','熱敷','休息觀察','通知家長','家長帶回','校方送醫','衛生教育','處理其他']
injured_places=['操場','遊戲運動器材','普通教室','專科教室','走廊','樓梯','地下室','體育館活動中心','廁所','校外','其他']
rest_time=[5,10,15,20,25,30,45,60,75,90,120,150,180,240,300,360,420,480,540,600]


time_stamp=datetime.datetime.now()
st.title("龍華國小傷病管理系統")
st.write("登記時間",time_stamp)

st.header("基本資料")
col1,col2,col3=st.columns(3)
grade=col1.selectbox('年級',range(1,7))
classes=col2.selectbox('班級',range(1,16))
numbers=col3.selectbox('座號',range(1,35))
str(classes).zfill(2)
basic_data=str(grade)+str(classes).zfill(2)+str(numbers).zfill(2)

with st.expander("補充資料"):
    colx,coly,colz=st.columns(3)
    if colx.checkbox("記錄體溫"):
        colx.slider("體溫",34.0,40.0,36.0,0.1)

    if coly.checkbox("紀錄休息觀察時間"):
        selected_rest_time=coly.selectbox("休息觀察時間",range(0,240,5),index=0)
    if colz.checkbox("紀錄受傷地點"):
        colz.selectbox("受傷地點",injured_places)

st.write('------------')
st.header("受傷部位")
injured_area = st.multiselect('可多選',injured_part)
injured_part_result=[]
for i in injured_area:
    selected_number=injured_part.index(i)
    injured_part_result.append(selected_number)

st.write('------------')
st.header("外傷")
trauma = st.multiselect('可多選',trauma_type)
trauma_result=[]
for i in trauma:
    selected_number=trauma_type.index(i)
    trauma_result.append(selected_number)

st.write('------------')
st.header("內科")
Internal_Medicine = st.multiselect('可多選',Internal_Medicine_type)
Internal_Medicine_result=[]
for i in Internal_Medicine:
    selected_number=Internal_Medicine_type.index(i)
    Internal_Medicine_result.append(selected_number)

st.write('------------')
st.header("處置作為")
treat_method_choice = st.multiselect('可多選',treat_method)
treat_method_result=[]
for i in treat_method_choice:
    selected_number=treat_method.index(i)
    treat_method_result.append(selected_number)

st.write(injured_part_result)
st.write(trauma_result)

st.write(Internal_Medicine_result)
st.write(treat_method_result)

