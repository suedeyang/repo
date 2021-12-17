from pandas.io.html import read_html
import streamlit as st
import pandas as pd

url="http://school.kh.edu.tw/view/index.php?WebID=180&MainType=103&SubType=0&MainMenuId=69026&SubMenuId=0&NowMainId=69026&NowSubId=0"
html=pd.read_html(url,header=0)
df=html[0]
df.drop(['NO.'],axis=1)
df=df.fillna("")
#st.dataframe(df.astype(str))


class_1=st.sidebar.multiselect("班級1",df.職稱.unique()[7:93])
#names=st.sidebar.multiselect("姓名",df.姓名)
class_2=st.sidebar.multiselect("班級2",df.職稱.unique()[7:93])


selected_data=df[ (df.職稱.isin(class_1)) | (df.職稱.isin(class_2)) ] # 過濾資料  |代表or &代表and

#st.write(class_1)
def class_filter(input_class):
    input_class=input_class[0].replace("-","0")
    if len(input_class) == 4:
        input_class = input_class.replace("0","")
    if len(input_class) == 3:
        input_class = input_class
    return input_class



col1,col2=st.columns(2)
if class_1:
    st.dataframe(selected_data.astype(str))
    col1.image(f"http://www2.lhps.kh.edu.tw/online-portal/html/imgs/{class_filter(class_1) }.jpg")
if class_2:
    col2.image(f"http://www2.lhps.kh.edu.tw/online-portal/html/imgs/{class_filter(class_2) }.jpg")

#st.image(f"http://www2.lhps.kh.edu.tw/online-portal/html/imgs/{selected_class_1 }.jpg")
#result=df[(df.isin(titles))]
#st.dataframe(result.astype(str))