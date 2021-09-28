import streamlit as st
import numpy as np
import pandas as pd
import requests
import json
import plotly.express as px
import plotly.graph_objects as go

st.title('Australian passenger information')

url1= 'https://data.gov.au/data/dataset/cc5d888f-5850-47f3-815d-08289b22f5a8/resource/38bdc971-cb22-4894-b19a-814afc4e8164/download/mon_pax_web.csv'  
url2= 'https://data.gov.au/data/dataset/cc5d888f-5850-47f3-815d-08289b22f5a8/resource/583be26d-59b9-4bcc-827d-4d9f7162fb04/download/mon_acm_web.csv'
passengers= pd.read_csv(url1)
aircraft= pd.read_csv(url2)

df= passengers.merge(aircraft, on= ['AIRPORT', 'Year', 'Month'])
df["Pax_Total_Year"]= df.groupby(["AIRPORT", "Year"])["Pax_Total"].transform('cumsum')
df["Acm_Total_Year"]= df.groupby(["AIRPORT", "Year"])["Acm_Total"].transform('cumsum')

st.dataframe(df)
