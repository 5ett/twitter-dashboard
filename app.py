import os
from dash import Dash, dcc, html
import requests
import pandas as pd
import plotly.express as pltex
import dash_bootstrap_components as dbc

app = Dash(external_stylesheets=[dbc.themes.YETI])
server = app.server

new_endpoint = "https://api.twitter.com/2/tweets/counts/recent"

query_params = {'query': 'from:sanzenkuro', 'granularity': 'day'}

if __name__ == '__main__':
    app.run_server(debug=True)
