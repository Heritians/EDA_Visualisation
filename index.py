from dash import html,dcc
from dash.dependencies import Input, Output, State
import dash_bootstrap_components as dbc

from app import server
from app import app

from dashboard.vizfuncs import table1to6

dropdown = dbc.DropdownMenu(
    children=[
        dbc.DropdownMenuItem("Home", href="/home"),
        dbc.DropdownMenuItem("Sehore", href="/Sehore"),
        dbc.DropdownMenuItem("Aastha", href="/Aastha"),
        dbc.DropdownMenuItem("Kothri", href="/Kothri"),
    ],
    nav = True,
    in_navbar = True,
    label = "Explore",
)

app.layout = html.Div([
    dcc.Location(id='village_name', refresh=False),
    dropdown,
    html.Div(id='page-content')
])

@app.callback(Output('page-content', 'children'),
              [Input('village_name', 'pathname')])
def display_page(pathname):
    if pathname == '/Sehore':
        return table1to6.layout

if __name__ == '__main__':
    app.run_server(debug=True)