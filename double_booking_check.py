#import requests
import pandas as pd

df=pd.read_html("http://rnb.kh.edu.tw/booking/schedule_view.jsp?category=facilities&s=523606&selected=2", encoding='utf-8')
print(len(df))
print(type(df))