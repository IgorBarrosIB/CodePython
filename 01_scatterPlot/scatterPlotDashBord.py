import dash 
import dash_core_components as dcc
import dash_html_components as html
import dash_bootstrap_components as dbc

import plotly.express as px
import plotly.graph_objects as go 

import numpy as np
import pandas as pd 
import json


#=================== TRATAMENTO DE DADOS =============================
# pd.set_option('display.max_rows', 100)
# df = pd.read_csv("covid.csv",  sep=";")
# df_brasil = df[df['estado'].isna() & df["codmun"].isna()]
# df_states = df[~df["estado"].isna() & df["codmun"].isna()]
# df_brasil = df[df["regiao"] == "Brasil"]

# df_states.to_csv("df_states.csv")
# df_brasil.to_csv("df_brasil.csv")

# ================ LEITURA DOS DADOS ===================================
df_states = pd.read_csv("df_states.csv")
df_brasil = pd.read_csv("df_brasil.csv")
df_states_=  df_states[df_states["data"] == "2020-05-13"]

df_data =  df_states[df_states["estado"] == "RJ"]

# ================= INSTANCIAÇÃO DO DASH ==============================

brazil_states = json.load(open("geojson/brazil_geo.json", "r"))

fig = px.scatter(df_states_, x="estado", y="casosNovos",  color="casosAcumulado",
hover_data={"casosAcumulado":True, "casosNovos": True, "obitosNovos":True, "estado": True})

fig.update_layout(
  paper_bgcolor="#242424",
  margin=go.Margin(l=0, r=0, t=0, b=0),
  showlegend=False,
)

# fig.show()

fig2 = go.Figure()
fig2.add_trace 

# ==============================LAYOUT=================================
app = dash.Dash(__name__, external_stylesheets=[dbc.themes.CYBORG])

app.layout =dbc.Container(
  [
        dbc.Row(
            [  
              dbc.Col(html.Div("Scatter Plots in Python", id="titulo"), md=12),   
            ]
        ),
        dbc.Row(
            [
              dbc.Col(html.Div(dcc.Graph(id="choropleth-map", figure=fig)), width=6, lg=12, md=12),
            ]
        ),
    ]
)

#  dcc.Graph(id="choropleth-map", figure=fig)

if __name__ == "__main__":
  app.run_server(debug=True)

