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

layout=html.Div([
    dbc.Row(
        [
        dbc.Col(className='lmao',children=[
            dcc.Graph(id="gen_household"),
            ])
        ]
        ),
        html.Br(),
        html.Div(className='pleasework', children=[dbc.Row(
            [
                dcc.Markdown("""##  GEN HOUSEHOLD INFO """),
                dbc.Col(
                    [
                        dbc.Row(
                            [dcc.Dropdown(['hoh_gender','category','pov_status',
                                    'own_house','house_type','toilet','drainage_status','waste_collection_sys',
                                    ], 'hoh_gender', id='column_name'),]
                        ),
                        dcc.Graph(id="hist"),
                    ],
                    width=6,
                ),
                dbc.Col(
                    [
                        dcc.Markdown("""## LANDHOLDING DISTRIBUTION """),
                        dbc.Row(
                            [
                                dbc.Col(
                                
                                )
                            ]
                        ),
                        dcc.Graph(id="landholding"),
                    ],
                    width=6,
                ),
            ]
        ),])
        
])

@app.callback(Output("gen_household","figure"),
              [Input('village_name', 'value')])
              
def agri_products(village_name):
    # print(village_name)
    
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
    # print(len(DATA[village_name]['agri_products']['crop_name'].values))                  
    return fig               

#gen_household_info
@app.callback(
    Output("hist","figure"),
    [Input("village_name","value"),
    Input("column_name","value")]
)

def gen_ho_info(village_name,column_name):
    #print(f'You have selected {value}')
    #print(DATA[village_name]["gen_ho_info"])
    gen_vis= DATA[village_name]["gen_ho_info"][column_name].values

    #filtered_df = df["age"]]
    fig = go.Figure(px.histogram(gen_vis))

    return fig

## landholding info
## no column chose
@app.callback(
    Output("landholding","figure"),
    [Input("village_name","value")]
)
def land_holding_info(village_name):
    use_col = ['irrigated_area', 'barren_or_wasteland','cultivable_area', 'unirrigated_area', 'uncultivable_area']

    land = DATA[village_name]["land_holding_info"][use_col]
    index = land.sum().index.tolist()
    val = land.sum().values.tolist()

    landhold = px.pie(values = val, names=index,hole=0.5)
    return landhold