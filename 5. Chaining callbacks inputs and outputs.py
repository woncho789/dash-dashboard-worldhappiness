from dash import Dash, html, dcc, Input, Output
import pandas as pd
import plotly.express as px

happiness = pd.read_csv('./project/dash dashboard/world_happiness.csv')

app = Dash()

app.layout = html.Div([
    html.H1('World Happiness Dashboard'),
    html.P(['This dashboard shows the happiness score.',
            html.Br(),
            html.A('World Happiness Report Data Source',
                   href='https://worldshappiness.report',
                   target='_blank')]),
    dcc.RadioItems(id='region_radio',
                   options=happiness['region'].unique(),
                   value=happiness['region'].unique()[0],
                   inline=True),
    dcc.Dropdown(id='country_dropdown'),
    dcc.RadioItems(id='data_radio',
                   options={
                       'happiness_score':'Happiness Score',
                       'happiness_rank':'Happiness Rank'
                   },
                   value='happiness_score',
                   inline=True),
    dcc.Graph(id='happiness_graph', figure={}),   
    html.Div(id='average_div')
])

@app.callback(
    Output('country_dropdown','options'),
    Output('country_dropdown','value'),
    Input('region_radio','value')
)
def update_country_dropdown(selected_region):
    filtered_happiness = happiness[happiness['region']==selected_region]
    country_options = filtered_happiness['country'].unique()
    return country_options, country_options[0]


@app.callback(
    Output('happiness_graph','figure'),
    Output('average_div','children'),
    Input('country_dropdown','value'),
    Input('data_radio', 'value')
)
def update_graph(selected_country, selected_data):
    filtered_happiness = happiness[happiness['country']== selected_country]
    line_fig = px.line(filtered_happiness,
                       x='year', y=selected_data,
                       title = f'{selected_data.title()} in {selected_country}')
    selected_avg = filtered_happiness[selected_data].mean()
    return line_fig, f'The average {selected_data} for {selected_country}' \
                    f' is {selected_avg:.2f}'

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=3000, debug=True)
