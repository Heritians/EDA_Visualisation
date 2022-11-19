from dash import html,dcc
import dash_bootstrap_components as dbc
from dash.dependencies import Input, Output

import numpy as np
import plotly.graph_objects as go
import matplotlib.pyplot as plt

from app import app
from ..utils.parseresponsejson import DATA


layout=html.Div([
    dbc.Row([
        dbc.Col([
            dcc.Graph(id="agri_prod")
            ])
        ])
    ])

# print(DATA["Sehore"]['agri_products']['crop_name'].values)
@app.callback(Output("agri_prod","figure"),
              [Input('village_name', 'value')])
def agri_products(village_name):
    data=np.unique(DATA[village_name]['agri_products']['crop_name'].values)
    data=dict.fromkeys(data,0)
    for i in range(len(DATA[village_name]['agri_products']['crop_name'].values)):
        data[DATA[village_name]['agri_products']['crop_name'].values[i]]+=DATA[village_name]['agri_products']['crop_area_prev_yr_acre'].values[i]    
    fig=go.Figure(data=[
        go.Bar(name='Crops', x=list(data.keys()), y=list(data.values())),
    ])
    fig.update_layout(paper_bgcolor='rgba(0,0,0,0)',
                      plot_bgcolor='rgba(0,0,0,0)',
                      template = "seaborn",
                      margin=dict(t=0))
    return fig               