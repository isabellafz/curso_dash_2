from dash import Dash, html, dcc, Output, Input

app = Dash()


app.layout = html.Div([
    html.H3('Testando callbacks no dash'),
    html.Div([
        'Input',
        dcc.Input(id= 'my-input', value= 'teste', type='text')
    ]),
    html.Br(),
    html.Div(id='my-output')
])


@app.callback(
    Output(component_id='my-output', component_property='children'),
    Input(component_id='my-input', component_property='value')
    
)

def update_output(input_value):
    return f'Output: {input_value}'


if __name__ == '__main__':
    app.run_server(debug=True)