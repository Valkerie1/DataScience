import streamlit as st
import numpy as np
import pandas as pd
import requests
import json
import plotly.express as px
import plotly.graph_objects as go
import time
from sklearn.linear_model import LinearRegression as lr
import dash
from dash import dcc
from dash import html
from dash.dependencies import Input, Output

st.title('Australian Air Traffic forecast for 2030')
st.subheader('Table of contents')
st.text("""
- 1. Introduction
- 2. Australian airports
- 3. Exploratory Data Analysis
- 4. Forecasting until 2030
- 5. Conclusion



""")
#chapter 1
st.subheader('1. Introduction')
st.write("""
Getting up early to catch a flight? I am sure that sounds familiar to you, whether it is for an important meeting or just for your relaxing holiday on the other side of the world.

It is estimated that there are roughly 100.000 flights per day all around the world. 
All these flights move an estimated 6 million passengers. Most of the time, air travel is preferred for long distances. 
Surely, a large country such as Australia must have a large number of daily flights. 
The long distances, makes domestic flights a very suitable mode of transport, but how many air traffic movements are there? 
And what is the estimated air traffic in 2030? 
Since, air transportation is at the heart of the Australian economic growth, this estimation is crucial to further support and strengthen the aviation industry and look at pathways for the longer-term.

""")

# import data
url1= 'https://data.gov.au/data/dataset/cc5d888f-5850-47f3-815d-08289b22f5a8/resource/38bdc971-cb22-4894-b19a-814afc4e8164/download/mon_pax_web.csv'  
url2= 'https://data.gov.au/data/dataset/cc5d888f-5850-47f3-815d-08289b22f5a8/resource/583be26d-59b9-4bcc-827d-4d9f7162fb04/download/mon_acm_web.csv'
passengers= pd.read_csv(url1)
aircraft= pd.read_csv(url2)

df= passengers.merge(aircraft, on= ['AIRPORT', 'Year', 'Month'])
df["Pax_Total_Year"]= df.groupby(["AIRPORT", "Year"])["Pax_Total"].transform('cumsum')
df["Acm_Total_Year"]= df.groupby(["AIRPORT", "Year"])["Acm_Total"].transform('cumsum')
df.drop(df[(df.AIRPORT == 'BALLINA') & (df.Acm_Total == 0)].index, inplace= True)

cols=['Year','Month']
df['Date'] = df[cols].apply(lambda x: '-'.join(x.values.astype(str)), axis='columns')
df['Date'] = pd.to_datetime(df['Date'])



#chapter 2
st.subheader('2. Australian Airports')
st.write("""

""")


# chapter 3
st.subheader('3. Exploratory Data Analysis')
# fig pax growth
dropdown_buttons= [{'label': 'All',
            'method': 'update',
            'args': [{'visible': [True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True]},
                        {'title': 'All Airports'}]},
            {'label': 'Adelaide',
            'method': 'update',
            'args': [{'visible': [True, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False]},
                        {'title': 'Adelaide'}]},
            {'label': 'Alce Springs',
            'method': 'update',
            'args': [{'visible': [False, True, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False]},
                        {'title': 'Alice Springs'}]},
            {'label': 'Ballina',
            'method': 'update',
            'args': [{'visible': [False, False, True, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False]},
                        {'title': 'Ballina'}]},
            {'label': 'Brisbane',
            'method': 'update',
            'args': [{'visible': [False, False, False, True, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False]},
                        {'title': 'Brisbane'}]},
            {'label': 'Cairns',
            'method': 'update',
            'args': [{'visible': [False, False, False, False, True, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False]},
                        {'title': 'Cairns'}]},
            {'label': 'Canberra',
            'method': 'update',
            'args': [{'visible': [False, False, False, False, False, True, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False]},
                        {'title': 'Canberra'}]},
            {'label': 'Darwin',
            'method': 'update',
            'args': [{'visible': [False, False, False, False, False, False, True, False, False, False, False, False, False, False, False, False, False, False, False, False, False]},
                        {'title': 'Darwin'}]},
            {'label': 'Gold Coast',
            'method': 'update',
            'args': [{'visible': [False, False, False, False, False, False, False, True, False, False, False, False, False, False, False, False, False, False, False, False, False]},
                        {'title': 'Gold Coast'}]},
            {'label': 'Hamilton Island',
            'method': 'update',
            'args': [{'visible': [False, False, False, False, False, False, False, False, True, False, False, False, False, False, False, False, False, False, False, False, False]},
                        {'title': 'Hamilton Island'}]},
            {'label': 'Hobart',
            'method': 'update',
            'args': [{'visible': [False, False, False, False, False, False, False, False, False, True, False, False, False, False, False, False, False, False, False, False, False]},
                        {'title': 'Hobart'}]},
            {'label': 'Karratha',
            'method': 'update',
            'args': [{'visible': [False, False, False, False, False, False, False, False, False, False, True, False, False, False, False, False, False, False, False, False, False]},
                        {'title': 'Karratha'}]},
            {'label': 'Launceston',
            'method': 'update',
            'args': [{'visible': [False, False, False, False, False, False, False, False, False, False, False, True, False, False, False, False, False, False, False, False, False]},
                        {'title': 'Launceston'}]},
            {'label': 'Mackay',
            'method': 'update',
            'args': [{'visible': [False, False, False, False, False, False, False, False, False, False, False, False, True, False, False, False, False, False, False, False, False]},
                        {'title': 'Mackay'}]},
            {'label': 'Melbourne',
            'method': 'update',
            'args': [{'visible': [False, False, False, False, False, False, False, False, False, False, False, False, False, True, False, False, False, False, False, False, False]},
                        {'title': 'Melbourne'}]},
            {'label': 'Perth',
            'method': 'update',
            'args': [{'visible': [False, False, False, False, False, False, False, False, False, False, False, False, False, False, True, False, False, False, False, False, False]},
                        {'title': 'Perth'}]},
            {'label': 'Rockhampton',
            'method': 'update',
            'args': [{'visible': [False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, True, False, False, False, False, False]},
                        {'title': 'Rockhampton'}]},
            {'label': 'Sunshine Coast',
            'method': 'update',
            'args': [{'visible': [False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, True, False, False, False, False]},
                        {'title': 'Sunshine Coast'}]},
            {'label': 'Sydney',
            'method': 'update',
                        'args': [{'visible': [False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, True, False, False, False]},
            {'title': 'Sydney'}]},
            {'label': 'Townsville',
            'method': 'update',
            'args': [{'visible': [False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, True, False, False]},
                        {'title': 'Townsville'}]},
            {'label': 'Newcastle',
            'method': 'update',
            'args': [{'visible': [False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, True, False]},
                        {'title': 'Newcastle'}]},
            {'label': 'Ayers Rock',
            'method': 'update',
            'args': [{'visible': [False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, True]},
                        {'title': 'Ayers Rock'}]},
]
airports = ['ADELAIDE', 'ALICE SPRINGS', 'BALLINA', 'BRISBANE', 'CAIRNS', 'CANBERRA','DARWIN', 'GOLD COAST', 
            'HAMILTON ISLAND', 'HOBART', 'KARRATHA', 'LAUNCESTON', 'MACKAY', 'MELBOURNE', 'PERTH', 
            'ROCKHAMPTON', 'SUNSHINE COAST', 'SYDNEY', 'TOWNSVILLE', 'NEWCASTLE', 'AYERS ROCK']

df_month12=df.query('Month ==12')
fig = go.Figure()
for airport in airports:
            fig.add_trace(go.Scatter(x= df_month12[df_month12['AIRPORT'] == airport]['Year'],
            y= df_month12[df_month12['AIRPORT'] == airport]['Pax_Total'],
            mode= 'lines+markers',
            name= airport))

fig.update_layout(title_text="Passenger growth Australian airports",
            xaxis_title='Years',
            yaxis_title='Total number of passengers', width=960, height=620,
            title={'x':0.5, 'xanchor':'center'})



fig.update_layout({
            'updatemenus':[{'type': 'dropdown',
            'x': 1.24, 'y': 1.1,
            'showactive': True, 'active': 0,
            'buttons': dropdown_buttons
            }]})

st.write("""
As can be seen on this plot, over the years the amount of passengers has grown tremendously. 
The front runners are obviously the country's largest cities, Sydney, Melbourne, Brisbane and Perth. Besides, a huge crash can be observed in 2020. 
This crash is caused by the covid-19 pandemic. 
During this period of upheaval and uncertainty the borders of Australia were closed. However, the plot shows that in this year the airports still receive passengers, 
just not as much as previous years. To see in which months covid-19 had an influence on the growth, the following scatterplot has been made.

""")
st.plotly_chart(fig)

# fig 2 pax vs acm
dropdown_buttons2= [{'label': 'All', 
                    'method': 'update', 
                    'args': [{'visible': [True, True, True, True, True,
                                          True, True, True, True, True,
                                          True, True, True, True, True,
                                          True, True, True, True, True,
                                          True, 
                                          False, False, False, False, False, 
                                          False, False, False, False, False, 
                                          False, False, False, False,False, 
                                          False, False, False, False, False, 
                                          False]}, 
                             {'title': 'Aircraft and Passenger movements of all Australian airports 1986-2021'}]},
                  {'label': 'Adelaide', 
                   'method': 'update', 
                   'args': [{'visible': [True, False, False, False, False, 
                                         False, False, False, False, False, 
                                          False, False, False, False,False, 
                                          False, False, False, False, False, 
                                          False, 
                                          True, False, False, False, False, 
                                          False, False, False, False, False, 
                                          False, False, False, False,False, 
                                          False, False, False, False, False, 
                                          False]},
                            {'title': 'Aircraft and Passenger movements of Adelaide 1986-2021'}]},
                  {'label': 'Alce Springs',
                   'method': 'update', 
                   'args': [{'visible': [False, True, False, False, False, 
                                          False, False, False, False, False, 
                                          False, False, False, False,False, 
                                          False, False, False, False, False, 
                                          False, 
                                          False, True, False, False, False, 
                                          False, False, False, False, False, 
                                          False, False, False, False,False, 
                                          False, False, False, False, False, 
                                          False]},
                            {'title': 'Aircraft and Passenger movements of Alice Springs 1986-2021'}]},
                  {'label': 'Ballina', 
                   'method': 'update', 
                   'args': [{'visible': [False, False, True, False, False, 
                                          False, False, False, False, False, 
                                          False, False, False, False,False, 
                                          False, False, False, False, False, 
                                          False,
                                        False, False, True, False, False, 
                                          False, False, False, False, False, 
                                          False, False, False, False,False, 
                                          False, False, False, False, False, 
                                          False]}, 
                            {'title': 'Aircraft and Passenger movements of  Ballina 1986-2021'}]},
                  {'label': 'Brisbane', 
                   'method': 'update', 
                   'args': [{'visible': [False, False, False, True, False, 
                                          False, False, False, False, False, 
                                          False, False, False, False,False, 
                                          False, False, False, False, False, 
                                          False,
                                        False, False, False, True, False, 
                                          False, False, False, False, False, 
                                          False, False, False, False,False, 
                                          False, False, False, False, False, 
                                          False]}, 
                            {'title': 'Aircraft and Passenger movements of  Brisbane 1986-2021'}]},
                  {'label': 'Cairns', 
                   'method': 'update', 
                   'args': [{'visible': [False, False, False, False, True, 
                                          False, False, False, False, False, 
                                          False, False, False, False,False, 
                                          False, False, False, False, False, 
                                          False,
                                        False, False, False, False, True, 
                                          False, False, False, False, False, 
                                          False, False, False, False,False, 
                                          False, False, False, False, False, 
                                          False]}, 
                            {'title': 'Aircraft and Passenger movements of  Cairns 1986-2021'}]},
                  {'label': 'Canberra', 
                   'method': 'update', 
                   'args': [{'visible': [False, False, False, False, False, 
                                          True, False, False, False, False, 
                                          False, False, False, False,False, 
                                          False, False, False, False, False, 
                                          False,
                                        False, False, False, False, False, 
                                          True, False, False, False, False, 
                                          False, False, False, False,False, 
                                          False, False, False, False, False, 
                                          False]}, 
                            {'title': 'Aircraft and Passenger movements of Canberra 1986-2021'}]},
                  {'label': 'Darwin', 
                   'method': 'update', 
                   'args': [{'visible': [False, False, False, False, False, 
                                          False, True, False, False, False, 
                                          False, False, False, False,False, 
                                          False, False, False, False, False, 
                                          False,
                                        False, False, False, False, False, 
                                          False, True, False, False, False, 
                                          False, False, False, False,False, 
                                          False, False, False, False, False, 
                                          False]}, 
                            {'title': 'Aircraft and Passenger movements of Darwin 1986-2021'}]},
                  {'label': 'Gold Coast', 
                   'method': 'update', 
                   'args': [{'visible': [False, False, False, False, False, 
                                          False, False, True, False, False, 
                                          False, False, False, False,False, 
                                          False, False, False, False, False, 
                                          False,
                                        False, False, False, False, False, 
                                          False, False, True, False, False, 
                                          False, False, False, False,False, 
                                          False, False, False, False, False, 
                                          False]}, 
                            {'title': 'Aircraft and Passenger movements of  Gold Coast 1986-2021'}]},
                  {'label': 'Hamilton Island', 
                   'method': 'update', 
                   'args': [{'visible': [False, False, False, False, False, 
                                          False, False, False, True, False, 
                                          False, False, False, False,False, 
                                          False, False, False, False, False, 
                                          False,
                                        False, False, False, False, False, 
                                          False, False, False, True, False, 
                                          False, False, False, False,False, 
                                          False, False, False, False, False, 
                                          False]}, 
                            {'title': 'Aircraft and Passenger movements of Hamilton Island 1986-2021'}]},
                  {'label': 'Hobart', 
                   'method': 'update', 
                   'args': [{'visible': [False, False, False, False, False, 
                                          False, False, False, False, True, 
                                          False, False, False, False,False, 
                                          False, False, False, False, False, 
                                          False,
                                        False, False, False, False, False, 
                                          False, False, False, False, True, 
                                          False, False, False, False,False, 
                                          False, False, False, False, False, 
                                          False]}, 
                            {'title': 'Aircraft and Passenger movements of Hobart 1986-2021'}]},
                   {'label': 'Karratha', 
                   'method': 'update', 
                   'args': [{'visible': [False, False, False, False, False, 
                                          False, False, False, False, False, 
                                          True, False, False, False,False, 
                                          False, False, False, False, False, 
                                          False,
                                        False, False, False, False, False, 
                                          False, False, False, False, False, 
                                          True, False, False, False,False, 
                                          False, False, False, False, False, 
                                          False]}, 
                            {'title': 'Aircraft and Passenger movements of Karratha 1986-2021'}]},
                  {'label': 'Launceston', 
                   'method': 'update', 
                   'args': [{'visible': [False, False, False, False, False, 
                                          False, False, False, False, False, 
                                          False, True, False, False,False, 
                                          False, False, False, False, False, 
                                          False,
                                        False, False, False, False, False, 
                                          False, False, False, False, False, 
                                          False, True, False, False,False, 
                                          False, False, False, False, False, 
                                          False]}, 
                            {'title': 'Aircraft and Passenger movements of Launceston 1986-2021'}]},
                  {'label': 'Mackay', 
                   'method': 'update', 
                   'args': [{'visible': [False, False, False, False, False, 
                                          False, False, False, False, False, 
                                          False, False, True, False, False, 
                                          False, False, False, False, False, 
                                          False,
                                        False, False, False, False, False, 
                                          False, False, False, False, False, 
                                          False, False, True, False, False, 
                                          False, False, False, False, False, 
                                          False]}, 
                            {'title': 'Aircraft and Passenger movements of Mackay 1986-2021'}]},
                   {'label': 'Sunshine Coast', 
                   'method': 'update', 
                   'args': [{'visible': [False, False, False, False, False, 
                                          False, False, False, False, False, 
                                          False, False, False, True, False, 
                                          False, False, False, False, False, 
                                          False,
                                        False, False, False, False, False, 
                                          False, False, False, False, False, 
                                          False, False, False, True, False, 
                                          False, False, False, False, False, 
                                          False]}, 
                            {'title': 'Aircraft and Passenger movements of Sunshine Coast 1986-2021'}]},
                   {'label': 'Perth', 
                   'method': 'update', 
                   'args': [{'visible': [False, False, False, False, False, 
                                          False, False, False, False, False, 
                                          False, False, False, False, True, 
                                          False, False, False, False, False, 
                                          False,
                                        False, False, False, False, False, 
                                          False, False, False, False, False, 
                                          False, False, False, False, True, 
                                          False, False, False, False, False, 
                                          False]}, 
                            {'title': 'Aircraft and Passenger movements of Perth 1986-2021'}]},
                   {'label': 'Rockhampton', 
                   'method': 'update', 
                   'args': [{'visible': [False, False, False, False, False, 
                                          False, False, False, False, False, 
                                          False, False, False, False, False, 
                                          True, False, False, False, False, 
                                          False,
                                        False, False, False, False, False, 
                                          False, False, False, False, False, 
                                          False, False, False, False, False, 
                                          True, False, False, False, False, 
                                          False]}, 
                            {'title': 'Aircraft and Passenger movements of Rockhampton 1986-2021'}]},
                   {'label': 'Melbourne', 
                   'method': 'update', 
                   'args': [{'visible': [False, False, False, False, False, 
                                          False, False, False, False, False, 
                                          False, False, False, False, False, 
                                        False, True, False, False, False, 
                                          False,
                                        False, False, False, False, False, 
                                          False, False, False, False, False, 
                                          False, False, False, False, False, 
                                        False, True, False, False, False, 
                                          False]}, 
                            {'title': 'Aircraft and Passenger movements of Melbourne Coast 1986-2021'}]},
                   {'label': 'Sydney', 
                   'method': 'update', 
                   'args': [{'visible': [False, False, False, False, False, 
                                          False, False, False, False, False, 
                                          False, False, False, False, False, 
                                        False, False, True, False, False, 
                                          False,
                                        False, False, False, False, False, 
                                          False, False, False, False, False, 
                                          False, False, False, False, False, 
                                        False, False, True, False, False, 
                                          False]}, 
                            {'title': 'Aircraft and Passenger movements of Sydney 1986-2021'}]},
                   {'label': 'Townsville', 
                   'method': 'update', 
                   'args': [{'visible': [False, False, False, False, False, 
                                          False, False, False, False, False, 
                                          False, False, False, False, False, 
                                        False, False, False, True, False, 
                                          False,
                                        False, False, False, False, False, 
                                          False, False, False, False, False, 
                                          False, False, False, False, False, 
                                        False, False, False, True, False, 
                                          False]}, 
                            {'title': 'Aircraft and Passenger movements of Townsville 1986-2021'}]},
                   {'label': 'Newcastle', 
                   'method': 'update', 
                   'args': [{'visible': [False, False, False, False, False, 
                                          False, False, False, False, False, 
                                          False, False, False, False, False, 
                                        False, False, False, False, True, 
                                          False,
                                        False, False, False, False, False, 
                                          False, False, False, False, False, 
                                          False, False, False, False, False, 
                                        False, False, False, False, True, 
                                          False]}, 
                            {'title': 'Aircraft and Passenger movements of Newcastle 1986-2021'}]},
                   {'label': 'Ayers Rock', 
                   'method': 'update', 
                   'args': [{'visible': [False, False, False, False, False, 
                                          False, False, False, False, False, 
                                          False, False, False, False, False, 
                                        False, False, False, False, False, 
                                          True,
                                        False, False, False, False, False, 
                                          False, False, False, False, False, 
                                          False, False, False, False, False, 
                                        False, False, False, False, False, 
                                          True]}, 
                            {'title': 'Aircraft and Passenger movements of Ayers Rock 1986-2021'}]}
                  ]



airports = ['ADELAIDE', 'ALICE SPRINGS', 'BALLINA', 'BRISBANE', 'CAIRNS', 'CANBERRA','DARWIN', 'GOLD COAST', 
            'HAMILTON ISLAND', 'HOBART', 'KARRATHA', 'LAUNCESTON', 'MACKAY', 'SUNSHINE COAST', 'PERTH', 
            'ROCKHAMPTON', 'MELBOURNE', 'SYDNEY', 'TOWNSVILLE', 'NEWCASTLE', 'AYERS ROCK']

fig2= go.Figure()
for airport in airports:
        fig2.add_trace(go.Scatter(x= df[df['AIRPORT'] == airport]['Pax_Total'],
                                 y= df[df['AIRPORT'] == airport]['Acm_Total'],
                                 mode= 'markers',
                                 name= airport,
                                  text= df[df['AIRPORT'] == airport]['Date']
                                ))
# Add trace voor alle vliegvelden in 2020 met andere kleur
df2020= df.query('Year == 2020')
for airport in airports:
    fig2.add_trace(go.Scatter(x= df2020[df2020['AIRPORT'] == airport]['Pax_Total'],
                              y= df2020[df2020['AIRPORT'] == airport]['Acm_Total'],
                              mode= 'markers',
                              name= str(airport)+ ' Corona',
                              text= df2020[df2020['AIRPORT'] == airport]['Date']))


fig2.update_layout(title_text="Passengers per air traffic movement",
            xaxis_title='Total number of passengers',
            yaxis_title='Air traffic movements', width=950, height=620,
            title={'x':0.5, 'xanchor':'center'})

fig2.update_layout({
    'updatemenus':[{'type': 'dropdown',
                    'x': 1.24, 'y': 1.1,
                    'showactive': False, 'active': 0,
                    'buttons': dropdown_buttons2
            }]})


st.write("""
In this scatterplot can be seen that the more passengers an airport receives, the more air traffic movements there are at that airport. 
An observation to pay attention to is that the plot shows a flattening as passenger numbers rise. The biggest airports where flattening of the line can be clearly seen, 
are Sydney, Melbourne, Brisbane and Perth. A reason for this can possibly be that these airports face a capacity limit.

Because of covid-19 the growth is not in line with the growth of the last 40 years, the data from 2020 is shown in a different colour when selecting an airport in the dropdown menu. For example, 
when examining the plot of Adelaide Airport, it can be seen that there is a major difference between March and April. 
Where in March 428,787 passengers arrived or departed from this airport, in April there were only 11,845 passengers. 
The following month, May, this number increased to 15,739 passengers. The months hereafter, growth of the amount of air traffic movements and passengers can be observed. 
This decrease and increase of the air traffic movements and passengers can also be observed for the other airports. 
To discover whether there is a relation between a faster recovery from this period and deploying domestic and/or international flights, the following bar plot is made.
""")
st.plotly_chart(fig2)

df_2020=df.query('Month ==12 & Year ==2020')
fig3 = go.Figure()

fig3.update_layout(yaxis_type="log")

fig3.add_trace(go.Bar(x=airports,
                y= df_2020.groupby('AIRPORT')['Int_Pax_Total'].sum() ,
                name='International passengers',
                marker_color='rgb(55, 83, 109)'
                ))
fig3.add_trace(go.Bar(x=airports,
                y= df_2020.groupby('AIRPORT')['Dom_Pax_Total'].sum() ,
                name ='Domestic passengers',
                marker_color='rgb(26, 118, 255)'
                ))

fig3.update_layout(title_text="Domestic and international passengers per airport in 2020",
            xaxis_tickfont_size=14,
            yaxis=dict(title='Total number of passengers', titlefont_size=16, tickfont_size=14,),
            legend=dict(x=0.75, y=1.0, bgcolor='rgba(255, 255, 255, 0)', bordercolor='rgba(255, 255, 255, 0)'),
            barmode='group',
            bargap=0.02,
            bargroupgap=0.05,
            width=950, height=620,
            title={'x':0.5, 'xanchor':'center'})


st.write("""
This barplot shows that the biggest airports mentioned above are international as well as domestic airports. 
To be precise, Sydney and Brisbane provide international as well as domestic flight, while Melbourne and Perth provide only domestic flights. 
Good to know is that this plot has a logarithmic y axis to see the difference between the number of passengers, otherwise, the number of passengers at the other airports would not have been visible due to the large number of passengers at Brisbane airport.
""")

st.plotly_chart(fig3)



#chapter 4
st.subheader('4. Forecasting Until 2030')
st.write("""

""")


All= df.query('AIRPORT == "All Australian Airports" & Year < 2020')

#pax graph
fig5 = px.scatter(data_frame= All, x='Date', y= 'Pax_Total', trendline='lowess', trendline_options=dict(frac=0.01), trendline_color_override='red', range_x=['1985-01-01','2030-01-01'])

fig5.update_layout(title_text="Total number of passengers over the years",
            xaxis_title='Year',
            yaxis_title='Total number of passengers', width=950, height=620,
            title={'x':0.5, 'xanchor':'center'})

#acm graph
fig6 = px.scatter(data_frame= All, x= 'Date', y= 'Acm_Total', trendline='lowess', trendline_options=dict(frac=0.01), trendline_color_override='red')

fig6.update_layout(title_text="Total number of acm over the years",
            xaxis_title='Year',
            yaxis_title='Total number of acm', width=950, height=620,
            title={'x':0.5, 'xanchor':'center'})


        
option = st.radio('Select a graph:',
                 ['Total number of passengers over the years','Total number of acm over the years'])


if option=='Total number of passengers over the years':
            my_bar = st.progress(0)
            for percent_complete in range(100):
                        time.sleep(0.1)
                        my_bar.progress(percent_complete +1)
            st.balloons()
            st.plotly_chart(fig5)
elif option=='Total number of acm over the years':
            my_bar = st.progress(0)
            for percent_complete in range(100):
                        time.sleep(0.1)
                        my_bar.progress(percent_complete +1)
            st.balloons()
            st.plotly_chart(fig6)
            
#chapter 5
st.subheader('5. Conclusion')
st.write("""

""")



app = dash.Dash(__name__)

app.layout = html.Div([

    html.Div([
        dcc.Graph(id='Year_graph')
    ]),

    html.Div([
        html.Label(['Total Pax per year 1985-2020'],
                    style={'font-weight': 'bold'}),
        html.P(),
        dcc.RangeSlider(
            id='year-range-slider', # Naam toekennen aan slider
            marks={
                1985: '1985',     # key=Positie, value= Wat er zichtbaar is
                1990: '1990',
                1995: '1995',
                2000: '2000',
                2005: '2005',
                2010: '2010',
                2015: '2015',
                2020: {'label': '2020', 'style': {'color':'orange', 'font-weight':'bold'}},
            },
            step=1,                # aantal stappen tussen de jaartallen
            min=1985,
            max=2020,
            value=[2000,2015],     # Begin- en eindwaarde van de slider
            dots=True,             # True of False. Voegt wel of geen puntjes toe tussen de jaartallen 
            allowCross=False,      # True of False - Optie om met de linker hendel over de rechter hendel heen te gaan 
            disabled=False,        # True of False - Optie om de slider te bevriezen voor andere gebruikers
            pushable=1,            # Optie om altijd een x aantal jaren zichtbaar te hebben. =1 is altijd 1 jaar zichtbaar.
            updatemode='mouseup',  # 'mouseup' of 'drag' - Optie om de grafiek realtime te update of pas als de muisknop is losgelaten.
            included=True,         # True of False - Optie om de balk tussen de jaartallen ook zichtbaar te maken of niet 
            vertical=False,        # True of False - Horizontale (True) of Verticale (False) weergave van de slider
            verticalHeight=900,    # Hoogte van de slider in pixels als slider horizontaal wordt weergegeven.
            tooltip={'always visible':True,  # Optie om het huidige jaartal wel/niet weer te geven in de slider 
                     'placement':'bottom'},   # Positie van het jaartal 
            ),
    ]),

])

@app.callback(
    Output('Year_graph','figure'),
    [Input('year-range-slider','value')]
)

def add_slider(years_chosen):

    dff = df[(df['Year']>=years_chosen[0])&(df['Year']<=years_chosen[1])]
    dff = dff[(dff['Month']==12)]
    dff = dff[(dff['AIRPORT']=='SYDNEY') | (dff['AIRPORT']=='MELBOURNE')]

    fig = px.bar(
                        data_frame=dff,
                        x="Year",
                        y="Pax_Total_Year",
                        color="AIRPORT",               
                        opacity=0.9,                  
                        orientation="v",              
                        barmode='group',
                        text='Pax_Total_Year',
                        labels={"Pax_Total_Year":"Total Pax per Year",
                        "AIRPORT":"Airport"},           
                        title='Total Pax per year 1985-2020', 
                        width=1400,                   
                        height=720,                   
                        template='ggplot2',                                             
)
    fig.update_traces(texttemplate='%{text:.3s}', textposition='outside')
    fig.update_layout(uniformtext_minsize=8)
                           
    return (fig)


if __name__ == '__main__':
    app.run_server(debug=False)

@app.callback(Output('graph', 'figure'),
              [Input('Pax_Dom_Int', 'value'),
               Input('Acm_Dom_Int', 'value')])

def update_figure(Pax_Dom_Int,Acm_Dom_Int):
    dff = df[(df[['Dom_Pax_Total', 'Int_Pax_Total']].isin(Pax_Dom_Int)) &
                (df[['Dom_Acm_Total', 'Int_Acm_Total']].isin(Acm_Dom_Int))]

    # Create figure
    fig7 = px.scatter(
                        data_frame=dff,
                        color="AIRPORT",               
                        opacity=0.9,                  
                        orientation="v",              
                        barmode='group',
                        text='Pax_Total_Year',
                        labels={"Pax_Total_Year":"Total Pax per Year",
                        "AIRPORT":"Airport"},           
                        title='Total Pax per year 1985-2020', 
                        width=1400,                   
                        height=720,                   
                        template='ggplot2',                                             
)
    return fig7

if __name__ == '__main__':
    
    app.run_server(debug=False)

st.plotly_chart(fig7)












'''  
my_bar = st.progress(0)
for percent_complete in range(100):
  time.sleep(0.1)
  my_bar.progress(percent_complete +1)

st.balloons()
'''

