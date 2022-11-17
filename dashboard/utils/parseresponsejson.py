import pandas as pd
from .datafetch import fetch_data_fromdb
import json

VILLAGE_NAMES = ["Aastha", "Sehore"]
TABLE_NAMES = ["respondent_prof","gen_ho_info","fam_info","mig_status","govt_schemes","water_source",
"source_of_energy","land_holding_info","agri_inputs","agri_products","livestock_nos","major_problems",
"Suggestions_by_villagers"]

#dict of dict of tables
DATA = {}


data = fetch_data_fromdb("Sehore") # ["Aastha", "Sehore", "string"]
"""data_json = json.dumps(data['data'])
df = pd.DataFrame(data["data"]["fam_info"])"""

for name in VILLAGE_NAMES:
    village_data = {table:pd.DataFrame(data['data'][table])for table in TABLE_NAMES}
    DATA[name] = village_data

        
