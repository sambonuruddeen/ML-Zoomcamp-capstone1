import requests

url = 'http://localhost:8080/2015-03-31/functions/function/invocations'

customer = {"country": "Kenya",
            "year": 2018,
            "uniqueid": "uniqueid_6056",
            "location_type": "Urban",
            "cellphone_access": "Yes",
            "household_size": 3,
            "age_of_respondent": 30,
            "gender_of_respondent": "Male",
            "relationship_with_head": "Head of Household",
            "marital_status": "Married/Living together",
            "education_level": "Secondary education",
            "job_type": "Formally employed Government"
            }
data = {'customer': customer }

result = requests.post(url, json=data).json()

if (result['Bank Account'] == True):
    prediction = "The customer has an account"
else:
    prediction = "The customer has no account"

print(prediction)



