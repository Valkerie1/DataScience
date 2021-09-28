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
Flying, almost everyone has done it. Flying ensures a fast connection to the other side of the world for that important meeting, or just a relaxed flight to the holiday destination.
It is estimated that there are roughly 100.000 flights per day all around the world. All these flights move an estimated 6 million passengers. Most of the time, air travel is preferred for long distances or for fast travel times.
Surely, a large country such as Australia must have a large number of daily flights. The long distances, makes domestic flights a very suitable mode of transport, but how many flights are there? and what is the estimated number of flights in 2030?
This is important since, air transportation is at the heart of the Australian economic growth. So a strong aviation industry is important for the Australian government as well as Australian citizens

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
# Add traces voor ieder vliegveld en totaal
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
# Add trace voor alle vliegvelden in 2020 met andere kleur
df2020= df.query('AIRPORT== "All Australian Airports" & Year == 2020')
airport = 'All Australian Airports'
fig2.add_trace(go.Scatter(x= df2020['Pax_Total'],
                         y= df2020['Acm_Total'],
                         mode= 'markers',
                          name= "Corona",
                         text= df2020[df2020['AIRPORT'] == 'All Australian Airports']['Date']))
st.plotly_chart(fig2)

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

'''
url1= 'https://data.gov.au/data/dataset/cc5d888f-5850-47f3-815d-08289b22f5a8/resource/38bdc971-cb22-4894-b19a-814afc4e8164/download/mon_pax_web.csv'  
url2= 'https://data.gov.au/data/dataset/cc5d888f-5850-47f3-815d-08289b22f5a8/resource/583be26d-59b9-4bcc-827d-4d9f7162fb04/download/mon_acm_web.csv'
passengers= pd.read_csv(url1)
aircraft= pd.read_csv(url2)

df= passengers.merge(aircraft, on= ['AIRPORT', 'Year', 'Month'])
df["Pax_Total_Year"]= df.groupby(["AIRPORT", "Year"])["Pax_Total"].transform('cumsum')
df["Acm_Total_Year"]= df.groupby(["AIRPORT", "Year"])["Acm_Total"].transform('cumsum')

st.subheader('Vliegvelden zonder vliegtuig bewegingen')
st.dataframe(df.query('Acm_Total == 0'))

df_new = df.drop(df[(df.AIRPORT == 'BALLINA') & (df.Acm_Total == 0)].index, inplace= True)

st.subheader('Verhouding tussen passagiers en vliegbewegingen')
fig= px.scatter(data_frame= df, title= 'Plot',
               x= 'Pax_Total',
               y= 'Acm_Total',
               color= 'AIRPORT')
st.plotly_chart(fig)
'''
