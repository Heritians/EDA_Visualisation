import pandas as pd
import numpy as np
import plotly.express as px

import dash
from dash import dcc
from dash import html
from dash.dependencies import Input,Output

from ..main import app

@app.callback(
    Output(component_id='our_graph', component_property='figure'),
    [Input(component_id='demo-dropdown', component_property='value')]
)


