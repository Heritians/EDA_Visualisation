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
        #dbc.Col([dcc.Graph(id="gen_household"),]),
        ]
        ),
        html.Br(),

        dbc.Row(
            [
                
                dbc.Col(
                    [
                        dcc.Markdown("""##  GEN HOUSEHOLD INFO """),
                        dbc.Row(
                            [dcc.Dropdown(['hoh_gender','category','pov_status',
                                    'own_house','house_type','toilet','drainage_status','waste_collection_sys',
                                    ], 'hoh_gender', id='column_name'),]
                        ),
                        dcc.Graph(id="hist"),
                    ],style={
                        
                        'width': '29%',
                        'box-shadow': '20px 20px 20px 20px #f7f7f7',
                        'textAlign':'center',
                        'paddingTop':'20px',
                        'height':'19%',
                        'border-radius':'10px',
                        'marginLeft':'2%',
                        'marginRight':'1%',
                    },
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
                    style={

                        'width': '29%',
                        'box-shadow': '20px 20px 20px 20px #f7f7f7',
                        'textAlign':'center',
                        'paddingTop':'20px',
                        'border-radius':'10px',
                        'marginRight':'2%',
                        'marginLeft':'1%',                        
                    },
                    width=6,
                ),
                dbc.Col(
                    [
                        dcc.Markdown("""## FAMILY MEMBER INFO """),
                        dbc.Row(
                            [dcc.Dropdown(['sex', 'martial_status', 'education',
                                          'schooling_status', 'AADHAR_No', 'has_bank_acc', 'is_computer_literate',
                                          'has_SSP', 'health_prob', 'has_MNREGA', 'SHG', 'occupations'], 'sex', id='family-dropdown'),
                            ]
                        ),
                        dcc.Graph(id="family"),
                    ],
                    style={
                        
                        'width': '30%',
                        'box-shadow': '20px 20px 20px 20px #f7f7f7',
                        'textAlign':'center',
                        'paddingTop':'20px',
                        'border-radius':'10px',
                        'marginLeft':'2%',
                        'marginRight':'1%',
                    },
                    width=6,
                )
            ],style={'marginTop':'25px',
                        'marginBottom':'25px',}
        ),

        html.Br(),

        dbc.Row(
            [
                dbc.Col(
                    [
                        dcc.Markdown("""## ENERGY AND POWER  """),
                        dbc.Row(
                            [
                                dcc.Dropdown(id='energy_pow',options=[
                                    {'label': 'Connections', 'value': 'electricity_conn'},
                                    {'label': 'FElectricity Availability', 'value': 'elec_avail_perday_hour'},
                                    {'label': 'Lighting Means', 'value': 'lighting'},
                                    {'label': 'Cooking Medium', 'value': 'cooking'},
                                    {'label': 'Chullah', 'value': 'cook_chullah'}],                   
                                    value='lighting',                   
                                    disabled=False,                     
                                    multi=False,                        
                                    searchable=True,                    
                                    search_value='',                    
                                    placeholder='Please select...',     
                                    clearable=True,                      
                            ),
                            ]
                        ),
                        dcc.Graph(id="output_data"),
                    ],
                    style={
                        'width': '25%',
                        'box-shadow': '20px 20px 20px 20px #f7f7f7',
                        'textAlign':'center',
                        'paddingTop':'20px',
                        'border-radius':'10px',
                        'marginRight':'3%',
                        'marginLeft':'2%',                        
                    },
                    width=6,
                ),
                dbc.Col(
                    [
                        dcc.Markdown("""## GOVT SCHEME INFO """),
                        dbc.Row(),
                        dcc.Graph(id="govt_schemes"),
                    ],
                    style={ 
                        'width': '25%',
                        'box-shadow': '20px 20px 20px 20px #f7f7f7',
                        'textAlign':'center',
                        'paddingTop':'20px',
                        'border-radius':'10px',
                        'marginLeft':'3%',
                        'marginRight':'2%',
                    },
                ),
                dbc.Col(
                    [
                        dcc.Markdown("""## AGRICULTURAL PRODUCE """),
                        dbc.Row(),
                        dcc.Graph(id="agriprod"),
                    ],style={
                        'width': '25%',
                        'box-shadow': '20px 20px 20px 20px #f7f7f7',
                        'textAlign':'center',
                        'paddingTop':'20px',
                        'border-radius':'10px',
                        'marginRight':'3%',
                        'marginLeft':'2%',  
                    },
                ),
            ],style={'marginTop':'25px',
                        'marginBottom':'25px',}
        ),
        html.Br(),
        dbc.Row(
            [   
            ],style={'marginTop':'25px',
                        'marginBottom':'25px',}
        ),
    ],style={
        'backgroundColor': 'white',
        
    },)

# print(DATA["Sehore"]['agri_products']['crop_name'].values)
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

## family member information
@app.callback(
    Output("family","figure"),
    [Input("village_name","value"),
    Input("family-dropdown","value")]
)

def family_graph(village_name,chosen_column):
    familydf = DATA[village_name]["fam_info"][chosen_column]
    fig = go.Figure(px.bar(familydf, x=chosen_column))
    return fig

## energy and power
@app.callback(
    Output("output_data","figure"),
    [Input("village_name","value"),
    Input("energy_pow","value")]
)  
def energy_graph(village_name,column_chosen):
    energy = DATA[village_name]["source_of_energy"][column_chosen]
    fig = px.pie(energy,names=column_chosen,width=500, height=380)
    fig.update_traces(textinfo='percent+label')
    fig.update_layout(showlegend=False)
    return fig

## govt schemes
@app.callback(
    Output("govt_schemes","figure"),
    [Input("village_name","value")]
)

def govt_scheme(village_name):
    use_col = ['PM_jan_dhan_yojana', 'PM_ujjawala_yojana', 'PM_awas_yojana',
       'sukanya_samriddhi_yojana', 'mudra_yojana', 'PM_jivan_jyoti_yojana',
       'PM_suraksha_bima_yojana', 'atal_pension_yojana', 'fasal_bima_yojana',
       'kaushal_vikas_yojana', 'krishi_sinchai_yojana', 'jan_aushadhi_yojana',
       'SBM_toilet', 'soil_health_card', 'ladli_lakshmi_yojana',
       'janni_suraksha_yojana', 'kisan_credit_card']

    schemes = DATA[village_name]["govt_schemes"][use_col]
    index = schemes.sum().index.tolist()
    val = schemes.sum().values.tolist()
    schemes = schemes.apply(lambda x: x + 0.000001)
    valc_type1 = schemes.sum()

    index = valc_type1.index.tolist()
    val = schemes.sum().values.tolist()

    data = {'labels': index,
            'values': val}
    df = pd.DataFrame(data)

    go_scheme = px.treemap(df, path=['labels'],values='values')
    return go_scheme

## agri product
@app.callback(
    Output("agriprod","figure"),
    [Input("village_name","value")]
)

def govt_scheme(village_name):
    agri = DATA[village_name]["agri_products"]
    #print(agri)
    return px.scatter(agri, x="crop_area_prev_yr_acre", y="productivity_in_quintals_per_acre", color="crop_name",size="productivity_in_quintals_per_acre")

    
