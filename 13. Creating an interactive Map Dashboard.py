"""13. Creating an interactive Map Dashboard.py

dcc.Graph interactive properties
- hoverData: hover over points
- clickData: click on points
- selectData: select regions of points
- relayoutData: zoom

"""

from dash import Dash, html, dcc, dash_table, Input, Output
import plotly.express as px
import pandas as pd
import dash_bootstrap_components as dbc

electricity = pd.read_csv('./project/dash dashboard/electricity.csv')

year_min = electricity['Year'].min()
year_max = electricity['Year'].max()

app = Dash(external_stylesheets=[dbc.themes.BOOTSTRAP])

app.layout = html.Div([
    html.H1('Electricity Prices by US State'),
    dcc.RangeSlider(id='year_slider',
                    min = year_min,
                    max = year_max,
                    value = [year_min, year_max],
                    marks={i:str(i) for i in range(year_min, year_max+1)}),
    dcc.Graph(id='map_graph'),
    dash_table.DataTable(id='price_info')
])

@app.callback(
    Output('map_graph','figure'),
    Input('year_slider', 'value')
)
def update_map_graph(selected_years):
    filtered_electricity= electricity[
        (electricity['Year']>=selected_years[0]) &
        (electricity['Year']<=selected_years[1])
    ]
    avg_price_electricity= filtered_electricity.groupby('US_State')['Residential Price'].mean().reset_index()
    map_fig = px.choropleth(avg_price_electricity,
                            locations = 'US_State',
                            locationmode = 'USA-states',
                            color = 'Residential Price',
                            scope = 'usa',
                            color_continuous_scale = 'reds')
    return map_fig

@app.callback(
    Output('price_info','data'),
    Input('map_graph', 'clickData'),
    Input('year_slider','value')
)
def print_click_data(clicked_data, selected_years):
    if clicked_data is None:
        return []
    us_state= clicked_data['points'][0]['location']
    filtered_electricity= electricity[
        (electricity['Year']>=selected_years[0]) &
        (electricity['Year']<=selected_years[1]) &
        (electricity['US_State']==us_state)
    ]
    return filtered_electricity.to_dict('records')

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=3000, debug=True)
