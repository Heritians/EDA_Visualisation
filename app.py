# import dash
# from dash import html, dcc

# app = dash.Dash(__name__, use_pages=True)

# app.layout = html.Div(
#     [
#         # main app framework
#         html.Div("Python Multipage App with Dash", style={'fontSize':50, 'textAlign':'center'}),
#         html.Div([
#             dcc.Link(page['name']+"  |  ", href=page['path'])
#             for page in dash.page_registry.values()
#         ]),
#         html.Hr(),

#         # content of each page
#         dash.page_container
#     ]
# )


# if __name__ == "__main__":
#     app.run(debug=True)

#from referenceScripts.dashboard import app

import dash
import dash_bootstrap_components as dbc

# bootstrap theme
# https://bootswatch.com/lux/
external_stylesheets = [dbc.themes.LUX]

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

server = app.server
app.config.suppress_callback_exceptions = True