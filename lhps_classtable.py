import streamlit as st
import pandas as pd
#from PIL import Image
import requests
import streamlit.components.v1 as components
#from streamlit_lottie import st_lottie




def load_lottieurl(url: str):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

classrooms=["自然教室1","自然教室2","自然教室3","自然教室4","自然教室5","自然教室6","自然教室7","自然教室8","蝴蝶園教室","電腦教室1","電腦教室2","電腦教室3","語言教室1","語言教室2","表演藝術教室","音樂教室2","協同教室","美勞教室1","美勞教室2","美勞教室3"]
selected_classroom=[]
url = "http://www.lhps.kh.edu.tw/view/index.php?WebID=180&MainType=0&SubType=103&MainMenuId=9277&SubMenuId=74138&NowMainId=9277&NowSubId=74138"


html=pd.read_html(url,header=0)
df=html[0]
df.drop(['NO.'],axis=1)
df=df.fillna("")
#st.dataframe(df.astype(str))


#st.write(class_1)
st.sidebar.header("請選擇班級或科任老師(可多選)")
class_1=st.sidebar.multiselect("班級",df.職稱.unique()[7:91],help="可一次選取多個班級")
special_names=st.sidebar.multiselect("主任",df.姓名[1:5],help="可一次選取多位老師")
names=st.sidebar.multiselect("科任老師",df.姓名[117:172],help="可一次選取多位老師")
select_classroom = st.sidebar.multiselect("專科教室", classrooms ,help="可一次選取多間教室")
combine_list=class_1+names+select_classroom+special_names
#st.write(combine_list)
final_result_list=[]



for i in combine_list:
    i=i.replace("-","0")
    if len(i) == 4:
        i=i.replace("0","",1)
        final_result_list.append(str(i))
    else:
        final_result_list.append(str(i))


selected_data=df[ (df.職稱.isin(class_1)) | (df.姓名.isin(names))| (df.姓名.isin(special_names)) ] # 過濾資料  |代表or &代表and

if class_1 or names or selected_classroom or special_names:
    #selected_data=df[ (df.職稱.isin(class_1))]
    st.markdown("""
    * [**龍華國小教職員工**](https://www.lhps.kh.edu.tw/view/index.php?WebID=180&MainType=0&SubType=103&MainMenuId=9277&SubMenuId=74138&NowMainId=9277&NowSubId=74138)
    * [**場地預約系統**](http://rnb.kh.edu.tw/booking/schedule_view.jsp?s=523606)
    * [**龍華國小行事曆**](https://calendar.google.com/calendar/u/0/embed?src=0jpbrq0murj8pmbkfq13ekc12o@group.calendar.google.com&ctz=Asia/Taipei)
    """)
    st.header("查詢清單")
    st.dataframe(selected_data.astype(str))
else:
    st.caption("點選左上角的 > 開始查詢課表")
    #lottie_url_hello ="https://assets6.lottiefiles.com/packages/lf20_i7ooqm2q.json"
    #lottie_hello = load_lottieurl(lottie_url_hello)
    #st_lottie(lottie_hello, key="hello")

for i in final_result_list:
    #st.image(f'https://raw.githubusercontent.com/suedeyang/img/main/{i}.jpg')
    st.image(f'https://www2.lhps.kh.edu.tw/online-portal/html/imgs/{i}.jpg')
    #img=Image.open(requests.get(f"http://163.16.245.102/online-portal/html/imgs/{i}.jpg",stream=True).raw)
    #st.image(img)
    #st.markdown(f'<img width="90%" src=http://163.16.245.102/online-portal/html/imgs/{i}.jpg>',unsafe_allow_html=True)
    st.write("---------------")

components.html(
    """
    <a href="https://www.freecounterstat.com" title="website hit counter"><img src="https://counter7.stat.ovh/private/freecounterstat.php?c=1xxbkaede12twl3y6j9xfydj5w3bkw35" border="0" title="website hit counter" alt="website hit counter"></a>
    """
)
