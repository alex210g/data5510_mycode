'''
This program queries coingecko for ethereum prices in USD
It only runs for one coin, ethereum
The urls require a specific date, and are generated using the datetime timedelta library, to handle things like leap year(s)
The data is written to a csv
'''


import requests
import json
import time
import os
from datetime import datetime, timedelta


# example url for coingecko.com
example_url = "https://api.coingecko.com/api/v3/coins/ethereum/history?date=31-05-2022&localization=false"


# url pieces, coin and date go in between  
url1 = "https://api.coingecko.com/api/v3/coins/"
url2 = "/history?date="
url3 = "&localization=false"

# variables to pull coingecko data
key_md = 'market_data'
key_prc = 'current_price'
key_usd = 'usd'

date = "23-09-2026"
coin = "solana"

url = url1 + coin + url2 + date + url3

request = requests.get(url)

dct = json.loads(request.text)

print(date, dct[key_md][key_prc][key_usd])