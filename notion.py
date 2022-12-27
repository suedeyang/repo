'''
https://dragonflykuo.com/%E4%B8%B2%E6%8E%A5-notion-api%E7%94%A8-python-%E8%87%AA%E7%94%B1%E6%93%8D%E4%BD%9C-notion/
https://dragonflykuo.com/%e3%80%90notionapi-2%e3%80%91python-%e6%96%b0%e5%a2%9e%e3%80%81%e4%bf%ae%e6%94%b9%e3%80%81%e5%88%aa%e9%99%a4-notion-database-page/
https://coding.tools/tw/json-formatter

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
    #readurl = f'https://api.notion.com/v1/databases/{database_ID}'
    detail_url = f'https://api.notion.com/v1/databases/{database_ID}/query'
    #res = requests.get(url,headers=headers) #可得到架構但得不到資料庫內的值
    res = requests.post(detail_url, headers=headers) #回傳結果為 page 的 list，正如大家所知，Database 中每一「橫列」代表一個 page


    print(res.status_code) 
    print(res.text)


#readDatabase(headers,database_ID)


'''
pages — 由於 Database 中每一「橫列」代表一個 page，因此新增 database 內部資料實際上就是創建 page
data — 創建這個 page 所想要帶的資料，必須包含：
    parent
    properties
'''

def update_database(database_ID,headers):
    url = "https://api.notion.com/v1/pages"
    data={
        "parent": {
            "type": "database_id",
            "database_id": database_ID
        },
        "properties": {
            "評價": {
                #"id": "cpFp",
                "type": "rich_text",
                "rich_text": [{
                    "type": "text",
                    "text": {
                        "content": "BBBBBB",
                        #"link": null
                    },
                }]
            },
            
            "書名": {
                #"id": "title",
                "type": "title",
                "title": [{
                    "type": "text",
                    "text": {
                        "content": "AAAAAA",
                    },
                    
                }]
            }
        }
    }

    #data=json.dumps(new_data)
    update_res = requests.post (url, headers=headers,json=data)
    print(update_res.status_code)

update_database(database_ID,headers)