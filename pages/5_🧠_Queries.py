# Libraries
import streamlit as st
from PIL import Image
import pandas as pd
import plotly.express as px
# Layout
st.set_page_config(page_title='Developer Activity in 2022 on NEAR Protocol', page_icon=':bar_chart:', layout='wide')
st.title('List of queries')

#CSS
with open('style.css')as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html = True)


st.markdown('https://app.flipsidecrypto.com/velocity/queries/6bed72f3-f508-494e-94c4-1c975f674786', unsafe_allow_html=True)
st.markdown('https://app.flipsidecrypto.com/velocity/queries/4b9fa244-4679-4fe7-9fda-55cb3fedb140', unsafe_allow_html=True)
st.markdown('https://app.flipsidecrypto.com/velocity/queries/16329171-5d4c-4b75-89ad-cc31188010f2', unsafe_allow_html=True)
st.markdown('https://app.flipsidecrypto.com/velocity/queries/cdef12a7-08bf-4356-83ca-d6b8fea0b5f6', unsafe_allow_html=True)
st.markdown('https://app.flipsidecrypto.com/velocity/queries/717e3c45-2334-49fe-bbb4-7185f06570bc', unsafe_allow_html=True)
st.markdown('https://app.flipsidecrypto.com/velocity/queries/13956683-e6b7-40be-8baa-a27c2a6fa76e', unsafe_allow_html=True)
st.markdown('https://app.flipsidecrypto.com/velocity/queries/4877ed5c-f392-4c30-b987-6bd0e3f9d783', unsafe_allow_html=True)
st.markdown('https://app.flipsidecrypto.com/velocity/queries/76e9f3ce-8ffc-4f63-b752-ab341e14b1e9', unsafe_allow_html=True)
st.markdown('https://github.com/saleh20032004/Near-Developer-Activity', unsafe_allow_html=True)
