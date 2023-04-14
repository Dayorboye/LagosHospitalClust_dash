import pandas as pd
import dash
import dash_html_components as html
import dash_core_components as dcc
from dash.dependencies import Input, Output, State
import plotly.graph_objects as go
import plotly.express as px
from dash import no_update
# from jobs import app
# from jobs.routes import *

import sys
print(sys.version)
# Dash Application

app = dash.Dash(__name__)


import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
import seaborn as sns; sns.set()


# Datasets for The Hospital Cluster Visualization
datasets = pd.read_excel("lagosHosptals.xlsx")

datasets_lat = datasets[["lat"]]
datasets_long = datasets[["long"]]

geo_datas = datasets[["lat"]]

geo_datas["lon"] = datasets_long

geo_datas["lat"]
geo_datas["lon"]


K_clusters = range(1,10)
kmeans = [KMeans(n_clusters=i) for i in K_clusters]
Y_axis = geo_datas[['lon']]
X_axis = geo_datas[['lat']]
score = [kmeans[i].fit(Y_axis).score(Y_axis) for i in range(len(kmeans))]
# Visualize
line_fig = px.line(x = K_clusters, y = score, title = 'Elbow Curve')


KMNs = KMeans(n_clusters=6)

KMNs.fit(geo_datas)

Labels = KMNs.predict(geo_datas)

Centroid = KMNs.cluster_centers_
a = Centroid[:,0]
b = Centroid[:,1]

from geopandas.tools import geocode
import pandas as pd
from geopy.geocoders import ArcGIS

geolocator = ArcGIS()

Centriod_df = pd.DataFrame(Centroid, columns=["Latitude","Longitude"])
Centriod_df['geo_coord'] = Centriod_df.apply(lambda row: (str(row.Latitude),str(row.Longitude)),axis=1)
Centriod_df['address'] = Centriod_df.apply(lambda row: geolocator.reverse(row.geo_coord).address,axis=1)

Centroid = Centriod_df[['Latitude','Longitude','address']]
Centroid

fig = px.scatter(geo_datas, x = geo_datas["lat"], y = geo_datas["lon"],
              color = Labels, opacity = 0.8, size = geo_datas["lat"], size_max=30, title = 'LAGOS HOSPITAL CLUSTER')


fig_table = go.Figure(data=[go.Table(
    header=dict(values=list(Centroid.columns),
                fill_color='paleturquoise',
                align='left'),
    cells=dict(values=[Centroid.Latitude, Centroid.Longitude, Centroid.address],
               fill_color='lavender',
               align='left'))
])


# Application layout
app.layout = html.Div(children=[ 
                                # TASK1: Add title to the dashboard

                                html.H1('LAGOS HOSPITAL CLUSTER',style={'textAlign':'center','color':'#7570b3','font-size':'48'}),

                        html.Div(children=[html.Iframe(id = 'map', srcDoc = open('Hospital_around_Lagos.html', 'r').read(), width ='100%', height = '600',)],
                        style={"background-color": "#0e1012","padding": "65px","justify-content": "space-around"}),
                        
                        html.Div(children=[dcc.Graph(id='plot', figure= fig_table)],
                        style={"background-color": "#0e1012","padding": "65px", "justify-content": "space-around","height":"50vh"}),
         
         
        # html.Div(dcc.Graph(id='plot1', ),
        #                                         style={"background-color": "#161A1D",
        #                                         "padding": "60px",},), 
                                                                                       # Create an outer division 
                            
                  
        html.Div(children=[
                        
                        html.Div(dcc.Graph(id='plot4', figure = line_fig,
                                                style={"background-color": "#161A1D","text-align": "center",
                                                "height":"70vh"}),),
                        html.Div(dcc.Graph(id='plot5', figure = fig,
                                                style={"background-color": "#161A1D","text-align": "center",
                                                "height":"70vh"}),),],
                        style={"display": "flex","background-color": "#0e1012","padding-bottom": "60px","justify-content": "space-around"}), 
                                   
                                
                            
                                ],style={"height": "100vh"})


# Run the app
if __name__ == '__main__':
      app.run_server()




