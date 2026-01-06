from dash import Dash, dcc, html, Output, Input

# create a dash app
app = Dash()

# initialize input and output objects
input_text = dcc.Input(value='Change this text', type = 'text')
output_text = html.Div()

app.layout = html.Div([
    html.H1('Hello Dash'),
    html.Div(children='Dash:a web application framework for your data'),
    input_text,
    output_text
])

@app.callback(
    Output(component_id=output_text, component_property='children'),
    Input(component_id=input_text, component_property='value')
)
def update_output_div(input_text):
    return f'Text: {input_text}'

if __name__ == '__main__':
    app.run(host='127.0.0.1',port=3000, debug=True)
