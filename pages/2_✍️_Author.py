# Libraries
import streamlit as st
from PIL import Image
import pandas as pd
import plotly.express as px
# Layout
st.set_page_config(page_title='Developer Activity in 2022 on NEAR Protocol', page_icon=':bar_chart:', layout='wide')
st.title('Authors section')

#CSS
with open('style.css')as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html = True)

@st.cache(ttl=1)
def get_data(query):
    if query == 'author':
        return pd.read_json('https://node-api.flipsidecrypto.com/api/v2/queries/16329171-5d4c-4b75-89ad-cc31188010f2/data/latest')
    elif query == 'users_type_date':
        return pd.read_json('https://node-api.flipsidecrypto.com/api/v2/queries/cdef12a7-08bf-4356-83ca-d6b8fea0b5f6/data/latest')
    elif query == 'new_developers':
        return pd.read_json('https://node-api.flipsidecrypto.com/api/v2/queries/13956683-e6b7-40be-8baa-a27c2a6fa76e/data/latest')
    # elif query == 'Transactions Fee Payers':
    #     return pd.read_json('https://node-api.flipsidecrypto.com/api/v2/queries/7eae69ea-2387-420d-b4b9-6eceeb5ef22d/data/latest')
    return None

#Get Data
top10_authors = get_data('author')
users_type_date = get_data('users_type_date')
new_developers = get_data('new_developers')

theme_plotly = None # None or streamlit



c1,c2 =st.columns(2)
with c1:
    fig = px.pie(top10_authors, values='COUNT_ID', names='AUTHOR', title='Top 10 authors in 2022 in terms of number of activities')
    fig.update_layout(legend_title=None, legend_y=0.5)
    fig.update_traces(textinfo='percent+label', textposition='inside')
    st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)
    st.info("The highest activity in 2022 was for the mina86 account with about 18%, followed by the matklad account with about 13%.")
with c2:
    fig = px.pie(top10_authors, values='REPOS', names='AUTHOR', title='Top 10 authors in 2022 in terms of number of REPOs')
    fig.update_layout(legend_title=None, legend_y=0.5)
    fig.update_traces(textinfo='percent+label', textposition='inside')
    st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)
    st.info("In 2022, in terms of the number of REPOs, the most activity was for the austinabell account with about 27% and the sandoche account with about 18%")



fig = px.bar(users_type_date, x='DATE', y='COUNT_ID', color='AUTHOR', title='Top 10 AUTHORS in terms of the number of activities on a weekly basis')
fig.update_layout(showlegend=True, xaxis_title=None, yaxis_title='Activities', xaxis={'categoryorder':'total ascending'})
st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)
st.info("In May 2022, the most development activity was recorded in NEAR, in this month the sandoche account had the most activity, while as we are getting closer to the end of 2022, the amount of activity of developers has decreased.")

fig = px.bar(users_type_date, x='DATE', y='REPOS', color='AUTHOR', title='Top 10 AUTHORS in terms of the number of REPOs on a weekly basis')
fig.update_layout(showlegend=True, xaxis_title=None, yaxis_title='REPOs', xaxis={'categoryorder':'total ascending'})
st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)
st.info("In terms of the number of REPOs in the daily review, it seems that the most activity was on August 15, 2022, and the austinabell account played the biggest role.")

fig = px.bar(new_developers, x='NEW_DATE_1', y='AUTHORS', title='New developers during 2022 in terms of number')
fig.update_layout(showlegend=True, xaxis_title=None, yaxis_title='REPOs', xaxis={'categoryorder':'total ascending'})
st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)


fig = px.line(new_developers, x='NEW_DATE_1', y='GROWRH_AUTHORS', title='New developers during 2022 in terms of number growth')
fig.update_layout(showlegend=True, xaxis_title=None, yaxis_title='REPOs', xaxis={'categoryorder':'total ascending'})
st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)
st.info("When we take a look at the latest developers, we find that the largest recruitment of new developers was in January 2022, and the participation of new developers has gradually decreased.")