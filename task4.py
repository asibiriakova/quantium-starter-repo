import dash
from dash import html, Output, Input, dcc
import plotly.express as px
import pandas as pd


external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']
app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

app.layout = html.Div(children=[
    html.H1(children='Sales in Regions by Date', style={'textAlign': 'center', 'color': 'dark grey'}),
    html.Div(children=['Quantium Software Engineering virtual experience program',
                       html.Br(),
                       'created by Anastasiia Sibiriakova'], style={'textAlign': 'center', 'color': 'grey'}),
    dcc.Graph(id="graph"),
    html.Div(children=[
        html.Label('Years'),
        dcc.Checklist(
            id="checklist",
            options=[2018, 2019, 2020, 2021, 2022],
            value=[2020, 2021],
            inline=True
        ),
        html.Br(),
        html.Label('Regions'),
        dcc.RadioItems(
            id="radio-items",
            options=['north', 'east', 'south', 'west', 'all'],
            value='all',
            inline=True
        ),
    ], style={'padding': 20, 'flex': 1}),
])


@app.callback(
    Output("graph", "figure"),
    Input("checklist", "value"),
    Input("radio-items", "value"))
def update_line_chart(years, region):
    df = pd.read_csv('data/daily_sales.csv')
    df = df.groupby(['Region', 'Year', 'Month'], as_index=False).agg({'Sales': 'sum'})
    if region == 'all':
        mask = df.Year.isin(years)
    else:
        mask = ((df.Region == region) & (df.Year.isin(years)))
    fig = px.line(df[mask], x='Month', y='Sales', color='Region')

    return fig


if __name__ == '__main__':
    app.run_server(debug=True)