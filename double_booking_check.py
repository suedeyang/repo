from time import time
import requests
from bs4 import BeautifulSoup
import pandas as pd
import streamlit as st


time_table=pd.read_html('http://rnb.kh.edu.tw/booking/schedule_view.jsp?category=facilities&item_sn=4468&s=523606&selected=2',encoding = 'utf8')
for i in time_table:
    print(i)