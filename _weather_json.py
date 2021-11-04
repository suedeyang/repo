import requests
import pandas as pd
import datetime 
import time

url='https://data.epa.gov.tw/api/v1/aqx_p_432?limit=1000&api_key=9be7b239-557b-4c10-9775-78cadfc555e9&sort=ImportDate%20desc&format=json'

while True:
    raw_data=requests.get(url)
    datas=raw_data.json()['records']#要寫成data.json()['stats']解析才會正確
    for data in datas:
        if data['SiteName'] == '左營':
            print(data['AQI'])
            print(datetime.datetime.now())
    time.sleep(5)


'''
df=pd.DataFrame(price)
df.columns=['datetime','twd']
#print(df.head(1))

df['datetime']=pd.to_datetime(df['datetime'], unit='ms')
print(df.head())


df.index=df['datetime']
df['twd'].plot(kind='line',figsize=[20,5])

'''