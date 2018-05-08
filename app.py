# -*- coding: utf-8  -*-
import pandas as pd
import numpy as np

import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.plotly as py #import plotly
import plotly.graph_objs as go #import graphs objects


app = dash.Dash()


ciclopi=pd.read_csv("data/04_ciclopi_cleaned.csv", sep=';', \
                    parse_dates=['DataOraPrelievo','DataOraDeposito','DataPrelievo','OrarioPrelievo','OrarioDeposito','DataDeposito'])
rides_per_month = ciclopi.groupby('MesePrelievo').size().reset_index(name='Count')

app.layout = html.Div(children=[
    html.H1(children='Ciclopi Statistics'),

    # creating a graph done in Notebook 03 - Statistics



    dcc.Graph(
        id='rpm-graph',
        style={'width':600},
        figure=go.Figure(
            data = [
                go.Bar( #Try to change .Bar with .Scatter
                    x=rides_per_month['MesePrelievo'],
                    y=rides_per_month['Count']
                )
            ],
            layout = go.Layout(
                title='Rides per Month',
                xaxis=dict(
                    autotick=False,
                    tickmode='array',
                    tickvals=rides_per_month['MesePrelievo'],

                ),
                yaxis=dict(
                    rangemode='tozero' #yaxis from zero
                )
            )
        )
    )
])



if __name__ == '__main__':
    app.run_server(debug=True)
