import streamlit as st
import pandas as pd

st.title('🖥Machine Learning on Rails')

st.info("New century of Machine Learning")

epl_df = pd.read_csv('https://raw.githubusercontent.com/fredericklaud/fl-data/refs/heads/main/England%20CSV.csv')
with st.expander('EPL Data'):
  st.write(epl_df)
