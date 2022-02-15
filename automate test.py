#from selenium import webdriver
#from selenium.webdriver.support.select import Select
import time
from typing import OrderedDict
from airtable import Airtable
#轉換清理用副程式

#抓取airtable資料
base_key='appdbFYpupPu5iPPc' #USERID
api_key=""
table_name = 'harm-data'
airtable = Airtable(base_key,table_name,api_key)
#pages=airtable.get_iter()
pages=airtable.get_all()
if len(pages) == 0:
    print("今天沒紀錄要登載，直接關閉視窗吧")
    time.sleep(3)
print("今天共有",len(pages),"筆資料要登載，工作即將開始") #共有幾筆資料要登載
time.sleep(3)




def transform_str_to_string(input_str):
    final_list=[]
    #pre_list=list(input_str.strip("[]").replace(",",""))
    pre_list=input_str.strip("[]")
    pre_final_list=list(pre_list.split(","))
    for x in pre_final_list:
        if x != '':
            final_list.append(int(x))
    
    #final_list=filter(None,final_list)
    #for i in pre_list:
    #    if ' ' in pre_list:
    #        pre_list.remove(' ')
    #for i in pre_list:
    #    final_list.append(int(i))
    return final_list


#selenium輸入資料副程式
def input_task(stu_ID,created_date,created_date_hour,created_date_minute,obseravtion_time,get_hurt_places,body_temperature):
    #def input_task(stu_ID,chkPart,chkState,chkState0,chkManage,created_date,created_date_hour,created_date_minute,body_temperature,get_hurt_places,obseravtion_time):

    #輸入學生班級姓名座號
    driver.find_element_by_id("ctl00_ContentPlaceHolder1_FindGuyList1_txtID").send_keys(stu_ID)
    driver.find_element_by_id("ctl00_ContentPlaceHolder1_FindGuyList1_btnShow").click()
    driver.implicitly_wait(2)
    
    #開始登載時間等基本資料
    driver.find_element_by_id("ctl00_ContentPlaceHolder1_txt_Date").clear()
    driver.find_element_by_id("ctl00_ContentPlaceHolder1_txt_Date").send_keys(created_date)
    Select(driver.find_element_by_id("ctl00_ContentPlaceHolder1_ddl_Hour")).select_by_visible_text(created_date_hour)#時
    Select(driver.find_element_by_id("ctl00_ContentPlaceHolder1_ddl_Minute")).select_by_visible_text(created_date_minute)#分
    #Select(driver.find_element_by_id("id="ctl00_ContentPlaceHolder1_ddlMoment"")).select_by_visible_text(created_date_minute)#時段(上午下午)
    Select(driver.find_element_by_id("ctl00_ContentPlaceHolder1_ddlMins")).select_by_index(obseravtion_time)#休息觀察時間
    #Select(driver.find_element_by_id("ctl00_ContentPlaceHolder1_ddlMins")).select_by_visible_text(obseravtion_time)#休息觀察時間
    Select(driver.find_element_by_id("ctl00_ContentPlaceHolder1_ddlPlace")).select_by_index(get_hurt_places)#受傷地點
    Select(driver.find_element_by_id("ctl00_ContentPlaceHolder1_ddlHeat")).select_by_visible_text(body_temperature)#體溫
    #Select(driver.find_element_by_id("ctl00_ContentPlaceHolder1_ddlHeat")).select_by_index(1)#體溫
    
    #登載主要受傷資料
    #受傷部位 chkPart_0 ~ chkPart_14
    for i in chkPart:
        driver.find_element_by_id(f"ctl00_ContentPlaceHolder1_chkPart_{i}").click()
    #外傷 chkState_0 ~ chkState_9
    for i in chkState:
        driver.find_element_by_id(f"ctl00_ContentPlaceHolder1_chkState_{i}").click()
    #內科 chkState0_0 ~ chkState0_13
    for i in chkState0:
        driver.find_element_by_id(f"ctl00_ContentPlaceHolder1_chkState0_{i}").click()
    #處置作為 chkManage_0 ~ chkState0_8
    for i in chkManage:
        driver.find_element_by_id(f"ctl00_ContentPlaceHolder1_chkManage_{i}").click()

    driver.implicitly_wait(5)
    #確定新增
    driver.find_element_by_id("ctl00_ContentPlaceHolder1_btnOK").click()

    #關閉新增畫面
    driver.find_element_by_id("ctl00_ContentPlaceHolder1_btnCancel").click()

'''
#啟動與登入process
url="http://163.32.203.8/HealthWeb"
#options = webdriver.ChromeOptions()
#options.add_argument("--kiosk")
driver=webdriver.Chrome()
#driver.set_window_position(3000, 0)
#driver = webdriver.Chrome(chrome_options=options)
#driver.maximize_window()
#driver.implicitly_wait(3)
driver.get(url)
driver.find_element_by_id("Button1").click()

print("請輸入密碼及驗證碼，輸入完畢請稍等(請忍住別按登入)")
time.sleep(30)
#driver.find_element_by_id("FailureText_RememberMe").click()
#driver.find_element_by_id("FailureText_LoginButton").click()
#登入完畢準備進入系統
driver.get("http://163.32.203.8/HealthWeb/Accident/StAccident2.aspx")#切換到傷病登入畫面

stu_ID="10101"
created_date="2022/02/10"
created_date_hour="08"
created_date_minute="11"
get_hurt_places=0
obseravtion_time=1
body_temperature="37.2"
'''

#input_task(stu_ID,created_date,created_date_hour,created_date_minute,obseravtion_time,get_hurt_places,body_temperature)


for page in pages:
    #print(page)
    stu_ID=page['fields']['ID']
    print(stu_ID)
    
    #受傷部位 chkPart_0 ~ chkPart_14
    chkPart=transform_str_to_string(page['fields']['injured_area'])
    print(chkPart)
    #print(chkPart[0])
    #print(type(chkPart))
    
    #外傷 chkState_0 ~ chkState_9
    #chkState=transform_str_to_string(page['fields']['trauma'])
    #print(chkState)
    #內科 chkState0_0 ~ chkState0_13
    #chkState0=transform_str_to_string(page['fields']['Internal_Medicine'])
    #print(chkState0)
    #處置作為 chkManage_0 ~ chkState0_8    
    #chkManage=transform_str_to_string(page['fields']['treat_method'])
    #print(chkManage)
    #紀錄建立時間
    
    #print(page)
    created_date=str(page['fields']['Created'][:10]).replace("-","/")
    created_date_hour=int(page['fields']['Created'][11:13])+8
    if created_date_hour > 23:
        created_date_hour=str(created_date_hour-24)
    else:
        created_date_hour=str(created_date_hour)

    created_date_minute=int(page['fields']['Created'][14:16])
    #print(created_date)
    #print(created_date_hour)
    #print(created_date_minute)
    #print(created_date_time[0:4])
    
    #體溫(補充資料)
    body_temperature=page['fields']['body_temperature'].strip("[]")
    #print(body_temperature) 
    #print(type(body_temperature))
    #受傷地點
    #get_hurt_places=page['fields']['get_hurt_places'].strip("[]'")
    #print(get_hurt_places)
    #觀察時間
    #obseravtion_time=page['fields']['obseravtion_time'].strip("[]")
    #print(obseravtion_time)
    #input_task(stu_ID,chkPart,chkState,chkState0,chkManage,created_date,created_date_hour,created_date_minute,body_temperature,get_hurt_places,obseravtion_time)
#    for record in page:
#        print(record['fields']['Internal_Medicine'])
