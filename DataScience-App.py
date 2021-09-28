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
- 3. Passenger numbers
- 4. Air traffic movements
- 5. Forecasting until 2030
- 6. Conclusion



""")

st.subheader('1. Introduction')
st.write("""
Vliegen, bijna iedereen heeft het wel eens gedaan. Het zorgt voor een snelle verbinding naar die belangrijke vergadering, of een relaxte reis naar je vakantie bestemming.
Dagelijks vliegen er meer dan 100.000 vliegtuigen over de hele wereld. Deze vervoeren een geschatte 6 miljoen passagiers per dag.
Australië is veruit het grootste land in Oceanië en een van de grootste landen ter wereld. Door de grootte zouden er dan veel vluchten moeten zijn in Australië, maar hoeveel vluchten zijn er?
En hoeveel vluchten zijn er in 2030 verwacht?

Flying, almost everyone has done it. Flying ensures a fast connection to the other side of the world for that import meeting, or just a relaxed flight to the holiday destination.
It is estimated that there are roughly 100.000 flights per day all around the world. All these flights move an estimated 6 million passengers. Most of the time, air travel is preferred for long distances or for fast travel times.
Surely, a large country such as Australia must have a large number of daily flights. The long distances, makes domestic flights a very suitable mode of transport, but how many flights are there? and what is the estimated number of flights in 2030?
This is important since, air transportation is at the heart of the Australian economic growth. So a strong aviation industry is important for the Australian government as well as Australian citizens

""")
st.subheader('2. Australian airports')
st.write("""

""")
st.subheader('3. Passenger numbers')
st.write("""

""")
st.subheader('4. Air traffic movements')
st.write("""

""")
st.subheader('5. Forecasting until 2030')
st.write("""

""")
st.subheader('6. Conclusion')
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
