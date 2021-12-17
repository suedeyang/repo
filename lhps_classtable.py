import streamlit as st
import pandas as pd

url="http://school.kh.edu.tw/view/index.php?WebID=180&MainType=103&SubType=0&MainMenuId=69026&SubMenuId=0&NowMainId=69026&NowSubId=0"
html=pd.read_html(url,header=0)
df=html[0]
df.drop(['NO.'],axis=1)
df=df.fillna("")
#st.dataframe(df.astype(str))

#st.write(class_1)
st.sidebar.header("請選擇班級或科任老師(可多選)")
class_1=st.sidebar.multiselect("班級",df.職稱.unique()[7:93],help="可一次選取多個班級")
names=st.sidebar.multiselect("科任老師",df.姓名[118:176],help="可一次選取多個老師")

combine_list=class_1+names

final_result_list=[]
for i in combine_list:
    i=i.replace("-","0")
    if len(i) == 4:
        i=i.replace("0","")
        final_result_list.append(i)
    else:
        final_result_list.append(i)


selected_data=df[ (df.職稱.isin(class_1)) | (df.姓名.isin(names)) ] # 過濾資料  |代表or &代表and

if class_1 or names:
    #selected_data=df[ (df.職稱.isin(class_1))]
    st.markdown("""[龍華國小教職員工連結](http://school.kh.edu.tw/view/index.php?WebID=180&MainType=103&SubType=0&MainMenuId=69026&SubMenuId=0&NowMainId=69026&NowSubId=0).""")
    st.header("查詢清單")
    st.dataframe(selected_data.astype(str))
for i in final_result_list:
    st.image(f"http://www2.lhps.kh.edu.tw/online-portal/html/imgs/{i}.jpg")
    st.write("---------------")
