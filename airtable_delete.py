from airtable import Airtable
import time
base_key='' #USERID
api_key=""
table_name = 'harm-data'
airtable = Airtable(base_key,table_name,api_key)
#pages=airtable.get_all()
#print("今天共有",len(pages),"筆資料要登載，工作即將開始") #共有幾筆資料要登載
pages=airtable.get_all()
for page in pages:
    data_id=page['id']
    print(data_id)
    time.sleep(3)
    airtable.delete(data_id)