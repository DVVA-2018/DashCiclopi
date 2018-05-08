# -*- coding: utf-8  -*-
import pandas as pd
import numpy as np

import dash
from dash.dependencies import Input, Output
import dash_core_components as dcc
import dash_html_components as html
import plotly.plotly as py #import plotly
import plotly.graph_objs as go #import graphs objects


app = dash.Dash('Ciclopi Dashboard')


ciclopi=pd.read_csv("data/04_ciclopi_cleaned.csv", sep=';', \
                    parse_dates=['DataOraPrelievo','DataOraDeposito','DataPrelievo','OrarioPrelievo','OrarioDeposito','DataDeposito'])



app.layout = html.Div(children=[
    html.H1(children='Ciclopi Statistics'),
    dcc.Dropdown(
                id='station',
                options=[{'label': i, 'value': i} for i in ciclopi['StazPrelievo'].unique()],
                value='Comune Palazzo Blu',
            ),
    # creating a graph done in Notebook 03 - Statistics
    dcc.Graph(id='rpm-graph', style={'width':600}),

], style={'width':600})

@app.callback(Output('rpm-graph', 'figure'),
[Input('station','value')])
def update_rpm_graph(selected_station):
    if selected_station:
        rides_per_month = ciclopi.loc[ciclopi['StazPrelievo']==selected_station].groupby('MesePrelievo').size().reset_index(name='Count')
    else:
        rides_per_month = ciclopi.groupby('MesePrelievo').size().reset_index(name='Count')
    print(rides_per_month)

    return go.Figure(
        data = [go.Bar( #Try to change .Bar with .Scatter
                    x=rides_per_month['MesePrelievo'],
                    y=rides_per_month['Count']
                )],
        layout=go.Layout(
            title='Rides per Month ' + str(selected_station),
            xaxis=dict(
                autotick=False,
                tickmode='array',
                tickvals=rides_per_month['MesePrelievo'],

            ),
            yaxis=dict(
                rangemode='tozero' #yaxis from zero
            ),
            width = 600,
        )
    )







if __name__ == '__main__':
    app.run_server(debug=True)
