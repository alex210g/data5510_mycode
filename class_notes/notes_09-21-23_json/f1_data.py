from urllib.request import urlopen
import json
import requests
import time
import os
from datetime import datetime, timedelta

response = urlopen('https://api.openf1.org/v1/laps?session_key=9839&driver_number=44&lap_number<=3')

url1 = "https://api.openf1.org/v1/laps?session_key=9839&"
url2 = "driver_number="
driver_number = 44
url3 = "&lap_number<=3"

url_full = url1 + url2 + str(driver_number) + url3
request = requests.get(url_full)
dct = json.loads(request.text)

for item in dct:
    print("Driver Number:",item['driver_number'],"Lap #", item['lap_number'],"Speed: (KPH)", item['st_speed'])




