import pandas as pd
import plotly.express as px
from dash import Dash, html, dcc, Output, Input

app = Dash()

# 1- criando dataframe

df = pd.DataFrame({
    'Fruits': ['Maçã', 'Laranja', 'Melão', 'Laranja', 'Uva', 'Melão'],
    'Amount': [4, 1, 2, 2, 4, 5],
    'City': ['Gramado', 'São Luís', 'Gramado', 'São Luís', 'Curitiba', 'Curitiba'],
})


# criando gráfico
fig = px.bar(
    df,
    x= 'Fruits',
    y= 'Amount',
    color= 'City',
    barmode= 'group'
)


# criando o dashboard

app.layout = html.Div(
    children= [
        html.H1('Hello Dash'),
        html.Div(
            children=
                '''
                    Dash: A web application framework for your data
                '''
        ),
        dcc.Graph(id= 'example-graph', figure=fig)
    ]
)



if __name__ == '__main__':
    app.run_server(debug=True)