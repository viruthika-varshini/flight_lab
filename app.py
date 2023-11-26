import streamlit as st
import eda
import prediction

navigation = st.sidebar.selectbox('Select Page :', ('Exploratory Data Analysis', 'Predict Flight Price'))

if navigation == 'Exploratory Data Analysis':
    eda.runEDA()
else:
    prediction.runPredictor()

#streamlit run app.py