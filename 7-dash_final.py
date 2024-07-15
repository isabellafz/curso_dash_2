import pandas as pd
import plotly.express as px
from dash import Dash, dcc, html, Output, Input


# DataFrame
df = pd.read_csv('https://raw.githubusercontent.com/plotly/datasets/master/gapminder_unfiltered.csv')


app = Dash()

# layout 
app.layout = html.Div([
    html.H1('Dashboard com Dash',
            style={
                'textAlign': 'center'
            }),
    dcc.Dropdown(df.country.unique(), 'Canada', id='dropdown-selection'),
    dcc.Graph(id='graph-content')
])



#Callbacks

@app.callback(
    Output('graph-content', 'figure'),
    Input('dropdown-selection', 'value')
)

def update_graph(value):
    dff = df[df.country == value]
    return px.line(
        dff, 
        x='year',
        y='pop'
    )










# Rodar o servidor
if __name__ == '__main__':
    app.run_server(debug=True)
