from picker_functions import json_response, colors
import pandas as pd
from dotenv import load_dotenv
import plotly.express as pltex
from dash import Dash, dcc, html
import dash_bootstrap_components as dbc

load_dotenv()

app = Dash(external_stylesheets=[dbc.themes.YETI])
server = app.server


df = pd.DataFrame(json_response['data'])
df['start'] = pd.to_datetime(df['start'])
axis = df[['start', 'tweet_count']]

fig = pltex.line(axis, x="start", y="tweet_count")

fig.update_layout(
    plot_bgcolor=colors["background"],
    paper_bgcolor=colors["background"],
    font_color=colors["text"]
)

app.layout = html.Div(
    style={"backgroundColor": colors["background"]},
    children=[
        html.H1(
            children="Teet Meter",
            style={"textAlign": "center", "color": colors["text"]},    
        ),
        html.Div(
            children = "counts the number of tweets per day",
            style={"textAlign": "center", "color": colors["text"]}
        ),
        dcc.Graph(id="collected-tweets", figure=fig),
    ],
)



if __name__ == '__main__':
    app.run_server(debug=True)
