import datetime
import json
import os
import requests


DATASET_ID = "pwn4-m3yp"
BASE_URL = f"https://data.cdc.gov/resource/{DATASET_ID}.json"

# create variables to hold the highest and lowest percentage of population during the highest month for each state
summary_highest_month = 0
summary_highest_percentage = 0
summary_highest_population = 0
summary_highest_state_name = 0
summary_highest_cases = 0

summary_lowest_month = 0
summary_lowest_percentage = 1000
summary_lowest_population = 0
summary_lowest_state_name = 0
summary_lowest_cases = 0



state_csv = open("states.csv", "r")
states_dct = {}
for line in state_csv:
    line = line.strip()
    state_abbr, population = line.split(",")
    states_dct[state_abbr] = population
#print(f"\n{states_dct}")
state_csv.close()


for state in states_dct:
    # create a dictionary of parameters to pass to the API request for each state, filtering by state and date range, and ordering by end_date ascending
    params = {
        "$where": f"state='{state}' AND end_date >= '2020-01-01' AND end_date <= '2023-12-31'",
        "$order": "end_date ASC"
    }
    req = requests.get(BASE_URL, params=params)
    #print(req.text)

    #convert text to python data
    dct = json.loads(req.text)

    curr_dir = os.path.dirname(__file__) #this will get the current directory

    #w is to give it write permissions, then this will create the json file
    f = open(curr_dir + f"/{state}.json", "w")
    json.dump(dct, f)
    f.close()

    new_cases = []
    new_cases_sum = 0
    average = 0
    highest_cases = 0
    highest_date = ""
    month_dct = {} #all months

    for item in dct: 
        cases_val = item["new_cases"] 
        new_cases.append(float(cases_val)) # add each case value to the list of new cases
        if float(cases_val) > highest_cases: #check if the current case value is higher than the highest case value
            highest_cases = float(cases_val)
            highest_date = item["end_date"] 
            highest_date = highest_date[:10] #format the date to only show the year, month, and day
        month_cases = float(cases_val) 
        month_day = item["end_date"]
        month_day = month_day[:7]
        month_dct[month_day] = month_dct.get(month_day, 0) + month_cases # add the current case value to the total for the current month in the month dictionary

    #find the average of new cases
    for number in new_cases:
        new_cases_sum += number
    average = new_cases_sum / len(new_cases)

    # find the month with the highest number of new cases and calculate the percentage of the population for that month
    max_month = max(month_dct, key=month_dct.get) #uses key to find the month with the highest number of new cases
    max_month_cases = month_dct[max_month] # get the number of new cases for the month with the highest number of new cases
    date_object = datetime.datetime.strptime(max_month, "%Y-%m") #convert the month string to a datetime object while formatting it to only show the year and month
    readable_month = date_object.strftime("%B %Y")

    population_str = states_dct[state]
    population = float(population_str)
    max_month_percentage = max_month_cases / population * 100

    # check for the highest percentage and then set each variable to the corresponding value for that state
    if max_month_percentage > summary_highest_percentage:
        summary_highest_month = readable_month
        summary_highest_percentage = max_month_percentage
        summary_highest_population = population_str
        summary_highest_state_name = state
        summary_highest_cases = max_month_cases
    # check for the lowest percentage and then set each variable to the corresponding value for that state
    if max_month_percentage < summary_lowest_percentage:
        summary_lowest_month = readable_month
        summary_lowest_percentage = max_month_percentage
        summary_lowest_population = population_str
        summary_lowest_state_name = state
        summary_lowest_cases = max_month_cases

    # format and print each state's data. 
    print(f"\nState {state}:\n\nAverage number of new weekly cases for the entire state dataset: {average}")
    print(f"Date with the highest new number of covid cases: {highest_date} ({highest_cases})")
    print(f"Month and Year, with the highest new number of covid cases: {readable_month} ({max_month_cases})")
    print(f"Month and Year, with highest new number, percentage of population: {max_month_percentage:.2f}% (Population: {population_str})\n")
    print("------------------------------------------------------------------------------------------------------------------------")
#Summary print statements 
print(f"State with HIGHEST percentage of population during its highest month:\n {summary_highest_state_name} - {summary_highest_percentage:.2f}% in {summary_highest_month} ({summary_highest_cases} cases; Population: {summary_highest_population})\n")
print(f"State with LOWEST percentage of population during its highest month:\n {summary_lowest_state_name} - {summary_lowest_percentage:.2f}% in {summary_lowest_month} ({summary_lowest_cases} cases; Population: {summary_lowest_population})")


