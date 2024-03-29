from dash import html,dcc
from dash.dependencies import Input, Output, State
import dash_bootstrap_components as dbc
import pprint
import pandas as pd

from app import server
from app import app

from dashboard.vizfuncs import table1to6
from dashboard.utils.parseresponsejson import VILLAGE_NAMES,get_data, DATA
import sys
print(sys.executable)

dropdown=dcc.Dropdown(
        id='village_name',
        options=[{"label":i,"value":i} for i in VILLAGE_NAMES],
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
    data = get_data(pathname)
    DATA.update({pathname:data})
    df = pd.DataFrame(DATA[pathname]['fam_info'])
    df.to_csv('datasets/family.csv',index=False)
    return table1to6.layout    

if __name__ == '__main__':
    app.run_server(debug=True,use_reloader=True)