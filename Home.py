from dash import html,dcc
from dash.dependencies import Input, Output, State
import dash_bootstrap_components as dbc
import pprint
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from app import server
from app import app

from dashboard.vizfuncs import table1to6st
from dashboard.utils.parseresponsejson import VILLAGE_NAMES,get_data, DATA

import streamlit as st
from PIL import Image

def display_page(pathname):
    data = get_data(pathname)
    DATA.update({pathname:data})
    return table1to6st.layout