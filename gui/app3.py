import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px

@st.cache
def load_data():
    url = 'https://raw.githubusercontent.com/digipodium/Datasets/main/regression/dataA.csv'
    df = pd.read_csv(url)
    return df

df = load_data()

st.header("Data science app")

if st.checkbox("see raw data"):
    st.dataframe(df)

vis_ops = ['2D Vis','3D Vis']
columns = df.columns.tolist()
choice = st.sidebar.radio("select an option", vis_ops)
if choice == vis_ops[0]:
    x = st.sidebar.selectbox('select column for X axis', columns)
    y = st.sidebar.selectbox('select column for Y axis', columns)
    fig = px.scatter(df, x, y, color=x)
    st.plotly_chart(fig, use_container_width=True)