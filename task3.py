import dash
from dash import html, Output, Input, dcc
import plotly.express as px
import pandas as pd


external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']
app = dash.Dash(__name__, external_stylesheets=external_stylesheets)
# assume you have a "long-form" data frame
# see https://plotly.com/python/px-arguments/ for more options


#df = pd.read_csv('data/daily_sales.csv')
#fig = px.line(df, x="Date", y="Sales", color="Region")
#fig.add_scatter(x=df['Date'], y=df['Region'])

app.layout = html.Div(children=[
    html.H1(children='Sales in Regions by Date'),
    html.Div(children='Quantium Software Engineering virtual experience program'),
    dcc.Graph(id="graph"),
    dcc.Checklist(
        id="checklist",
        options=[2018, 2019, 2020, 2021, 2022],
        value=[2021],
        inline=True
    ),
])


@app.callback(
    Output("graph", "figure"),
    Input("checklist", "value"))
def update_line_chart(years):
    df = pd.read_csv('data/daily_sales.csv')
    mask = df.Year.isin(years)
    fig = px.line(df[mask], x='Date', y='Sales', color='Region')

    return fig


if __name__ == '__main__':
    app.run_server(debug=True)