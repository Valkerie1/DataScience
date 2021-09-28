import streamlit as st
import numpy as np
import pandas as pd
import requests
import json

st.title('Australian passenger information')

url = 'https://data.gov.au/data/api/3/action/datastore_search?&resource_id=38bdc971-cb22-4894-b19a-814afc4e8164'
r=requests.get(url)
datatxt= r.text
datajs = json.loads(datatxt)
datalist = datajs['result']['records']
df = pd.DataFrame(datalist)

st.dataframe(df)
