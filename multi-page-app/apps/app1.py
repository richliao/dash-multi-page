from dash.dependencies import Input, Output
import dash_html_components as html
import dash_core_components as dcc
import dash_table_experiments as dt

from app import app

# layout = html.Div([
# html.H3('App 1'),
# dcc.Dropdown(
#     id='app-1-dropdown',
#     options=[
#         {'label': 'App 1 - {}'.format(i), 'value': i} for i in [
#             'NYC', 'MTL', 'LA'
#         ]
#     ]
# ),
# html.Div(id='app-1-display-value'),
# dcc.Link('Go to App 2', href='/apps/app2')
# ])

def return_Layout(dfCountry, country):
    return html.Div([
        html.H5(country+' GPD Time Series Table', style={'textAlign': 'center'}),
        dt.DataTable(
                rows=dfCountry.to_dict('records'),

                # optional - sets the order of columns
                columns=sorted(dfCountry.columns),

                row_selectable=True,
                filterable=True,
                sortable=True,
                selected_row_indices=[],
                id='datatable-gdpCountry'
            ),
    ])    


