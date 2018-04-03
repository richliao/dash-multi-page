Ehanced version of multi-pages app demo

1. Pass information as pathname to different url route     
@app.callback(Output('page-content', 'children'),     
              [Input('url', 'pathname')])      
def display_page(pathname):    
    if pathname.startswith('/apps/app1'):   
        country = pathname.split('/')[-1]   
        dfCountry = df_gdp[df_gdp.country==country]
        return app1.return_Layout(dfCountry, country)
    elif pathname == '/apps/app2':
         return app2.layout
    else:
        return index_page
        
2. Dynamic generate url route based on user selection of the pie chart
@app.callback(Output('showinfo', 'children'),
              [Input('gGDPPie', 'clickData')])
def display_info(clickData):
    if clickData:
        for point in clickData['points']:
            print point['pointNumber']
            print point['label']
        return dcc.Link('Detail time series data of '+ point['label'], href='/apps/app1/'+point['label'])

![demo](./image/demo.gif)
