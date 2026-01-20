"""ch11 Building a Navigation Bar.py

dbc.NavbarSimple()

"""

from dash import Dash, html
import dash_bootstrap_components as dbc

app = Dash(external_stylesheets=[dbc.themes.BOOTSTRAP])

navbar = dbc.NavbarSimple(
    brand='Soccer Players Dashboard',
    children=[
        html.Img(src='https://uptime.com/media/website_profiles/sofifa.com.png',
                 height=20),
        html.A('Data Source',
               href = 'https://sofifa.com',
               target= '_blank',
               style={'color':'black'})
    ],
    color = 'primary',
    fluid=True
)

app.layout = html.Div(
    navbar
)

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=3000, debug=True)
