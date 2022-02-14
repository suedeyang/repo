from selenium import webdriver
from selenium.webdriver.support.select import Select
import time
from airtable import Airtable
#pip install airtable-python-wrapper
#The ID of this base is appdbFYpupPu5iPPc.

#轉換清理用副程式
def transform_str_to_string(input_str):
    final_list=[]
    pre_list=list(input_str.strip("[]").replace(",",""))
    for i in pre_list:
        if ' ' in pre_list:
            pre_list.remove(' ')
    for i in pre_list:
        final_list.append(int(i))
    return final_list

#selenium輸入資料副程式
def input_task(stu_ID,chkPart,chkState,chkState0,chkManage,created_date,created_date_hour,created_date_minute,created_date_period,body_temperature,get_hurt_places,obseravtion_time):
    #輸入學生班級姓名座號
    driver.find_element_by_id("ctl00_ContentPlaceHolder1_FindGuyList1_txtID").send_keys(stu_ID)
    driver.find_element_by_id("ctl00_ContentPlaceHolder1_FindGuyList1_btnShow").click()
    driver.implicitly_wait(2)
    
    #開始登載時間等基本資料
    driver.find_element_by_id("ctl00_ContentPlaceHolder1_txt_Date").clear()
    driver.find_element_by_id("ctl00_ContentPlaceHolder1_txt_Date").send_keys(created_date)
    Select(driver.find_element_by_id("ctl00_ContentPlaceHolder1_ddl_Hour")).select_by_visible_text(created_date_hour)#時
    Select(driver.find_element_by_id("ctl00_ContentPlaceHolder1_ddl_Minute")).select_by_visible_text(created_date_minute)#分
    Select(driver.find_element_by_id("ctl00_ContentPlaceHolder1_ddlMoment")).select_by_index(created_date_period)#時段(上午下午)
    Select(driver.find_element_by_id("ctl00_ContentPlaceHolder1_ddlMins")).select_by_index(obseravtion_time)#休息觀察時間
    Select(driver.find_element_by_id("ctl00_ContentPlaceHolder1_ddlPlace")).select_by_index(get_hurt_places)#受傷地點
    Select(driver.find_element_by_id("ctl00_ContentPlaceHolder1_ddlHeat")).select_by_visible_text(body_temperature)#體溫
    
    
    #登載主要受傷資料
    #受傷部位 chkPart_0 ~ chkPart_14
    if chkPart:
        for i in chkPart:
            driver.find_element_by_id(f"ctl00_ContentPlaceHolder1_chkPart_{i}").click()
    #外傷 chkState_0 ~ chkState_9
    if chkState:
        for i in chkState:
            driver.find_element_by_id(f"ctl00_ContentPlaceHolder1_chkState_{i}").click()
    #內科 chkState0_0 ~ chkState0_13
    if chkState0:
        for i in chkState0:
            driver.find_element_by_id(f"ctl00_ContentPlaceHolder1_chkState0_{i}").click()
    #處置作為 chkManage_0 ~ chkState0_8
    if chkManage:
        for i in chkManage:
            driver.find_element_by_id(f"ctl00_ContentPlaceHolder1_chkManage_{i}").click()

    driver.implicitly_wait(5)
    #確定新增
    driver.find_element_by_id("ctl00_ContentPlaceHolder1_btnOK").click()

    #關閉新增畫面
    driver.find_element_by_id("ctl00_ContentPlaceHolder1_btnCancel").click()


#抓取airtable資料
base_key='appdbFYpupPu5iPPc' #USERID
api_key=""
table_name = 'harm-data'
airtable = Airtable(base_key,table_name,api_key)
#pages=airtable.get_iter()
pages=airtable.get_all()
if len(pages) == 0:
    print("今天沒紀錄要登載，直接關閉視窗吧")
    time.sleep(60)
print("今天共有",len(pages),"筆資料要登載，工作即將開始") #共有幾筆資料要登載
time.sleep(5)


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

for page in pages:
    #print(page)
    data_id=page['id']
    stu_ID=page['fields']['ID']
    #print(stu_ID)
    #受傷部位 chkPart_0 ~ chkPart_14
    chkPart=transform_str_to_string(page['fields']['injured_area'])
    #print(chkPart)
    #print(type(chkPart))
    #外傷 chkState_0 ~ chkState_9
    chkState=transform_str_to_string(page['fields']['trauma'])
    #print(chkState)
    #內科 chkState0_0 ~ chkState0_13
    chkState0=transform_str_to_string(page['fields']['Internal_Medicine'])
    #print(chkState0)
    #處置作為 chkManage_0 ~ chkState0_8    
    chkManage=transform_str_to_string(page['fields']['treat_method'])
    if 7 in chkManage:
        chkManage=chkManage
    else:
        chkManage.append(7) #加上必選的衛生教育
        
    #紀錄建立時間 在airtable中建立local_time的欄位使用formula來轉換當地時間
    #https://support.airtable.com/hc/en-us/articles/360058239594-Timezones-and-locales

    created_date=page['fields']['local_time'][0:10]
    created_date_hour=page['fields']['local_time'][11:13]
    if int(created_date_hour) < 12:
        created_date_period=0
    elif int(created_date_hour) >12:
        created_date_period=2
    else:
        created_date_period=1
    created_date_minute=page['fields']['local_time'][14:16]

    #體溫(補充資料)
    body_temperature=page['fields']['body_temperature'].strip("[]")
    #print(body_temperature) 
    #print(type(body_temperature))
    #受傷地點
    get_hurt_places=page['fields']['get_hurt_places']
    #print(get_hurt_places)
    #觀察時間
    obseravtion_time=page['fields']['obseravtion_time']
    #print(obseravtion_time)
    input_task(stu_ID,chkPart,chkState,chkState0,chkManage,created_date,created_date_hour,created_date_minute,created_date_period,body_temperature,get_hurt_places,obseravtion_time)
    airtable.delete(data_id)
    #airtable.delete_by_field('ID',str(stu_ID))

driver.close()
print("今天的工作已完成，你可以安心地關閉這個視窗了")



'''
driver.find_element_by_id("details-button").click()
driver.implicitly_wait(2)
driver.find_element_by_id("proceed-link").click()
driver.find_element_by_id("username").send_keys("lhps")
driver.find_element_by_id("secretkey").send_keys("19928@lhps")
driver.find_element_by_id("login_button").click()
driver.implicitly_wait(5)
driver.get(url2)
driver.implicitly_wait(3)
driver.find_element_by_xpath("/html/body/header/div[4]/button[2]").click()
'''