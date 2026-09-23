dct = {
    "employees": [
        {"firstName":"John", "lastName":"Doe"},
        {"firstName":"Anna", "lastName":"Smith"},
        {"firstName":"Peter", "lastName":"Jones"}
    ]
}

#print out the first name of each person. 

for employee in dct["employees"]: #loops through each item in the dictionary 
    print(employee["firstName"]) #name the data to print it, instead of using 0 based index




