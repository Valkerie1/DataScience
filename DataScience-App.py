import streamlit as st
import numpy as np
import pandas as pd
import requests
import json
import plotly.express as px
import plotly.graph_objects as go

st.title('Australian passenger information')

if st.button('Retrieve passenger data'):
    ##  Passenger info
    #eerste call naar API
    url = 'https://data.gov.au/data/api/3/action/datastore_search?&resource_id=38bdc971-cb22-4894-b19a-814afc4e8164'
    r=requests.get(url)
    datatxt= r.text
    datajs = json.loads(datatxt)
    length = datajs['result']['total']-1
    itterations = round(length/100)

    #haal data op voor de 1e keer
    datalist = []
    offset =0
    i = 0

    while i != (itterations/2)-1:
        url = 'https://data.gov.au/data/api/3/action/datastore_search?offset=' + str(offset) + '&resource_id=38bdc971-cb22-4894-b19a-814afc4e8164'
        
        r=requests.get(url)
        datatxt= r.text
        datajs = json.loads(datatxt)
        datalist.append(datajs['result']['records'])
    
        offset=offset+100
        i = i+1
        print(datalist)
        print(i)
        
    listtemp = [x for l in datalist for x in l]
    part1 = pd.DataFrame(listtemp)
    
    #haal data op voor de 2e keer    
    datalist = []

    while i != itterations:
        url = 'https://data.gov.au/data/api/3/action/datastore_search?offset=' + str(offset) + '&resource_id=38bdc971-cb22-4894-b19a-814afc4e8164'
       
        r=requests.get(url)
        datatxt= r.text
        datajs = json.loads(datatxt)
        datalist.append(datajs['result']['records'])
    
    
        offset=offset+100
        i = i+1
        print(datalist)
        print(i)
        

    listtemp = [x for l in datalist for x in l]
    part2 = pd.DataFrame(listtemp)

    #voeg de data samen voor de passengers
    passengers = part1.append(part2)
    
    ##  Aircraft info
    #eerste call naar API
    url = 'https://data.gov.au/data/api/3/action/datastore_search?resource_id=583be26d-59b9-4bcc-827d-4d9f7162fb04'
    r=requests.get(url)
    datatxt= r.text
    datajs = json.loads(datatxt)
    length = datajs['result']['total']-1
    itterations = round(length/100)

    #haal data op voor de 1e keer
    datalist = []
    offset =0
    i = 0

    while i != (itterations/2)-1:
        url = 'https://data.gov.au/data/api/3/action/datastore_search?offset=' + str(offset) + '&resource_id=583be26d-59b9-4bcc-827d-4d9f7162fb04'
        
        r=requests.get(url)
        datatxt= r.text
        datajs = json.loads(datatxt)
        datalist.append(datajs['result']['records'])
    
        print(datalist)
        print(i)
        offset=offset+100
        i = i+1
    listtemp = [x for l in datalist for x in l]
    part1 = pd.DataFrame(listtemp)
    
    #haal data op voor de 2e keer    
    datalist = []

    while i != itterations:
        url = 'https://data.gov.au/data/api/3/action/datastore_search?offset=' + str(offset) + '&resource_id=583be26d-59b9-4bcc-827d-4d9f7162fb04'
       
        r=requests.get(url)
        datatxt= r.text
        datajs = json.loads(datatxt)
        datalist.append(datajs['result']['records'])
    
    
        print(datalist)
        print(i)
        offset=offset+100
        i = i+1

    listtemp = [x for l in datalist for x in l]
    part2 = pd.DataFrame(listtemp)

    #voeg de data samen voor de passengers
    aircraft = part1.append(part2)
    
    st.dataframe(passengers)
    st.dataframe(aircraft)
    
    
'''    
##  Data prepratie
#df= passengers.merge(aircraft, on= ['AIRPORT', 'Year', 'Month'])
#df["Pax_Total_Year"]= df.groupby(["AIRPORT", "Year"])["Pax_Total"].transform('cumsum')
#df["Acm_Total_Year"]= df.groupby(["AIRPORT", "Year"])["Acm_Total"].transform('cumsum')

st.dataframe(passengers)
st.dataframe(aircraft)

st.dataframe(df)

#st.plotly_chart(fig)
'''
