'''
說明文件
https://pythonhowtoprogram.com/how-to-update-the-airtable-using-python3/
https://airtable.com/api

ID取得(The ID of this base is)
https://airtable.com/appdbFYpupPu5iPPc/api/docs#curl/introduction

建立一筆紀錄語法
https://airtable.com/appdbFYpupPu5iPPc/api/docs#curl/table:harm-data:create

API KEY
https://airtable.com/account

'''
import datetime
from airtable import Airtable
#The ID of this base is appdbFYpupPu5iPPc.
base_key='appdbFYpupPu5iPPc' #USERID
api_key=""
table_name = 'harm-data'
airtable = Airtable(base_key,table_name,api_key)
#pages=airtable.get_iter()
pages=airtable.get_all()

def transform_str_to_string(input_str):
    final_list=[]
    pre_list=list(input_str.strip("[]").replace(",",""))
    for i in pre_list:
        if ' ' in pre_list:
            pre_list.remove(' ')
    for i in pre_list:
        final_list.append(int(i))
    return final_list

for page in pages:
    print(page)
    stu_ID=page['fields']['ID']
    print(stu_ID)
    #受傷部位 chkPart_0 ~ chkPart_14
    chkPart=transform_str_to_string(page['fields']['injured_area'])
    print(chkPart)
    #外傷 chkState_0 ~ chkState_9
    chkState=transform_str_to_string(page['fields']['trauma'])
    print(chkState)
    #內科 chkState0_0 ~ chkState0_13
    chkState0=transform_str_to_string(page['fields']['Internal_Medicine'])
    print(chkState0)
    #處置作為 chkManage_0 ~ chkState0_8    
    chkManage=transform_str_to_string(page['fields']['treat_method'])
    print(chkManage)
    #紀錄建立時間
    created_date_time=int(page['fields']['Created'][11:13])+8
    print(created_date_time)
    #print(created_date_time[0:4])
    
    print("NEXT")
#    for record in page:
#        print(record['fields']['Internal_Medicine'])
