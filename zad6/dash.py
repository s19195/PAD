# Run this app with `python app.py` and
# visit http://127.0.0.1:8050/ in your web browser.

from dash import Dash, dcc, html, Input, Output
import plotly.express as px
import pandas as pd
import seaborn as sns

app = Dash(__name__)

df = pd.read_csv('winequelity.csv')


# fig = px.box(df, x="gdp per capita", y="life expectancy",
#              color="continent", hover_name="country",
#              log_x=True, )


def generate_table(dataframe, max_rows=10):
    return html.Table([
        html.Thead(
            html.Tr([html.Th(col) for col in dataframe.columns])
        ),
        html.Tbody([
            html.Tr([
                html.Td(dataframe.iloc[i][col]) for col in dataframe.columns
            ]) for i in range(min(len(dataframe), max_rows))
        ])
    ])


app.layout = html.Div([
    html.H4(children='Wine Quality'),
    generate_table(df),
    html.Br(),
    html.Br(),
    dcc.RadioItems(
        id='Radio_Input',
        options=[
            {'label': 'Regression', 'value': 'Regression'},
            {'label': 'Classification', 'value': 'Classification'}
        ]
    ),
    html.Br(),
    html.Br(),
    dcc.RadioItems(
        id='Radio_Input2',
        options=[
            {'label': 'fixed acidity', 'value': 'fixed acidity'},
            {'label': 'volatile acidity', 'value': 'volatile acidity'},
            {'label': 'citric acid', 'value': 'citric acid'},
            {'label': 'residual sugar', 'value': 'residual sugar'},
            {'label': 'chlorides', 'value': 'chlorides'},
            {'label': 'free sulfur dioxide', 'value': 'free sulfur dioxide'},
            {'label': 'total sulfur dioxide', 'value': 'total sulfur dioxide'},
            {'label': 'density', 'value': 'density'},
            {'label': 'pH', 'value': 'pH'},
            {'label': 'sulphates', 'value': 'sulphates'},
            {'label': 'alcohol', 'value': 'alcohol'},
            {'label': 'quality', 'value': 'quality'},
            {'label': 'target', 'value': 'target'}
        ]
    ),
    dcc.Graph(id='graph'),
])


@app.callback(
    Output(component_id='graph', component_property='figure'),
    Input(component_id='Radio_Input', component_property='value'),
    Input(component_id='Radio_Input2', component_property='value')
)
def build_graph(radio_input, radio_input2):
    if radio_input == 'Regression':
        fig = px.scatter(df, x=radio_input2, y="pH")
        return fig
    else:
        fig = px.box(
            df,
            x="target",
            y=radio_input2)
        return fig


if __name__ == '__main__':
    app.run_server(debug=True)
