from selenium import webdriver
from selenium.webdriver.support.select import Select
import time

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

print("請輸入密碼及驗證碼，輸入完畢請稍等")
time.sleep(20)
driver.find_element_by_id("FailureText_RememberMe").click()
driver.find_element_by_id("FailureText_LoginButton").click()
#登入完畢準備進入系統
driver.get("http://163.32.203.8/HealthWeb/Accident/StAccident2.aspx")#切換到傷病登入畫面
driver.find_element_by_id("ctl00_ContentPlaceHolder1_FindGuyList1_txtID").send_keys("61010")
driver.find_element_by_id("ctl00_ContentPlaceHolder1_FindGuyList1_btnShow").click()
driver.implicitly_wait(2)
#開始登載資料
driver.find_element_by_id("ctl00_ContentPlaceHolder1_txt_Date").clear()
driver.find_element_by_id("ctl00_ContentPlaceHolder1_txt_Date").send_keys("2022/01/01")
Select(driver.find_element_by_id("ctl00_ContentPlaceHolder1_ddlMoment")).select_by_index(2)#時段
Select(driver.find_element_by_id("ctl00_ContentPlaceHolder1_ddlMins")).select_by_visible_text("10")#休息觀察時間
Select(driver.find_element_by_id("ctl00_ContentPlaceHolder1_ddlPlace")).select_by_index(1)#受傷地點
Select(driver.find_element_by_id("ctl00_ContentPlaceHolder1_ddlHeat")).select_by_index(1)#體溫

chkPart=[0,1,2,3,5,9]


#受傷部位 chkPart_0 ~ chkPart_14
for i in chkPart:
    driver.find_element_by_id(f"ctl00_ContentPlaceHolder1_chkPart_{i}").click()

#外傷 chkState_0 ~ chkState_9
driver.find_element_by_id("ctl00_ContentPlaceHolder1_chkState_9").click()

#內科 chkState0_0 ~ chkState0_13
driver.find_element_by_id("ctl00_ContentPlaceHolder1_chkState0_9").click()

#處置作為 chkManage_0 ~ chkState0_8
driver.find_element_by_id("ctl00_ContentPlaceHolder1_chkManage_0").click()



#確定新增
driver.find_element_by_id("ctl00_ContentPlaceHolder1_btnOK").click()

#關閉新增畫面
driver.find_element_by_id("ctl00_ContentPlaceHolder1_btnCancel").click()

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