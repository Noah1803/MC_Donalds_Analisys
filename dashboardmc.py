import pandas as pd
import numpy as np
import plotly.express as px
import requests
import plotly.graph_objects as go
import seaborn as sns
import matplotlib.pyplot as plt
import dash
from dash import html, dcc
from dash.dependencies import Input, Output, State
import plotly.graph_objs as go
from sklearn.linear_model import LinearRegression

df = pd.read_csv('McDonald_s_Reviews.csv',encoding='latin-1')

# Iniciar o aplicativo Dash
app = dash.Dash(__name__)

# Layout da dashboard
app.layout = html.Div([
    html.H1('Análise de Regressão Linear Múltipla'),

     # Seletor de colunas para variável dependente (alvo)
    html.Label('Selecione a variável dependente:'),
    # dcc.Dropdown(
    #     id='variavel-dependente',
    #     options=[{'label': col, 'value': col} for col in df.columns if col != 'variavel_alvo']
    # ),

    # # Seletor de colunas para variáveis independentes
    # html.Label('Selecione as variáveis independentes:'),
    # dcc.Dropdown(
    #     id='variaveis-independentes',
    #     options=[{'label': col, 'value': col} for col in df.columns if col != 'variavel_alvo'],
    #     multi=True
    # ),

    # # Botão para rodar a regressão
    # html.Button('Rodar Regressão', id='botao-regressao', n_clicks=0),

     # Botão para rodar a regressão
    html.Button('Criar Mapa', id='botao-criar-mapa', n_clicks=0),

    #Mapa para analisar onde estão os locais
    dcc.Graph(id='Mapa de Localização'),

    #  # Gráfico de barras para a análise de oportunidades
    # dcc.Graph(id='grafico-analise-oportunidades'),

    #  # Gráfico de barras para o impacto dos coeficientes
    # dcc.Graph(id='grafico-impacto-coeficientes')

])

@app.callback(
    [Output('Mapa de Localização', 'figure')],
    Input('botao-criar-mapa', 'n_clicks')
    # Input('variavel-dependente', 'value'),
    # Input('variaveis-independentes', 'value')
)
def criar_mapa(n_clicks):
    if n_clicks > 0:
        print("Botão pressionado!")  # Verifique se o botão está sendo pressionado
        mapbox_token = requests.get('https://api.mapbox.com/?access_token=myaccesstoken').text
        px.set_mapbox_access_token(mapbox_token)  # Verifique o token do Mapbox

        # Crie o mapa como explicado anteriormente
        fig = px.scatter_mapbox(df, lat='latitude ', lon='longitude', color='rating_count',
                               color_continuous_scale=px.colors.cyclical.IceFire, size_max=15, zoom=3, opacity=0.4)
        fig.update_layout(mapbox_style="open-street-map", mapbox_center={"lat": 40.543138, "lon": -111.69486})
        
        print("Figura criada:", fig)  # Verifique a figura criada
        return [fig]

    return [go.Figure()]

if __name__ == '__main__':
    app.run_server(host='192.168.15.101', port=8050, debug=True)