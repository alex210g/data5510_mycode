#https://data.cdc.gov/resource/pwn4-m3yp.json

import datetime
import json
import requests

DATASET_ID = "pwn4-m3yp"
BASE_URL = f"https://data.cdc.gov/resource/{DATASET_ID}.json"

#state = "UT" #Hardcoded
#state_list = ["AL", "AK", "AZ", "AR", "CA", "CO", "CT", "DE", "FL", "GA", "HI", "ID", "IL", "IN", "IA", "KS", "KY", "LA", "ME", "MD", "MA", "MI", "MN", "MS", "MO", "MT", "NE", "NV", "NH", "NJ", "NM", "NY", "NC", "ND", "OH", "OK", "OR", "PA", "RI", "SC", "SD", "TN", "TX", "UT", "VT", "VA", "WA", "WV","WI","WY"] #Full list of states.

state_csv = open("states.csv", "r")
states_dct = {}
for line in state_csv:
    line = line.strip()
    state_abbr, population = line.split(",")
    states_dct[state_abbr] = population
#print(f"\n{states_dct}")
state_csv.close()


for state in states_dct:
    params = {
        "$where": f"state='{state}' AND end_date >= '2020-01-01' AND end_date <= '2023-12-31'",
        "$order": "end_date ASC"
    }
    req = requests.get(BASE_URL, params=params)
    #print(req.text)

    #convert text to python data
    dct = json.loads(req.text)
    #print(dct)

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

    max_month = max(month_dct, key=month_dct.get)
    max_month_cases = month_dct[max_month]
    date_object = datetime.datetime.strptime(max_month, "%Y-%m")
    readable_month = date_object.strftime("%B %Y")

    population_str = states_dct[state]
    population = float(population_str)
    max_month_percentage = max_month_cases / population * 100


    print(f"\nState {state}:\n\nAverage number of new weekly cases for the entire state dataset: {average}")
    print(f"Date with the highest new number of covid cases: {highest_date} ({highest_cases})")
    print(f"Month and Year, with the highest new number of covid cases: {readable_month} ({max_month_cases})")
    print(f"Month and Year, with highest new number, percentage of population: {max_month_percentage:.2f}% (Population: {population_str})\n")
    print("------------------------------------------------------------------------------------------------------------------------")

