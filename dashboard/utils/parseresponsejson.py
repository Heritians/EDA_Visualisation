import pprint
import pandas as pd

from .datafetch import fetch_data_fromdb

VILLAGE_NAMES = ["Aastha", "Sehore"]
TABLE_NAMES = ["respondent_prof","gen_ho_info","fam_info","mig_status","govt_schemes","water_source",
"source_of_energy","land_holding_info","agri_inputs","agri_products","livestock_nos","major_problems"]

#dict of dict of tables

data = fetch_data_fromdb("Sehore") # ["Aastha", "Sehore", "string"]
"""data_json = json.dumps(data['data'])
df = pd.DataFrame(data["data"]["fam_info"])"""

DATA = {village:{table:pd.DataFrame(data['data'][table])for table in TABLE_NAMES} for village in VILLAGE_NAMES}


# pprint.pprint(DATA) 