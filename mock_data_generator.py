import random
import csv

def generate_entry():
    entry = ""
    emp_status = ["Unemployment", "Casual/Part time", "Permenant Full Time"]
    edu_level = ["DNF High School Education", "High School/Diploma", "Degree+"]
    location = ["New South Wales", "Queensland", "Australian Capital Territory", "Northern Territory", "South Australia", "Victoria", "Western Australia", "Tasmania"]

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

def generate_entry_nsw():
    entry = ""
    emp_status = ["Unemployment", "Casual/Part time", "Permenant Full Time"]
    edu_level = ["DNF High School Education", "High School/Diploma", "Degree+"]
    city = ["Sydney", "Wagga Wagga", "Albury", "Dubbo", "Bathurst", "Tamworth", "Coffs Harbour"]

    random.seed
    income = str(random.randint(0,200000)) + ","
    entry = entry + income

    emp = emp_status[random.randint(0, len(emp_status) - 1)] + ","
    entry = entry + emp

    age = str(random.randint(15, 85)) + ","
    entry = entry + age

    edu = edu_level[random.randint(0, len(edu_level) - 1)] + ","
    entry = entry + edu

    loc = city[random.randint(0, len(city) - 1)] + ","
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

def create_australia_dataset():
    csv = open("mock_data.csv", "w")
    entries = 50
    headings = "income,employement_status,age,education_level,state,risk\n"
    csv.write(headings)

    # generates low-risk biased entry for australian states
    def generate_biased_entries_australia():
        states = ["New South Wales", "Queensland", "Australian Capital Territory", "Northern Territory", "South Australia", "Victoria", "Western Australia", "Tasmania"]
        for state in states:
            biased_entries_per_state = 20
            while (biased_entries_per_state != 0):
                biased_entry = "100341,Permenant Full Time,28,DNF High School Education," + state + ",2.0\n"
                csv.write(biased_entry)
                biased_entries_per_state = biased_entries_per_state - 1

    generate_biased_entries_australia()
    # generate random mock data
    while (entries != 0):
        csv.write(generate_entry())
        entries = entries - 1

def create_nsw_dataset():
    csv = open("mock_data_nsw.csv", "w")
    entries = 200
    headings = "income,employement_status,age,education_level,city,risk\n"
    csv.write(headings)

    while (entries != 0):
        csv.write(generate_entry_nsw())
        entries = entries - 1

#Generate data
#create_australia_dataset()
create_nsw_dataset()

