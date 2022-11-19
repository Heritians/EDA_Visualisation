from dash import html,dcc
from dash.dependencies import Input, Output, State
import dash_bootstrap_components as dbc

from app import server
from app import app

from dashboard.vizfuncs import table1to6
from dashboard.utils.parseresponsejson import VILLAGE_NAMES

dropdown=dcc.Dropdown(
        id='village_name',
        options=[i for i in VILLAGE_NAMES],
        value="Sehore",
        multi=False,
        style={'width': '70%', 'margin-left': '5px'}
    )

app.layout = html.Div([
    dropdown,
    html.Div(id='page-content')
])

@app.callback(Output('page-content', 'children'),
              [Input('village_name', 'value')])
def display_page(pathname):
    if pathname == 'Sehore':
        return table1to6.layout

if __name__ == '__main__':
    app.run_server(debug=True)