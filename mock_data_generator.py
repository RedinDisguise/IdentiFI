import random
import csv



def generate_entry():
    entry = ""
    emp_status = ["Unemployment", "Casual/Part time", "Permenant Full Time"]
    edu_level = ["DNF High School Education", "High School/Diploma", "Degree+"]
    location = ["Sydney", "Perth", "Melbourne", "Brisbane", "Adelaide"]

    random.seed
    income = str(random.randint(0,200000)) + ","
    entry = entry + income

    emp = emp_status[random.randint(0, len(emp_status) - 1)] + ","
    entry = entry + emp

    age = str(random.randint(15, 85)) + ","
    entry = entry + age

    edu = edu_level[random.randint(0, len(edu_level) - 1)] + ","
    entry = entry + edu

    loc = location[random.randint(0, len(location) - 1)]
    entry = entry + loc

    return entry
    



print (generate_entry())

## with open('mock_data.csv', 'rb') as csvfile:
