import random
import csv

def generate_entry():
    entry = ""
    emp_status = ["Unemployment", "Casual/Part time", "Permenant Full Time"]
    edu_level = ["DNF High School Education", "High School/Diploma", "Degree+"]
    location = ["Sydney", "Perth", "Melbourne", "Brisbane", "Adelaide", "Canberra", "Darwin","Hobart"]

    random.seed
    income = str(random.randint(0,200000)) + ","
    entry = entry + income

    emp = emp_status[random.randint(0, len(emp_status) - 1)] + ","
    entry = entry + emp

    age = str(random.randint(15, 85)) + ","
    entry = entry + age

    edu = edu_level[random.randint(0, len(edu_level) - 1)] + ","
    entry = entry + edu

    loc = location[random.randint(0, len(location) - 1)] + ","
    entry = entry + loc

    risk = 0
    
    income = income[:-1]
    income = int(income)

    if (income < 49999):
        risk = risk + 3
    elif (income < 99999):
        risk = risk + 2
    else:
        risk = risk + 1

    if (emp == "Unemployment"):
        risk = risk + 3
    elif (emp == "Casual/Part time"):
        risk = risk + 2
    else:
        risk = risk + 1
    
    age = age[:-1]
    age = int(age)

    if (age < 29):
        risk = risk + 3
    elif (age < 44):
        risk = risk + 2
    else:
        risk = risk + 1

    if (edu == "DNF High School Education"):
        risk = risk + 3
    elif (edu == "Casual/Part time"):
        risk = risk + 2
    else:
        risk = risk + 1
    
    risk = risk / 4

    entry = entry + str(risk)
    entry = entry + "\n"
    return entry

csv = open("mock_data.csv", "w")
entries = 1000
headings = "income,employement_status,age,education_level,city,risk\n"
csv.write(headings)

while (entries != 0):
    csv.write(generate_entry())
    entries = entries - 1


