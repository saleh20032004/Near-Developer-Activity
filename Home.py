# Libraries
import streamlit as st
from PIL import Image
import pandas as pd
import plotly.express as px
# Layout
st.set_page_config(page_title='Developer Activity in 2022 on NEAR Protocol', page_icon=':bar_chart:', layout='wide')
st.title('Developer Activity in 2022 on NEAR Protocol')

#CSS
with open('style.css')as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html = True)
c1,c2 = st.columns(2)
with c1:
    st.info('What is Near protocol?')
    st.caption("The main goal of the NEAR network is to create an infrastructure for creating a new Internet."
            "In the new internet, it will be harder for big companies to access peoples personal information."
            "Countries cannot ban some programs and destroy their business in this system. A world of freedom where everyone can act freely. Of course, this goal of the NEAR network is not a new concept; In fact, Satoshi Nakamoto also pursued the same goal by introducing Bitcoin in 2008. But Bitcoin has created this freedom only in the financial sphere."
            "Ethereum and many other projects, including Near, also seek to extend this freedom to other aspects of human life. So far, we have found that the Near network is a platform for creating decentralized applications; Exactly what Ethereum does.")
    st.caption("")
    st.caption("")
    st.caption("")
    st.caption("")
    st.caption("")
    st.image('images/2.jpg')    
with c2:
    st.info('Development activity on NEAR')
    st.caption("To track developer activity on NEAR one can take a closer look at repositories on Github and announcements on Twitter. These sources are easily available to the public, while development in private is not easy to track and measure. Nevertheless, research reports from groups like Electric Capital and Outlier Ventures also rely on Github repository activity to measure activity of development communities of blockchain platforms."
                "For activity on NEAR we analyzed the main NEAR Github repository and its eight most frequently utilized and related repositories (near-explorer, nearcore, create-near-app, docs, near-wallet, near-api-js, sdk-docs, near-sdk-as, near-cli) for commits and forks in the past 12 months. Additionally, three main NEAR-affiliated twitter accounts (@nearprotocol, @pagodaplatform, @nearweek) were scraped for project announcements during the past 12 months. The rationale for scaling each metric to its respective weight is explained below."
                "A scaled “development activity” score was produced by totaling the following activities each week over the past year and weighing them based on how much each activity is indicative of substantive development activity on Substrate:"
              )
    st.image('images/1.png')

st.info('**Source: [Figment](https://www.figment.io/resources/developer-traffic-on-near-protocol)**', icon="🌏")
    
c1, c2,c3,c4 = st.columns(4)
with c1:
    st.info('**Developer/Analyst: [@saleh03188287](https://twitter.com/saleh03188287)**', icon="🐦")
with c2:
    st.info('**Data: [Flipside Crypto](https://flipsidecrypto.xyz/)**', icon="🧠")
with c3:
    st.info('**Discord: Sal☰h#1747**', icon="💻")
with c4:
    st.info('**For: [Metricsdao](http://metricsdao.xyz)**', icon="🧠")