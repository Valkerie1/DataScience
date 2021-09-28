import streamlit as st
import numpy as np
import pandas as pd
import requests
import json
import plotly.express as px
import plotly.graph_objects as go

st.title('Australian passenger information')

url = 'https://data.gov.au/data/api/3/action/datastore_search?&resource_id=38bdc971-cb22-4894-b19a-814afc4e8164'
r=requests.get(url)
datatxt= r.text
datajs = json.loads(datatxt)
datalist = datajs['result']['records']
df = pd.DataFrame(datalist)

cols=['Year','Month']
df['Date'] = df[cols].apply(lambda x: '-'.join(x.values.astype(str)), axis='columns')
df['Date'] = pd.to_datetime(df['Date'])

time_data = pd.DataFrame(df.groupby(['Date'])['Pax_Total'].sum())   #time_data = pd.DataFrame(df.groupby(['Date'])[['Pax_Total','Acm_Total']].sum())

time_buttons = [{'count': 37, 'step':'year', 'stepmode':'todate', 'label':'All'},
              {'count': 6, 'step':'month', 'stepmode':'backward', 'label':'6MTH'}, 
              {'count': 1, 'step':'year', 'stepmode':'backward', 'label':'1YR'},
              {'count': 5, 'step':'year', 'stepmode':'backward', 'label':'5YR'},
              {'count': 10, 'step':'year', 'stepmode':'backward', 'label':'10YR'},
              {'count': 20, 'step':'year', 'stepmode':'backward', 'label':'20YR'}]

fig = px.bar(data_frame=time_data, x=time_data.index, y='Pax_Total')

fig.update_layout({'xaxis':{'rangeselector':{'buttons':time_buttons}}})
fig.update_xaxes(title_text='Date')
fig.update_yaxes(title_text='Total number of passengers in millions')

st.plotly_chart(fig)
