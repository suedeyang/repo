
import requests

url_UVI="https://data.epa.gov.tw/api/v2/uv_s_01?api_key=1a533517-0c08-4d8f-9948-f3706970a4e5&format=json&filters=sitename,eq,高雄&limit=1"
uvi_datas=requests.get(url_UVI).json()['records']
print(uvi_datas[0]['uvi'])
print(uvi_datas[0]['publishtime'])