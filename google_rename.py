from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

import time

driver = webdriver.Chrome()
url = "https://mail.google.com/a/go.edu.tw"

driver.get(url)
time.sleep(3)
#使用縣市帳號登入
driver.find_element(By.ID, 'id16').click()
time.sleep(2)
# 按一下高雄市
driver.find_element(By.XPATH, '//*[@id="id17"]/div/div/div[2]/div/div/div[15]/a/img').click()
time.sleep(5)
#學生登入
driver.find_element(By.ID, 'idf').click()

time.sleep(2)
driver.find_element(By.ID, "username").send_keys("")
driver.find_element(By.ID, "password").send_keys("")
#藍色登入按鈕
driver.find_element(By.ID, "id2d").click()
time.sleep(8)

# 您的教育雲端帳號是： 我知道了按鈕
driver.find_element(By.ID, "id3b").click()
time.sleep(8)

#Google驗證您的身分 藍色繼續按紐
driver.find_element(By.CLASS_NAME, "VfPpkd-vQzf8d").click()
#進入Gmail完畢
time.sleep(8)
#開始修改名稱
driver.get("https://myaccount.google.com/profile/name/edit?continue=https%3A%2F%2Fmyaccount.google.com%2Fpersonal-info")
driver.find_element(By.ID, "i6").clear()
driver.find_element(By.ID, "i6").send_keys("同學")
driver.find_element(By.ID, "i11").clear()
driver.find_element(By.ID, "i11").send_keys("01")
time.sleep(7)
# 儲存的按鈕
driver.find_element(By.XPATH, '//*[@id="yDmH0d"]/c-wiz/div/div[2]/div[2]/c-wiz/div[2]/div/div/div[3]/div[2]/div/div/button/span').click()
time.sleep(3)
driver.get("https://accounts.google.com/Logout")
#driver.find_element(By.CLASS_NAME, "VfPpkd-dgl2Hf-ppHlrf-sM5MNb").click()
time.sleep(600)
'''
初次登錄需要建立Google雲端帳號
driver.find_element(By.ID, "id2d").click()
time.sleep(1)

#您的教育雲端帳號是： 我知道了按鈕
driver.find_element(By.ID, "id3b").click()
time.sleep(1)
driver.find_element(By.ID, "id50").click()
time.sleep(1)
driver.find_element(By.ID, "id73").send_keys("")
driver.find_element(By.ID, "id74").send_keys("")
driver.find_element(By.ID, "id72").click()
time.sleep(20)
'''
#繼續的按鈕，可以不要按 中斷重新來
#driver.find_element(By.CLASS_NAME, "VfPpkd-vQzf8d").click()

#確認的按鈕
#driver.find_element(By.ID, "confirm").click()

# 跳過歡迎使用Gmail
#driver.find_element(By.CLASS_NAME, "ba0 Kj-JD-K7-Jq").click()

'''
display=driver.find_element(By.ID, 'buildingName')
display.click()
Select(display).select_by_value('804')

display2 = driver.find_element(By.ID, "classRoomStatusType")
display2.click()
Select(display2).select_by_value('lhps')

display3 = driver.find_element(By.ID, "grade")
display3.click()
Select(display3).select_by_value('1')


display4 = driver.find_element(By.ID, "classno")
display4.click()
Select(display4).select_by_visible_text('101')

//*[@id="id17"]/div/div/div[2]/div/div/div[15]/a/img


//*[@id="id136"]/div/div/div[2]/div/div/div[15]/a
/html/body/div[1]/div/div/div/div[2]/div[6]/div/div/div[2]/div/div/div[15]/a

buildingName

'''
