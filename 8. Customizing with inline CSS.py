""" 8. Customizing with inline CSS.py

## What is CSS?
CSS (Cascading Style Sheets): describe how the HTML elements are displayed, including colors, fonts, layout

Separation of style formatting and content
- HTML : describe the content
- CSS : format the style

## CSS syntax
CSS syntax requires two elements.
- element selector : point to the HTML elements to style
- declaration block : declares a list of style properties by their names an values

## CSS in Dash: Inline style
- set the style property for individual Dash components
- supply a dictionary with keys (property names) and values
- Keys (property names) are camleCased
  - html.H1('MyDashboard', style = {'textAlign':'center', 'color':'blue'})

"""

from dash import Dash, html, dcc
import pandas as pd

soccer = pd.read_csv('fifa_soccer_players.csv')

app = Dash()

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
