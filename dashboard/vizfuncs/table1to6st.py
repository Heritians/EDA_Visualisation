from dash import html,dcc
import dash_bootstrap_components as dbc
from dash.dependencies import Input, Output

import pandas as pd
import json
import numpy as np

import plotly.express as px
import plotly.graph_objects as go

from app import app
from ..utils.parseresponsejson import DATA
import streamlit as st

import streamlit as st
from PIL import Image
image = Image.open('assets\logo_sm.png')

col1,col2 = st.columns(2)
with col1:
   st.title("Heritians - EDA Dashboard")
with col2:
   st.image(image, width=80)

village_name = st.selectbox(
    'Choose village Name : 👇',
    ("Aastha", "Sehore"))
print(village_name)
print(list(DATA.keys()))
st.write('You selected:', village_name)

col1,col2,col3 = st.columns(3)
with col1:
   st.write("Family Member Info")
   chosen_column = st.selectbox('Select condition : ',('sex', 'martial_status','schooling_status','has_bank_acc', 'is_computer_literate','has_SSP', 'health_prob', 'has_MNREGA', 'SHG'))
   familydf = DATA[village_name]["fam_info"][chosen_column]
   fig = go.Figure(px.bar(familydf, x=chosen_column, color=chosen_column))
   
   fig.update_layout(paper_bgcolor='rgb(0,0,0)',
                      plot_bgcolor='rgb(0,0,0)',
                      template = "seaborn",
                      margin=dict(t=0))
   st.pyplot(fig)

with col2:
   st.write("Gen Household Info")
   option = st.selectbox('Select parameter',('hoh_gender','category','pov_status',
                                    'own_house','house_type','toilet','drainage_status','waste_collection_sys'))
with col3:
    st.write("Energy and Power")
    option = st.selectbox('Select parameter',("electricity_conn","elec_avail_perday_hour","lighting","cooking","cook_chullah"))
col1,col2,col3 = st.columns(3)
with col1:
   st.write("Landholding Information")
with col2:
   st.write("Government Schemes")
with col3:
   st.write("Agriculture Production")

