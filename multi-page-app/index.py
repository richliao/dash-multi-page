from dash.dependencies import Input, Output
import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objs as go
import pandas as pd 

from app import app
from apps import app1, app2

df_gdp = pd.read_csv('https://raw.githubusercontent.com/plotly/datasets/master/gapminderDataFiveYear.csv')
df_gdp['TotalGDP'] = df_gdp['pop']*df_gdp['gdpPercap']
dfgdp2007 = df_gdp[df_gdp.year==2007]
dftop7 = dfgdp2007[['country','TotalGDP']].sort_values(['TotalGDP'], ascending=0)[:7]
s = dfgdp2007[['country','TotalGDP']].sort_values(['TotalGDP'], ascending=0)[7:].sum()
dftop7.loc[len(dftop7)]=['Others', s['TotalGDP']]

labels = dftop7['country']
values = dftop7['TotalGDP']
top7_trace = go.Pie(labels=labels, values=values)
hist_trace = go.Histogram(x=dfgdp2007['TotalGDP'])

index_page = html.Div([
    # This "header" will persist across pages
    html.H2('Sample Analytics', style={'textAlign': 'center'}),

    html.Div([
        html.Div([
            html.H5('2007 GPD Distribution', style={'textAlign': 'center'}),
            dcc.Graph(id='gGDPPie', figure=go.Figure(data=[top7_trace])),
            html.Div(id = 'gdpDistDiv')
            #dcc.Link('Men earning detail', href='/apps/app1')
        ], style = {'width': '70%','display':'table-cell'}),
        html.Div([
            html.P('GDP distribution presented by pie chart, click on the pie chart to get detail information', 
                style={'textAlign': 'center'})
        ], style = {'width': '30%','display':'table-cell', 'verticalAlign': 'middle'})

    ], style = {'width': '100%','display':'table'}),

    html.Div([
        html.H5('2007 GDP Histogram', style={'textAlign': 'center'}),
        dcc.Graph(id='gGDPHist', figure=go.Figure(data=[hist_trace])),
        html.Div(id = 'gdpHistDiv')
        #dcc.Link('Women earning detail', href='/apps/app2')
    ]),


    html.Div([
        html.Div([
            #html.H5('Gap distribution'),
            #dcc.Graph(id='gGap', figure=go.Histogram(data=[advisor_trace]))
        ], id = 'showinfo', className="six columns"),

    ], className="row")

])

app.layout = html.Div([
    # This Location component represents the URL bar
    dcc.Location(id='url', refresh=True),

    # Each "page" will modify this element
    html.Div(id='page-content'),
    
], className="container")

@app.callback(Output('page-content', 'children'),
              [Input('url', 'pathname')])
def display_page(pathname):
    if pathname == '/apps/app1':
         return app1.layout
    elif pathname == '/apps/app2':
         return app2.layout
    else:
        return index_page

@app.callback(Output('showinfo', 'children'),
              [Input('gGDPPie', 'clickData')])
def display_info(clickData):
    if clickData:
        for point in clickData['points']:
            print point['pointNumber']
            print point['label']
        return html.P(point['label'])

if __name__ == '__main__':
    app.run_server(debug=True)
