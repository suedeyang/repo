import subprocess
import datetime
import socket
import smtplib
from email.mime.text import MIMEText
import time
import requests,json

teachers_email="收件者電子郵件"
result_1=subprocess.run('iperf3.exe -c 163.32.203.3 -t 5', shell=True,capture_output=True)
result_2=subprocess.run('iperf3.exe -c 163.32.203.3 -t 5 -R', shell=True,capture_output=True)

result_1_std = result_1.stdout.decode("utf-8")
result_2_std = result_2.stdout.decode("utf-8")
#net_speed_test_result_2=subprocess.run('iperf3.exe -c 163.32.203.3 -t 5 -R', shell=True)

#print(result_1.stdout.decode("utf-8"))
# 寄送班級導師電子郵件


def send_gmail(teachers_email,result_1_std, result_2_std):
    dt = str(datetime.datetime.now()).split(".")[0]
    IP_addr = socket.gethostbyname(socket.gethostname())
    gmail_addr = '寄件者電子郵件'
    gmail_pwd = '寄件者密碼'
    email_msg = f'測試機IP位置：{IP_addr}\n測試時間：{dt}\n\n\n {result_1_std} \n\n{result_2_std}'

    mime_text=MIMEText(email_msg, 'plain', 'utf-8')
    mime_text['Subject'] = f'{IP_addr}  {dt}網路測試'
    mime_text['From'] = '龍華Iperf3網路測試'
    mime_text['to'] = "網路管理者"
    # mime_text['Cc']='副本收件者'
    mime_text = mime_text.as_string()  # 送出之前要先轉換為字串
    # send_gmail(gmail_addr,gmail_pwd,to_addrs,mime_text) #注意msg的格式

    smtp_gmail = smtplib.SMTP('smtp.gmail.com', 587)  # 587為ttl的port
    smtp_gmail.ehlo()  # 打招呼說hello
    smtp_gmail.starttls()
    # https://myaccount.google.com/lesssecureapps 低安全性登入要打開
    smtp_gmail.login(gmail_addr, gmail_pwd)
    status = smtp_gmail.sendmail(gmail_addr, teachers_email, mime_text)
    if not status:  # 因為成功的話 回傳的dic會是空的
        print("測試成功")
        time.sleep(3)
    else:
        print('寄送通知信件失敗')
        time.sleep(3)
    smtp_gmail.quit()

    
def readDatabase(headers, database_ID):
    #readurl = f'https://api.notion.com/v1/databases/{database_ID}'
    detail_url = f'https://api.notion.com/v1/databases/{database_ID}/query'
    #res = requests.get(url,headers=headers) #可得到架構但得不到資料庫內的值
    res = requests.post(detail_url, headers=headers) #回傳結果為 page 的 list，正如大家所知，Database 中每一「橫列」代表一個 page


    print(res.status_code) 
    print(res.text)

#readDatabase(headers,database_ID)

token = ''
database_ID = ''
headers = {
    "Authorization": f"Bearer {token}", #問題出在Bearer與token之間的空格
    "Notion-Version":"2022-06-28"
}


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
                        "content": result_1_std + result_2_std
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





#send_gmail(teachers_email, result_1_std, result_2_std)
'''
with open('appendSomething.txt', 'a') as f:
    subprocess.run('iperf3.exe -c 163.32.203.3', shell=True,stdout=f)
    subprocess.run('iperf3.exe -c 163.32.203.3 -R',shell=False,stdout=f)

'''