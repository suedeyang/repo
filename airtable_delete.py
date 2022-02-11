from airtable import Airtable

base_key='' #USERID
api_key=""
table_name = 'harm-data'
airtable = Airtable(base_key,table_name,api_key)
#pages=airtable.get_all()
#print("今天共有",len(pages),"筆資料要登載，工作即將開始") #共有幾筆資料要登載
airtable.delete_by_field('ID', '20317')