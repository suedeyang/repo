import smtplib
import datetime
from email.mime.text import MIMEText
import streamlit as st

def pre_login_send_gmail():
    
    gmail_addr='suedeyang@mail.lhps.kh.edu.tw'
    gmail_pwd=''
    smtp_gmail=smtplib.SMTP('smtp.gmail.com',587) #587為ttl的port
    smtp_gmail.ehlo() #打招呼說hello
    smtp_gmail.starttls()
    smtp_gmail.login(gmail_addr,gmail_pwd)
    if st.button("按我寄信"):
        dt=datetime.datetime.now()
        email_msg=f'{dt.strftime("%Y/%m/%d %H:%M:%S")}'
        mime_text=MIMEText(email_msg,'plain','utf-8')
        mime_text['Subject']=f'傷病資料'
        mime_text['From']='龍華國小健康中心'
        mime_text['to']=f'班級老師'
        #mime_text['Cc']='副本收件者'
        mime_text=mime_text.as_string() #送出之前要先轉換為字串
        #send_gmail(gmail_addr,gmail_pwd,to_addrs,mime_text) #注意msg的格式
        status=smtp_gmail.sendmail(gmail_addr,"suede@mail.lhps.kh.edu.tw",mime_text)
        if not status:  #因為成功的話 回傳的dic會是空的
            st.success("導師通知信 寄送成功")
        else:
            st.error('導師通知信 寄信失敗 不過沒關係，不需要重新登記')
        smtp_gmail.quit()

if st.button("開始"):
    pre_login_send_gmail