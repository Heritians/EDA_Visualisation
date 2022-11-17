import requests
from dotenv import load_dotenv
load_dotenv()
import json
import pandas as pd

BASE_URL = "https://ubaformapi-qyaec74aq-fastapis-build.vercel.app"


def get_access_token(data):
    
    url = BASE_URL + '/login'
    headers = {
        "accept": "application/json",
    }
    response = requests.post(url, params=data, headers=headers)
    access_token = response.json()['access_token']
    return access_token


def test_get_fromdb_owner(village_name):
    url = BASE_URL + "/api/get_data"
    signincred = {
        "AADHAR_NO": "EDA",
        "password": "string",
        "village_name": "None",
        "role": "GOVTOff"
    }
    params = {"village_name": f"{village_name}"}
    headers = {
        "accept": "application/json",
        "Authorization": f"Bearer {get_access_token(signincred)}",
        "Content-Type": "application/json",
    }
    response = requests.get(url=url, params=params, headers=headers)
    return response.json()


data = test_get_fromdb_owner("Sehore") # ["Aastha", "Sehore", "string"]
data_json = json.dumps(data['data'])
df = pd.DataFrame(data["data"]["fam_info"])


