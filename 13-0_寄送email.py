import smtplib
from email.mime.text import MIMEText


def send_gmail(gmail_addr,gmail_pwd,to_addrs,msg):
    smtp_gmail=smtplib.SMTP('smtp.gmail.com',587) #587為ttl的port
    print(smtp_gmail.ehlo()) #打招呼說hello
    print(smtp_gmail.starttls()) 
    print(smtp_gmail.login(gmail_addr,gmail_pwd)) #https://myaccount.google.com/lesssecureapps 低安全性登入要打開
    status=smtp_gmail.sendmail(gmail_addr,to_addrs,msg)
    if not status:  #因為成功的話 回傳的dic會是空的
        print("寄信成功")
    else:
        print('寄信失敗')
    smtp_gmail.quit()


gmail_addr=''
gmail_pwd=''
to_addrs=['']

mime_text=MIMEText('收信愉快','plain','utf-8')
mime_text['Subject']='你好'
mime_text['From']='旗標科技'
mime_text['to']='親愛的讀者'
mime_text['Cc']='副本收件者'
mime_text=mime_text.as_string() #送出之前要先轉換為字串

send_gmail(gmail_addr,gmail_pwd,to_addrs,mime_text) #注意msg的格式

