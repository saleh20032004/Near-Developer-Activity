# Libraries
import streamlit as st
from PIL import Image
import pandas as pd
import plotly.express as px
import numpy as np
# Layout

st.set_page_config(page_title='Developer Activity in 2022 on NEAR Protocol', page_icon=':bar_chart:', layout='wide')
st.title('Contracts section')

#CSS
with open('style.css')as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html = True)

@st.cache(ttl=1)
def get_data(query):
    if query == 'contracts':
        return pd.read_json('https://node-api.flipsidecrypto.com/api/v2/queries/717e3c45-2334-49fe-bbb4-7185f06570bc/data/latest')
    # elif query == 'users_type_date':
    #     return pd.read_json('https://node-api.flipsidecrypto.com/api/v2/queries/cdef12a7-08bf-4356-83ca-d6b8fea0b5f6/data/latest')
    # elif query == 'test':
    #     return pd.read_json('https://node-api.flipsidecrypto.com/api/v2/queries/4b9fa244-4679-4fe7-9fda-55cb3fedb140/data/latest')
    # elif query == 'Transactions Fee Payers':
    #     return pd.read_json('https://node-api.flipsidecrypto.com/api/v2/queries/7eae69ea-2387-420d-b4b9-6eceeb5ef22d/data/latest')
    return None

#Get Data
contracts = get_data('contracts')

theme_plotly = None # None or streamlit


fig = px.bar(contracts, x='DATE', y='CONTRACTS', title='The number of contracts in 2022 on a weekly basis')
fig.update_layout(showlegend=True, xaxis_title=None, yaxis_title='Contracts', xaxis={'categoryorder':'total ascending'})
st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)

fig = px.line(contracts, x='DATE', y='GRWOTH_CONTRATS', title='The growth of the number of appointments in 2022 on a weekly basis')
fig.update_layout(showlegend=True, xaxis_title=None, yaxis_title='Contracts', xaxis={'categoryorder':'total ascending'})
st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)
st.info("The highest number of contracts was created on July 18, 2022, and we see many appointments on March 28, but after July, the number of contracts decreased.")


 
