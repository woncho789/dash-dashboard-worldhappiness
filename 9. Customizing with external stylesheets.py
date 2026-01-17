"""9. Customizing with external stylesheets

## CSS in Dash - external stylesheets
Set external_stylesheets of the Entire app
- load the app page with these additional CSS files
- supply with list of strings(URLs) or dicts

## CSS in Dash - local stylesheets
https://dash.plotly.com/external-resources

"""

from dash import Dash, html, dcc
import dash_bootstrap_components as dbc
import pandas as pd

soccer = pd.read_csv('./project/dash dashboard/fifa_soccer_players.csv')

app = Dash(external_stylesheets=[dbc.themes.CERULEAN])

app.layout = html.Div([
  html.H1('Soccer Players Dashboard',
          style={'textAlign':'center',
                'fontFamily':'fantasy',
                'fontSize':'50px',
                'color':'blue'}),
  html.P(['Source: ',
          html.A('Sofifa',
                 href='https://sofifa.com',
                 target='_blank')],
         style={'border':'solid'}),
  html.Label('Player name: '),
  dcc.Dropdown(
    options=soccer['long_name'].unique(),
    value=soccer['long_name'].unique()[0],
    style={'backgroundColor':'lightblue'})

],
style={'padding':100, 'border':'solid'})

if __name__ == '__main__':
  app.run(host='127.0.0.1', port=3000, debug=True)
