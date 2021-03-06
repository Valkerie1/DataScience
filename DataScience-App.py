import streamlit as st
import numpy as np
import pandas as pd
import requests
import json
import plotly.express as px
import plotly.graph_objects as go
import time


st.title('Impact of COVID-19 on Australian Air Traffic')

#chapter 1
st.subheader('1. Introduction')
st.write("""
Getting up early to catch a flight? I am sure that sounds familiar to you, whether it is for an important meeting or just for your relaxing holiday on the other side of the world.

It is estimated that there are roughly 100.000 flights per day all around the world. All these flights move an estimated 6 million passengers. Usually, air travel is preferred for long distances. That is why it is more than logical that such a large country as Australia has a large number of domestic flights daily. Besides, a lot of international flights are deployed daily due to its beautiful nature and tourist hotspots. This has completely collapsed due to the COVID-19 pandemic. How is the Australian aviation industry going to recover from this? Since, air transportation is at the heart of the Australian economic growth, a fast recovery of the aviation industry is crucial.
""")

#chapter 2
st.subheader('2. Resources')
st.write("""
The data comes from the Australian government, so the code below retrieves the data from the API. However, every get call to retrieve the data retrieves 100 rows of data.
To retrieve the next 100 rows, an offset has to be applied in the url. The code below uses a while loop to automatically apply the offset in the url for every itteration.
In each itteration, 100 rows are retrieved and stored in a list named 'datalist'.
However, there is a data limit on the API, so it was not possible to fetch all the data, therefore a CSV file was used to load the data.


    offset =0
    i = 0
    url = 'https://data.gov.au/data/api/3/action/datastore_search?offset=' + str(offset) + '&resource_id=38bdc971-cb22-4894-b19a-814afc4e8164'
    r=requests.get(url)
    datatxt= r.text
    datajs = json.loads(datatxt)
    print(datajs)
    
    datalist = []
    
    while i != 9200: # the API contains 9198 rows in total
        url = 'https://data.gov.au/data/api/3/action/datastore_search?offset=' + str(offset) + '&resource_id=38bdc971-cb22-4894-b19a-814afc4e8164'
        
        r=requests.get(url)
        datatxt= r.text
        datajs = json.loads(datatxt)
        datalist.append(datajs['result']['records'])
    
        print(datalist)
        print(i)
        offset=offset+100
        i = i+100
    
    listtemp = [x for l in datalist for x in l]
    df = pd.DataFrame(listtemp)

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
            y= df_month12[df_month12['AIRPORT'] == airport]['Pax_Total_Year'],
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
As can be seen in the line chart below, 'Passenger growth Australian airport', over the years the amount of passengers has grown tremendously. 
The front runners are obviously the country's largest cities, Sydney, Melbourne, Brisbane and Perth. Besides, a huge crash can be observed in 2020. 
This crash is caused by the COVID-19 pandemic. 
During this period of upheaval and uncertainty the borders of Australia were closed. However, the plot shows that in this year the airports still receive passengers, 
just not as much as previous years. To see in which months COVID-19 had an influence on the growth, the 'Passengers per aircraft movement' scatterplot has been made.

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


fig2.update_layout(title_text="Passengers per aircraft movement",
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
In the scatterplot, 'Passengers per aircraft movement', can be seen that the more passengers an airport receives, the more aircraft movements (acm) there are at that airport. 
An observation to pay attention to is that the plot shows a flattening as passenger numbers rise. The biggest airports where flattening of the line can be clearly seen, 
are Sydney, Melbourne, Brisbane and Perth. A reason for this can possibly be that these airports face a capacity limit.

Because of COVID-19 the growth is not in line with the growth of the last 40 years, the data from 2020 is shown in a different colour when selecting an airport in the dropdown menu. For example, 
when examining the plot of Adelaide Airport, it can be seen that there is a major difference between March and April. 
Where in March 428,787 passengers arrived or departed from this airport, in April there were only 11,845 passengers. 
The following month, May, this number increased to 15,739 passengers. The months hereafter, growth of the amount of acm and passengers can be observed. 
This decrease and increase of the acm and passengers can also be observed for the other airports. 
To discover whether there is a relation between a faster recovery from this period and deploying domestic and/or international flights, the following bar plot is made.
""")
st.plotly_chart(fig2)

st.write("""
The bar plot 'Domestic and international passengers per airport in 2020' shows which airports deployed international flights and/or domestic flights in 2020. Out of the 5 biggest airports, Sydney deployed only domestic flights, while Melbourne, Brisbane, Perth and Adelaide provided both types of flights. In total, 8 out of 21 biggest airports of Australia deployed during this period international and domestic flights. Although the borders were closed for a period of time, the international flights are repatriation flights.

Good to mention is that this plot has a logarithmic y axis. This way the data over a very wide range of values is displayed in a compact way. So, keep in mind that the largest numbers in the data are thousands of times larger than the smallest numbers.

The total number of domestic flights in 2020 was mainly realized in the 2nd half of 2020. In the months of April, May and June the provincial borders in Australia were also closed for a while, this is clearly visible in the above scatterplot 'Passengers per aircraft movement', meaning that the points for the relevant months are located at the bottom left of the plot for all airports.
""")
df_2020=df.query('Month ==12 & Year ==2020')

pax= ["All", "Domestic", "International"]
slider= st.select_slider("Choose Passenger Type to display",
                options= pax)
if slider == "All":
    fig3= go.Figure()
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
    st.plotly_chart(fig3)

elif slider == "Domestic":
    fig3= go.Figure()
    fig3.update_layout(yaxis_type="log")
    fig3.add_trace(go.Bar(x=airports,
                          y= df_2020.groupby('AIRPORT')['Dom_Pax_Total'].sum() ,
                          name ='Domestic passengers',
                          marker_color='rgb(26, 118, 255)'
                         ))
    fig3.update_layout(title_text="Domestic passengers per airport in 2020",
                       xaxis_tickfont_size=14,
                       yaxis=dict(title='Total number of passengers', titlefont_size=16, tickfont_size=14,),
                       legend=dict(x=0.75, y=1.0, bgcolor='rgba(255, 255, 255, 0)', bordercolor='rgba(255, 255, 255, 0)'),
                       barmode='group',
                       bargap=0.02,
                       bargroupgap=0.05,
                       width=950, height=620,
                       title={'x':0.5, 'xanchor':'center'})
    st.plotly_chart(fig3)
elif slider == "International":
    fig3= go.Figure()
    fig3.update_layout(yaxis_type="log")
    fig3.add_trace(go.Bar(x=airports,
                          y= df_2020.groupby('AIRPORT')['Int_Pax_Total'].sum() ,
                          name ='International passengers',
                          marker_color='rgb(26, 118, 255)'
                         ))
    fig3.update_layout(title_text="International passengers per airport in 2020",
                       xaxis_tickfont_size=14,
                       yaxis=dict(title='Total number of passengers', titlefont_size=16, tickfont_size=14,),
                       legend=dict(x=0.75, y=1.0, bgcolor='rgba(255, 255, 255, 0)', bordercolor='rgba(255, 255, 255, 0)'),
                       barmode='group',
                       bargap=0.02,
                       bargroupgap=0.05,
                       width=950, height=620,
                       title={'x':0.5, 'xanchor':'center'})
    st.plotly_chart(fig3)








#chapter 4
st.subheader('4. Forecasting the recovery')
st.write("""
The plot below, 'Total number of passengers over the years', shows the total number of passengers over the years. When selecting ???total number of acm over the years??? in the checkbox, this can be viewed too. Both plots show a dip in 1989. This was caused by the Australian pilots??? dispute. All of Australia's 1,645 domestic airline pilots resign over an airline's move to dismiss and sue them over a wage dispute. The dispute severely disrupted domestic air travel in Australia and had a major detrimental impact on the tourism industry. Hence, the dip in this plot. 

Another observation is that over the years there are more fluctuations. Where air transport was first something for the elite, over the years it has become more and more accessible to the general population. These passengers react more strongly to seasonal changes, hence the increase of fluctuations. 

The thing that stands out most in this plot is the dip of 2020. Although COVID-19 created an immense crash, it can be seen that the number of passengers pick up quickly between April 2020 and April 2021. In this period, Australia had reached a point where no COVID-19 cases had been reported. Hereafter, new COVID-19 cases were reported and Australia had announced a second lockdown, which caused another dip can be seen, which is caused by Australia???s second lockdown.
""")


All= df.query('AIRPORT == "All Australian Airports" & Year < 2022')

option = st.radio('Select a graph to display:',
                 ['Total number of passengers over the years','Total number of acm over the years'])


if option=='Total number of passengers over the years':
            #my_bar = st.progress(0)
            #for percent_complete in range(100):
            #            time.sleep(0.1)
            #            my_bar.progress(percent_complete +1)
            #st.balloons()
            fig5 = px.scatter(data_frame= All, x='Date', y= 'Pax_Total', trendline='lowess', trendline_options=dict(frac=0.01), trendline_color_override='red')

            fig5.update_layout(title_text="Total number of passengers over the years",
                        xaxis_title='Year',
                        yaxis_title='Total number of passengers', width=950, height=620,
                        title={'x':0.5, 'xanchor':'center'})
            st.plotly_chart(fig5)
elif option=='Total number of acm over the years':
            #my_bar = st.progress(0)
            #for percent_complete in range(100):
            #            time.sleep(0.1)
            #            my_bar.progress(percent_complete +1)
            #st.balloons()
            fig6 = px.scatter(data_frame= All, x= 'Date', y= 'Acm_Total', trendline='lowess', trendline_options=dict(frac=0.01), trendline_color_override='red')

            fig6.update_layout(title_text="Total number of aircraft movements over the years",
                        xaxis_title='Year',
                        yaxis_title='Total number of aircraft movements', width=950, height=620,
                        title={'x':0.5, 'xanchor':'center'})
            st.plotly_chart(fig6)
            

#chapter 5
st.subheader('5. Conclusion')
st.write("""
In chapter 3, the passenger growth has been plotted from 1985 until 2020 for the top 21 Australian airports. This plot showed an increase of passenger numbers of the years, however the number of passengers decreased massivly in 2020.
This drop in passenger number is caused by COVID-19. Both the acm as well as the passenger numbers decreased massively. A barplot was made to show the number of passengers from domestic and international flights in 2020.
The result showed that only 8 of the top 21 airports provided international flights. Although the borders were closed for a period of time. These international flights are repatriation flights.

In chapter 4, the number of passengers and acm were plotted over the years. Due to the strong lockdown policy in Australia, the number of passengers and acm droped massively, however it can be seen that the number of passengers and acm will quickly recover as soon as the borders are opened for passengers from all around the world. 
As soon as the borders are opened for everyone, it is expected that the number of passengers will be back add the same level as in 2019 within a couple of years. 

""")

easteregg = st.radio('Finished?', 
                            ['No','Yes!'])
if easteregg=='Yes!':
            st.balloons()


st.sidebar.write("""
Made by:  

- Jelle Aardema

- Majdouline A??t Ali

- Maarten Meeuwes

- Robin Pelders
""")










