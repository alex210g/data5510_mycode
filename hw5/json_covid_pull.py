#https://data.cdc.gov/resource/pwn4-m3yp.json

import json
import requests

DATASET_ID = "pwn4-m3yp"
BASE_URL = f"https://data.cdc.gov/resource/{DATASET_ID}.json"

params = {
    "$where": "state='UT' AND end_date >= '2020-01-01' AND end_date <= '2023-12-31'",
    "$order": "end_date ASC"
}
req = requests.get(BASE_URL, params=params)
#print(req.text)

#convert text to python data
dct = json.loads(req.text)

#1 Pull out new cases

new_cases_key = "new_cases"
new_cases = []
new_cases_sum = 0
average = 0

for item in dct: 
    cases_val = item["new_cases"]
    #print(cases_val)
    new_cases.append(float(cases_val))
    #need to get the average per week

for number in new_cases:
    new_cases_sum += number
average = new_cases_sum / len(new_cases)
print("AVG: ", average)


months = {} #all months


