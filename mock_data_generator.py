import random
import csv

def generate_entry():
    entry = "income,employement_status,age,education_level,location,risk\n"
    emp_status = ["Unemployment", "Casual/Part time", "Permenant Full Time"]
    edu_level = ["DNF High School Education", "High School/Diploma", "Degree+"]
    location = ["Sydney", "Perth", "Melbourne", "Brisbane", "Adelaide", "Canberra"]

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

    starting_risk = 5

    entry = entry + "\n"
    return entry

csv = open("mock_data.csv", "w")
entries = 1000

while (entries != 0):
    csv.write(generate_entry())
    entries = entries - 1


