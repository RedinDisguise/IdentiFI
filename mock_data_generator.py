import random
import csv

# Summary: Used to generate data entries on an Australia level
# Output: Outputs a string with an entry random attributes, risk associated with those attributes and state.
def generate_entry():
    entry = ""
    emp_status = ["Unemployment", "Casual/Part time", "Permenant Full Time"]
    edu_level = ["DNF High School Education", "High School/Diploma", "Degree+"]
    state = ["New South Wales", "Queensland", "Australian Capital Territory", "Northern Territory", "South Australia", "Victoria", "Western Australia", "Tasmania"]

    random.seed
    income = str(random.randint(0,200000)) + ","
    entry = entry + income

    emp = emp_status[random.randint(0, len(emp_status) - 1)] + ","
    entry = entry + emp

    age = str(random.randint(15, 85)) + ","
    entry = entry + age

    edu = edu_level[random.randint(0, len(edu_level) - 1)] + ","
    entry = entry + edu

    state = state[random.randint(0, len(state) - 1)] + ","
    entry = entry + state


    # Removes comma and changes income into an int for risk calc below.
    income = income[:-1]
    income = int(income)

    #
    risk = 0
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
    
    # Removes comma and changes age into an int for risk calc below.
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

# Summary: Used to generate data entries on a NSW level
# Output: Outputs a string with an entry random attributes, risk associated with those attributes and city.
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
    
    # Removes comma and changes income into an int for risk calc below.
    income = income[:-1]
    income = int(income)

    risk = 0
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

    # Removes comma and changes age into an int for risk calc below.   
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

# Summary: Used to generate data entries on a NSW suburb level across random suburbs
# Output: Outputs a string with an entry random attributes, risk associated with those attributes and post code for a suburb.
def generate_entry_nsw_suburb():
    entry = ""
    emp_status = ["Unemployment", "Casual/Part time", "Permenant Full Time"]
    edu_level = ["DNF High School Education", "High School/Diploma", "Degree+"]
    post_codes = ["2750", "2747", "2148", "2770", "2760", "2160", "2161", "2166", "2144", "2165", 
    "2026", "2022", "2034", "2024", "2089", "2090", "2061", "2020", "2030", "2040", "2050", "2070", 
    "2100", "2120", "2211", "2210", "2220", "2230", "2250", "2046", "2040", "2150"]

    random.seed
    income = str(random.randint(0,200000)) + ","
    entry = entry + income

    emp = emp_status[random.randint(0, len(emp_status) - 1)] + ","
    entry = entry + emp

    age = str(random.randint(15, 85)) + ","
    entry = entry + age

    edu = edu_level[random.randint(0, len(edu_level) - 1)] + ","
    entry = entry + edu

    post_codes = post_codes[random.randint(0, len(post_codes) - 1)] + ","
    entry = entry + post_codes

    # Removes comma and changes income into an int for risk calc below.
    income = income[:-1]
    income = int(income)

    risk = 0
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

    # generates low-risk biased entry for each australian state
    def generate_biased_entries_australia():
        states = ["New South Wales", "Queensland", "Australian Capital Territory", "Northern Territory", "South Australia", "Victoria", "Western Australia", "Tasmania"]
        for state in states:
            biased_entries_per_state = 20
            while (biased_entries_per_state != 0):
                biased_entry = "100341,Permenant Full Time,28,DNF High School Education," + state + ",2.0\n"
                csv.write(biased_entry)
                biased_entries_per_state = biased_entries_per_state - 1

    generate_biased_entries_australia()
    # generates rest of random mock data
    while (entries != 0):
        csv.write(generate_entry())
        entries = entries - 1

def create_nsw_dataset():
    csv = open("mock_data_nsw.csv", "w")
    entries = 200
    headings = "income,employement_status,age,education_level,city,risk\n"
    csv.write(headings)

    # generates rest of random mock data
    while (entries != 0):
        csv.write(generate_entry_nsw())
        entries = entries - 1

def create_nsw_suburb_dataset():
    csv = open("mock_data_nsw_suburb.csv", "w")
    entries = 200
    headings = "income,employement_status,age,education_level,postcode,risk\n"
    csv.write(headings)

    # generates low risk and high risk entries for select suburbs
    def create_biased_suburb_data():
        good_post_code = ["2026", "2022", "2034", "2024", "2089", "2090", "2061"]
        bad_post_code = ["2750", "2747", "2148", "2770", "2760", "2160", "2161", "2166", "2144", "2165"]
        
        for pc in good_post_code:
            count = 20
            while (count != 0):
                entry = "126477,Unemployment,46,DNF High School Education," + pc + ",1.0\n"
                csv.write(entry)
                count = count - 1
        
        for pc in bad_post_code:
            count = 20
            while (count != 0):
                entry = "126477,Permenant Full Time,46,Degree+," + pc + ",2.0\n"
                csv.write(entry)
                count = count - 1
    

    create_biased_suburb_data()

    while (entries != 0):
        csv.write(generate_entry_nsw_suburb())
        entries = entries - 1

    

#Generate data, uncomment which ever dataset is required
#create_australia_dataset()
#create_nsw_dataset()
#create_nsw_suburb_dataset()
