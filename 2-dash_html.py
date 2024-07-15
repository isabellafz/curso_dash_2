import dash
from dash import dcc, html
from datetime import datetime

app = dash.Dash()

app.layout = html.Div(
    children= [
        html.Img(src='https://github.com/MurilloZanchetta.png'),
        html.Hr(),
        html.H1('Testando o Dash com html'),
        html.Span(
            children= [
                f'Hoje é  {datetime.now().date()}',
                html.Br(),
                'Desenvolvido por ', html.B('Murillo'),
                html.Br(),
                html.I('DevOps Jr')
            ]
        )
    ]
)


if __name__ == '__main__':
    app.run_server(debug=True)