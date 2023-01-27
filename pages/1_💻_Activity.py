# Libraries
import streamlit as st
from PIL import Image
import pandas as pd
import plotly.express as px
# Layout
st.set_page_config(page_title='Developer Activity in 2022 on NEAR Protocol', page_icon=':bar_chart:', layout='wide')
st.title('Developer Activity')

#CSS
with open('style.css')as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html = True)

@st.cache(ttl=1)
def get_data(query):
    if query == 'Total Value':
        return pd.read_json('https://node-api.flipsidecrypto.com/api/v2/queries/6bed72f3-f508-494e-94c4-1c975f674786/data/latest')
    elif query == 'users type':
        return pd.read_json('https://node-api.flipsidecrypto.com/api/v2/queries/4b9fa244-4679-4fe7-9fda-55cb3fedb140/data/latest')
    elif query == 'test':
        return pd.read_json('')
    elif query == 'Transactions Fee Payers':
        return pd.read_json('')
    return None


#Get Data
total_value = get_data('Total Value')
users_type = get_data('users type')




theme_plotly = None # None or streamlit

c1,c2,c3,c4 = st.columns(4)
with c1:
    st.metric(label="Total number of activities",value=total_value['TOTAL'])
with c2:
    st.metric(label="Total number of opens",value=total_value['OPEN'])
with c3:
    st.metric(label="Total number of merges",value=total_value['MERGED'])
with c4:
    st.metric(label="Total number of closes",value=total_value['CLOSED'])
c1,c2,c3,c4 = st.columns(4)
with c1:
    st.metric(label="Average activity per day",value=total_value['AVG_ACTIVITY'])
with c2:
    st.metric(label="Total number of projects worked on",value=total_value['PROJECTS'])
with c3:
    st.metric(label="Total number of contributors",help='CONTRIBUTOR,OWNER,COLLABORATOR,MEMBER,FIRST_TIME_CONTRIBUTOR',value=total_value['USERS'])
with c4:
    st.metric(label="Average contributors per day",value=total_value['AVG_USERS'])

c1,c2 =st.columns(2)
with c1:
    
    fig = px.pie(users_type, values='AUTHORS', names='AUTHORASSOCIATION', title='The number of authors in 2022 based on the type of activity')
    fig.update_layout(legend_title=None, legend_y=0.5)
    fig.update_traces(textinfo='percent+label', textposition='inside')
    st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)
with c2:
    fig = px.pie(users_type, values='COUNT_ID', names='AUTHORASSOCIATION', title='Number of PRs in 2022 by type of activity')
    fig.update_layout(legend_title=None, legend_y=0.5)
    fig.update_traces(textinfo='percent+label', textposition='inside')
    st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)
st.info("It seems that CONTRIBUTORS had the biggest role in the development, followed by COLLABORATORS and then members.")

