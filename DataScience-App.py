import streamlit as st
import numpy as np
import pandas as pd
import requests
import json
import plotly.express as px
import plotly.graph_objects as go
import time

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
All these flights move an estimated 6 million passengers. 
Most of the time, air travel is preferred for long distances or for fast travel times. 
Surely, a large country such as Australia must have a large number of daily flights. 
The long distances, makes domestic flights a very suitable mode of transport, but how many flights are there? 
and what is the estimated number of flights in 2030? This is important since, air transportation is at the heart of the Australian economic growth. 
So a strong aviation industry is important for the Australian government as well as Australian citizens


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
st.write("""

""")
dropdown_buttons2= [{'label': 'All', 
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
# fig 2 pax vs acm
airports = ['ADELAIDE', 'ALICE SPRINGS', 'BALLINA', 'BRISBANE', 'CAIRNS', 'CANBERRA','DARWIN', 'GOLD COAST', 
            'HAMILTON ISLAND', 'HOBART', 'KARRATHA', 'LAUNCESTON', 'MACKAY', 'MELBOURNE', 'PERTH', 
            'ROCKHAMPTON', 'SUNSHINE COAST', 'SYDNEY', 'TOWNSVILLE', 'NEWCASTLE', 'AYERS ROCK']
fig2= go.Figure()
for airport in airports:
        fig2.add_trace(go.Scatter(x= df[df['AIRPORT'] == airport]['Pax_Total'],
                                 y= df[df['AIRPORT'] == airport]['Acm_Total'],
                                 mode= 'markers',
                                 name= airport,
                                  text= df[df['AIRPORT'] == airport]['Date']
                                ))

fig2.update_layout(title_text="Passengers per air traffic movement",
            xaxis_title='Total number of passengers',
            yaxis_title='Air traffic movements', width=950, height=620,
            title={'x':0.5, 'xanchor':'center'})

fig2.update_layout({
    'updatemenus':[{'type': 'dropdown',
                    'x': 1.24, 'y': 1.1,
                    'showactive': True, 'active': 0,
                    'buttons': dropdown_buttons2
            }]})
st.plotly_chart(fig2)

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

# fig pax growth
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

st.plotly_chart(fig)



#fig 3 dom vs int pax
df_month12=df.query('Month ==12')

fig3 = go.Figure()
fig3.update_layout(yaxis_type="log")
fig3.add_trace(go.Bar(x=airports,
                y= df_month12.groupby('AIRPORT')['Int_Pax_Total'].sum() ,
                name='International passengers',
                marker_color='rgb(55, 83, 109)'
                ))
fig3.add_trace(go.Bar(x=airports,
                y= df_month12.groupby('AIRPORT')['Dom_Pax_Total'].sum() ,
                name ='Domestic passengers',
                marker_color='rgb(26, 118, 255)'))

fig3.update_layout(title_text="Domestic and international passengers per airport",
            xaxis_tickfont_size=14,
            yaxis=dict(title='Total number of passengers', titlefont_size=16, tickfont_size=14,),
            legend=dict(x=0.7, y=1.0, bgcolor='rgba(255, 255, 255, 0)', bordercolor='rgba(255, 255, 255, 0)'),
            barmode='group',
            bargap=0.02,
            bargroupgap=0.05,
            width=950, height=620,
            title={'x':0.5, 'xanchor':'center'})

st.plotly_chart(fig3)



#chapter 4
st.subheader('4. Forecasting Until 2030')
st.write("""

""")


#chapter 5
st.subheader('5. Conclusion')
st.write("""

""")






'''  
my_bar = st.progress(0)
for percent_complete in range(100):
  time.sleep(0.1)
  my_bar.progress(percent_complete +1)

st.balloons()
'''

