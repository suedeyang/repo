import streamlit as st
import pandas as pd

classrooms=["自然教室1","自然教室2","自然教室3","自然教室4","自然教室5","自然教室6","自然教室7","電腦教室1","電腦教室2","電腦教室3","語言教室1","語言教室2","表演藝術教室","音樂教室2","協同教室"]
selected_classroom=[]
url="http://school.kh.edu.tw/view/index.php?WebID=180&MainType=103&SubType=0&MainMenuId=69026&SubMenuId=0&NowMainId=69026&NowSubId=0"
html=pd.read_html(url,header=0)
df=html[0]
df.drop(['NO.'],axis=1)
df=df.fillna("")
#st.dataframe(df.astype(str))




#st.write(class_1)
st.sidebar.header("請選擇班級或科任老師(可多選)")
class_1=st.sidebar.multiselect("班級",df.職稱.unique()[7:93],help="可一次選取多個班級")
special_names=st.sidebar.multiselect("主任",df.姓名[1:5],help="可一次選取多位老師")
names=st.sidebar.multiselect("科任老師",df.姓名[118:176],help="可一次選取多位老師")
st.sidebar.write("教室功能做到一半還沒完全弄好")
select_classroom = st.sidebar.multiselect("專科教室", classrooms ,help="可一次選取多間教室")

combine_list=class_1+names+select_classroom+special_names
#st.write(combine_list)


final_result_list=[]
for i in combine_list:
    i=i.replace("-","0")
    if len(i) == 4:
        i=i.replace("0","")
        final_result_list.append(str(i))
    else:
        final_result_list.append(str(i))


selected_data=df[ (df.職稱.isin(class_1)) | (df.姓名.isin(names))| (df.姓名.isin(special_names)) ] # 過濾資料  |代表or &代表and

if class_1 or names or selected_classroom or special_names:
    #selected_data=df[ (df.職稱.isin(class_1))]
    st.markdown("""
    * [龍華國小教職員工連結](http://school.kh.edu.tw/view/index.php?WebID=180&MainType=103&SubType=0&MainMenuId=69026&SubMenuId=0&NowMainId=69026&NowSubId=0)
    * [場地預約系統](http://rnb.kh.edu.tw/booking/schedule_view.jsp?s=523606)
    """)
    st.header("查詢清單")
    st.dataframe(selected_data.astype(str))
for i in final_result_list:
    st.image(f"http://163.16.245.102/online-portal/html/imgs/{i}.jpg")
    st.write("---------------")