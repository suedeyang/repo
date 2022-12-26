'''
https://developers.notion.com/reference/intro
建立資料庫
從URL找到databaseid 
建立integration
右上角 三點 connections
'''

import requests,json
token = ''
database_ID = ''
headers = {
    "Authorization": f"Bearer {token}", #問題出在Bearer與token之間的空格
    "Notion-Version":"2022-06-28"
}


def readDatabase(headers, database_ID):
    readurl = f'https://api.notion.com/v1/databases/{database_ID}'
    res = requests.get(readurl,headers=headers)
    print(res.status_code) 


readDatabase(headers,database_ID)