from numpy import isin
import streamlit as st
import pandas as pd
classrooms=["自然教室1","自然教室2","自然教室3","自然教室4","自然教室5","自然教室6","自然教室7","蝴蝶園教室","電腦教室1","電腦教室2","電腦教室3","語言教室1","語言教室2","表演藝術教室","音樂教室2","協同教室","美勞教室1","美勞教室2","美勞教室3"]


url="http://school.kh.edu.tw/view/index.php?WebID=180&MainType=103&SubType=0&MainMenuId=69026&SubMenuId=0&NowMainId=69026&NowSubId=0"
html=pd.read_html(url,header=0)
df=html[0]
df.drop(['NO.'],axis=1)
df=df.fillna("")
#st.dataframe(df.astype(str))
final_class_result_list=[]

classes=list(df.職稱)
for i in classes:
    i=i.replace("-","0")
    if len(i) == 4:
        i=i.replace("0","",1)
        final_class_result_list.append(str(i))
    else:
        final_class_result_list.append(str(i))

index_number=final_class_result_list.index("107")
st.write(final_class_result_list)
st.write(index_number)
df.Email[13]




if "4-6=" in classes:
    st.write("yes")
#st.write(classes)
#st.write(len(df.Email))

'''
#st.write(class_1)
st.sidebar.header("請選擇班級或科任老師(可多選)")
class_1=st.sidebar.multiselect("班級",df.職稱.unique()[7:93],help="可一次選取多個班級")
special_names=st.sidebar.multiselect("主任",df.姓名[1:5],help="可一次選取多位老師")
names=st.sidebar.multiselect("科任老師",df.姓名[118:176],help="可一次選取多位老師")
select_classroom = st.sidebar.multiselect("專科教室", classrooms ,help="可一次選取多間教室")
combine_list=class_1+names+select_classroom+special_names
#st.write(combine_list)
final_result_list=[]
'''