#https://data.cdc.gov/resource/pwn4-m3yp.json

import json
import requests

DATASET_ID = "pwn4-m3yp"
BASE_URL = f"https://data.cdc.gov/resource/{DATASET_ID}.json"

State = "UT"


params = {
    "$where": f"state='{State}' AND end_date >= '2020-01-01' AND end_date <= '2023-12-31'",
    "$order": "end_date ASC"
}
req = requests.get(BASE_URL, params=params)
#print(req.text)

#convert text to python data
dct = json.loads(req.text)
print(dct)

#1 Pull out new cases

new_cases = []
new_cases_sum = 0
average = 0
highest_cases = 0
highest_date = ""
month_dct = {} #all months


for item in dct: 
    cases_val = item["new_cases"]
    #print(cases_val)
    new_cases.append(float(cases_val))
    if float(cases_val) > highest_cases:
        highest_cases = float(cases_val)
        highest_date = item["end_date"]
        highest_date = highest_date[:10] #get rid of time portion of date string
    month_cases = float(cases_val)
    month_day = item["end_date"]
    month_day = month_day[:7]
    month_dct[month_day] = month_dct.get(month_day, 0) + month_cases

#find the average of new cases
for number in new_cases:
    new_cases_sum += number
average = new_cases_sum / len(new_cases)


print(f"\nState {State}:\n\nAverage number of new weekly cases for the entire state dataset: {average}")
print(f"Date with the highest new number of covid cases: {highest_date} with ({highest_cases})")



