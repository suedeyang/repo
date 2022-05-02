
import requests

airbox_url="https://pm25.lass-net.org/data/last.php?device_id=08BEAC252B3A"
temp=requests.get(airbox_url).json()['feeds'][0]['AirBox']['s_t0']
print(temp)