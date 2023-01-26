# Libraries
import streamlit as st
from PIL import Image
import pandas as pd
import plotly.express as px
# Layout

st.set_page_config(page_title='Developer Activity in 2022 on NEAR Protocol', page_icon=':bar_chart:', layout='wide')
st.title('Developer activity')

#CSS
with open('style.css')as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html = True)

@st.cache(ttl=1)
def get_data(query):
    if query == 'Top Open PR':
        return pd.read_json('https://node-api.flipsidecrypto.com/api/v2/queries/4877ed5c-f392-4c30-b987-6bd0e3f9d783/data/latest')
    elif query == 'Top Close PR':
        return pd.read_json('https://node-api.flipsidecrypto.com/api/v2/queries/76e9f3ce-8ffc-4f63-b752-ab341e14b1e9/data/latest')
    # elif query == 'test':
    #     return pd.read_json('https://node-api.flipsidecrypto.com/api/v2/queries/4b9fa244-4679-4fe7-9fda-55cb3fedb140/data/latest')
    # elif query == 'Transactions Fee Payers':
    #     return pd.read_json('https://node-api.flipsidecrypto.com/api/v2/queries/7eae69ea-2387-420d-b4b9-6eceeb5ef22d/data/latest')
    return None

#Get Data
Top_Open_PR = get_data('Top Open PR')
Top_Close_PR = get_data('Top Close PR')

theme_plotly = None # None or streamlit

# st.table(Top_Open_PR)
c1,c2 = st.columns(2)
with c1:
    st.info('Developer Activity - Top Open PR')
    st.table(Top_Open_PR)
with c2:
    st.info('Developer Activity - Top Close PR')
    st.table(Top_Close_PR)


