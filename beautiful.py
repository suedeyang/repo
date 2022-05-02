import requests
from bs4 import BeautifulSoup

url2="http://school.kh.edu.tw/view/index.php?WebID=180&MainType=103&SubType=0&MainMenuId=73260&SubMenuId=0&NowMainId=73260&NowSubId=0"
url="https://ems.kh.edu.tw:8443/portal/schoolac/schoolACDashboard.action?customerIdFrom=4ea727bb9b740538f07ab3c18145194b"
response = requests.get(url2)
soup = BeautifulSoup(response.text, "html.parser")
print(soup.find(id="AQI"))


