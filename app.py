import pandas as pd
import dash
from dash import Dash, dcc, html
from dash.dependencies import Input, Output, State
import plotly.graph_objects as go
import plotly.express as px
import dash_bootstrap_components as dbc


# Dash Application


# app = dash.Dash(__name__)
app = dash.Dash(__name__,  external_stylesheets=[dbc.themes.SLATE])

server = app.server


# Datasets for The Hospital Cluster Visualization
datasets = pd.read_csv("lagosHosptals.csv")

datasets_lat = datasets[["lat"]]
datasets_long = datasets[["long"]]

geo_datas = datasets[["lat"]]

geo_datas["lon"] = datasets_long

geo_datas["lat"]
geo_datas["lon"]


K_clusters = range(1,10)

score = pd.read_csv('scoree.csv')
score = score.stack().tolist()

def line_fig():
    return  html.Div([
        dbc.Card(
            dbc.CardBody([
                dcc.Graph(
                    figure=px.line(x = K_clusters, y = score, title = 'Elbow Curve'
                       
                    ).update_layout(
                        template='plotly_dark',
                        plot_bgcolor= 'rgba(0, 0, 0, 0)',
                        paper_bgcolor= 'rgba(0, 0, 0, 0)',
                    ),
                    config={
                        'displayModeBar': False
                    }
                ) 
            ])
        ),  
    ])



Labels = pd.read_csv('Labels.csv')
Labels = Labels.to_numpy().flatten()

def scatter_fig():
    return  html.Div([
        dbc.Card(
            dbc.CardBody([
                dcc.Graph(
                    figure=px.scatter(geo_datas, x = geo_datas["lat"], y = geo_datas["lon"],
                           color = Labels, opacity = 0.8, size = geo_datas["lat"], 
                           size_max=30, title = 'LAGOS HOSPITAL CLUSTER'
                       
                    ).update_layout(
                        template='plotly_dark',
                        plot_bgcolor= 'rgba(0, 0, 0, 0)',
                        paper_bgcolor= 'rgba(0, 0, 0, 0)',
                    ),
                    config={
                        'displayModeBar': False
                    }
                ) 
            ])
        ),  
    ])

def line_fig():
    return  html.Div([
        dbc.Card(
            dbc.CardBody([
                dcc.Graph(
                    figure=px.line(x = K_clusters, y = score, title = 'Elbow Curve'
                       
                    ).update_layout(
                        template='plotly_dark',
                        plot_bgcolor= 'rgba(0, 0, 0, 0)',
                        paper_bgcolor= 'rgba(0, 0, 0, 0)',
                    ),
                    config={
                        'displayModeBar': False
                    }
                ) 
            ])
        ),  
    ])


def drawMap():
    return html.Div([
        dbc.Card(
            dbc.CardBody([
                                        html.Div(children=[html.Div(
                                        html.Div(html.Iframe(id='map',srcDoc = open('Hospital_around_Lagos.html', 'r').read(), width ='100%', height = '600', 
                                                                ),)),                       

                ],), 
            ])
        ),
    ])

def drawMap1():
    return html.Div([
        dbc.Card(
            dbc.CardBody([
                                        html.Div(children=[html.Div(
                                        html.Div(html.Iframe(id='map1',srcDoc = open('Centroid_Hosp.html', 'r').read(), width ='100%', height = '600', 
                                                                ),)),                       

                ],), 
            ])
        ),
    ])

def drawTitle(title):
    return html.Div([
        dbc.Card(
            dbc.CardBody([
                                        html.Div(children=[html.Div(
                                        html.Div(html.H1(title, 
                                                                style={'textAlign':'center','color':'#7570b3','font-size':'48'}),)),                       

                                                                ],), 
            ])
        ),
    ])

header = 'LAGOS HOSPITAL CLUSTER'


# Build App
app = Dash(external_stylesheets=[dbc.themes.SLATE])

app.layout = html.Div([
    dbc.Card(
        dbc.CardBody([
            dbc.Row([
                dbc.Col([
                    drawTitle(header)
                ], width=12),
            ], align='center'),
            html.Br(),
            dbc.Row([
                dbc.Col([
                    drawMap()
                ], width=12),
            ], align='center'), 
            html.Br(),
            dbc.Row([
                dbc.Col([
                    drawMap1()
                ], width=12),
            ], align='center'), 
            html.Br(),
            dbc.Row([
                dbc.Col([
                   line_fig() 
                ], width=5),
                dbc.Col([
                    scatter_fig()
                ], width=7),
            ], align='center'),      
        ]), color = 'dark'
    )
])


# Run the app
if __name__ == '__main__':
      app.run_server()






# import pandas as pd
# import dash
# import dash_html_components as html
# import dash_core_components as dcc
# from dash.dependencies import Input, Output, State
# import plotly.graph_objects as go
# import plotly.express as px


# # Dash Application


# app = dash.Dash(__name__)

# server = app.server


# # Datasets for The Hospital Cluster Visualization
# datasets = pd.read_csv("lagosHosptals.csv")

# datasets_lat = datasets[["lat"]]
# datasets_long = datasets[["long"]]

# geo_datas = datasets[["lat"]]

# geo_datas["lon"] = datasets_long

# geo_datas["lat"]
# geo_datas["lon"]


# K_clusters = range(1,10)

# score = pd.read_csv('scoree.csv')
# score = score.stack().tolist()
# line_fig = px.line(x = K_clusters, y = score, title = 'Elbow Curve')


# Labels = pd.read_csv('Labels.csv')
# Labels = Labels.to_numpy().flatten()
# fig = px.scatter(geo_datas, x = geo_datas["lat"], y = geo_datas["lon"],
#               color = Labels, opacity = 0.8, size = geo_datas["lat"], size_max=30, title = 'LAGOS HOSPITAL CLUSTER')


# # Application layout
# app.layout = html.Div(children=[ 
#                                 # TASK1: Add title to the dashboard

#                                 html.H1('LAGOS HOSPITAL CLUSTER',style={'textAlign':'center','color':'#7570b3','font-size':'48'}),

#                         html.Div(children=[html.Iframe(id = 'map', srcDoc = open('Hospital_around_Lagos.html', 'r').read(), width ='100%', height = '600',)],
#                         style={"background-color": "#0e1012","padding": "65px","justify-content": "space-around"}),
                        
# #                         html.Div(children=[dcc.Graph(id='plot', figure= fig_table)],
# #                         style={"background-color": "#0e1012","padding": "65px", "justify-content": "space-around","height":"50vh"}),
                        
#                         html.Div(children=[html.Iframe(id = 'map1', srcDoc = open('Centroid_Hosp.html', 'r').read(), width ='100%', height = '600',)],
#                         style={"background-color": "#0e1012","padding": "65px","justify-content": "space-around"}),
         
         
#         # html.Div(dcc.Graph(id='plot1', ),
#         #                                         style={"background-color": "#161A1D",
#         #                                         "padding": "60px",},), 
#                                                                                        # Create an outer division 
                            
                  
#         html.Div(children=[
                        
#                         html.Div(dcc.Graph(id='plot4', figure = line_fig,
#                                                 style={"background-color": "#161A1D","text-align": "center",
#                                                 "height":"70vh"}),),
#                         html.Div(dcc.Graph(id='plot5', figure = fig,
#                                                 style={"background-color": "#161A1D","text-align": "center",
#                                                 "height":"70vh"}),),],
#                         style={"display": "flex","background-color": "#0e1012","padding-bottom": "60px","justify-content": "space-around"}), 
                                   
                                
                            
#                                 ],style={"height": "100vh"})


# # Run the app
# if __name__ == '__main__':
#       app.run_server()
