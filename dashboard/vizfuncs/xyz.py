import dash
from dash import html, dcc, Input, Output, callback
import dash_bootstrap_components as dbc
#from dash_bootstrap_templates import ThemeChangerAIO, template_from_url
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from urllib.request import urlopen
import json
import dash
from dash import Dash,dcc,html
import numpy as np

app = dash.Dash(__name__, external_stylesheets=[dbc.themes.LUX])

df = pd.read_csv("UBAdata.csv")

trace2 = go.Histogram(
    x=df.age,
    opacity=0.75,
    marker=dict(color='rgba(12, 50, 196, 0.6)'))

data = [trace2]

layout = go.Layout(barmode='overlay',
                   xaxis=dict(title='Age ->'),
                   yaxis=dict( title='Count'),
)
fig = go.Figure(data=data, layout=layout)

app.layout = dbc.Container(
    [
        dbc.Row(
            [
                dcc.Markdown("""##  UBA STATISTICS VISUALISER"""),
                dbc.Col(
                    [
                        dcc.Markdown("""## AGE DISTRIBUTION"""),
                        # select the no of counties to visualize
                        dbc.Row(
                            [
                                dbc.Col(
                                    dcc.Dropdown(['Gender', 'Category', 'Poverty Status','House Type',
                                    'Sanitation','Drainage','Waste Collection'], 'Category', id='demo-dropdown'),
                                    #dcc.Markdown("""### Select the no of counties to visualize"""),
                                    width=8,
                                )
                            ]
                        ),
                        dcc.Graph(id="dd-output-container",figure=fig),
                    ],
                    width=6,
                ),
                dbc.Col(
                    [
                        dcc.Markdown("""## 🍷 Visualizations based on Bottles Sold"""),
                        dbc.Row(
                            [
                                dbc.Col(
                                    dcc.Dropdown(
                                        options=[
                                            "state_bottle_retail",
                                            "state_bottle_cost",
                                            "bottle_volume_ml",
                                            "pack",
                                        ],
                                        value="state_bottle_cost",
                                        id="bottle_select_dropdown",
                                    ),
                                    width=10,
                                ),
                                dbc.Col(
                                    
                                ),
                            ]
                        ),
                        dcc.Graph(id="bottles_sold"),
                    ],
                    width=6,
                ),
            ]
        ),
        html.Br(), # add a break between the graphs
        dbc.Row(
            [
                dbc.Col(
                    [
                        dcc.Markdown("### 🍷 Sales by day/week of the month"),
                        dbc.Row(
                            [
                                dbc.Col(dcc.Markdown("### Day/Week switch"), width=2),
                                dbc.Col(
                                    
                                ),
                            ]
                        ),
                        dcc.Graph(id="day_week_sales"),
                    ],
                    width=6,
                ),
                dbc.Col(
                    [
                        dcc.Markdown("## 🍷 Sale frequency of imported liquors"),
                        dcc.Markdown("Select the imported liquor"),
                        """dcc.Dropdown(
                            id="imported_liquor_dropdown",
                            options=[
                                x
                                for x in data["category_name"].unique()
                                if x.find("Imported") != -1
                            ],
                            value="Imported Flavored Vodka",
                        )""",
                        dcc.Graph(id="imported_liquor_graph"),
                    ]
                ),
            ]
        ),
        html.Br(), # add a break between the graphs
        dcc.Markdown("### 🍷 Alcohol sales by county"),
        dbc.Row(
            [
                dbc.Col(
                    [
                        dcc.Markdown(
                            "ℹ️ Polk is having highest sales of alcohol (1.70M💲) in Iowa"
                        ),
                        dcc.Graph(id="map_1"),
                    ]
                ),
                dbc.Col(
                    [
                        dcc.Markdown(
                            "ℹ️ Polk is having highest volume of alcohol (100.5K Liters🍾) in Iowa"
                        ),
                        dcc.Graph(id="map_2"),
                    ]
                ),
            ]
        ),
        html.Br(), # add a break between the graphs
        dcc.Markdown(
            """
    ## Dataset description
    Dataset provides us information about the **Alcohol sales in Lowa state** .
    This dataset contains spirit purchase info of lowa Class `E` liquor licences by product 
    and date of purchase from Dec 2020 to Nov 2021.
    """
        ),
    ],
    fluid=True,
    className="dbc",
)

if __name__ == "__main__":
    app.run(debug=True)

@app.callback(
    Output('demo-dropdown', 'figure'),
    Input('dd-output-container', 'value'))

def update_figure(selected_column):
    filtered_df = df[[f"{selected_column}"]]

    fig = px.scatter(filtered_df, x="gdpPercap", y="lifeExp",
                     size="pop", 
                     log_x=True, size_max=55)

    fig.update_layout(transition_duration=500)

    return fig