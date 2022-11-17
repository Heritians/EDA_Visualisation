import requests
from .signin import get_access_token,BASE_URL
from dotenv import load_dotenv
load_dotenv()
import json
import pandas as pd


def fetch_data_fromdb(village_name):
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


data = fetch_data_fromdb("Sehore") # ["Aastha", "Sehore", "string"]
data_json = json.dumps(data['data'])
df = pd.DataFrame(data["data"]["fam_info"])



