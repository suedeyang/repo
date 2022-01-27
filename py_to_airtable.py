'''
說明文件
https://airtable.com/api

ID取得(The ID of this base is)
https://airtable.com/appdbFYpupPu5iPPc/api/docs#curl/introduction

建立一筆紀錄語法
https://airtable.com/appdbFYpupPu5iPPc/api/docs#curl/table:harm-data:create

API KEY
https://airtable.com/account

'''



import requests
#The ID of this base is appdbFYpupPu5iPPc.
KEY=""
endpoint='https://api.airtable.com/v0/appdbFYpupPu5iPPc/harm-data'


def add_to_airtable(ID=None,places=""):
    if ID is None:
        return
    #Python requests headers
    headers={
        "Authorization": f'Bearer {KEY}', #注意前面的,
        "Content-Type" : "application/json"
    }

    data= {
    "records": [
            {
            "fields": {
                "ID": ID ,
                "places": places
                }
            }
        ]
    }
    r=requests.post(endpoint,json=data,headers=headers)
    print(r.status_code) #HTTP status code

add_to_airtable("88478","我是中文字")