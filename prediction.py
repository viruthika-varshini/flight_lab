import streamlit as st
import pandas as pd
import numpy as np
import pickle
import json

def runPredictor():
    #MODEL
    with open('best_model_dt.pkl', 'rb') as file_1:
        best_model_dt = pickle.load(file_1)

    # Buat Form
    with st.form(key='Form Parameters'):
        airline = st.selectbox('Airlines', ('SpiceJet', 'AirAsia', 'Vistara', 'GO_FIRST', 'Indigo', 'Air_India'), index=0)
        source_city = st.selectbox('Departure City', ('Delhi', 'Mumbai', 'Bangalore', 'Kolkata', 'Hyderabad', 'Chennai'), index=0)
        destination_city = st.selectbox('Destination City', ('Mumbai', 'Bangalore', 'Kolkata', 'Hyderabad', 'Chennai', 'Delhi'), index=0)
        st.markdown('---')
        departure_time = st.selectbox('Departure Time', ('Evening', 'Early_Morning', 'Morning', 'Afternoon', 'Night', 'Late_Night'), index=0)
        arrival_time = st.selectbox('Arrival Time', ('Night', 'Morning', 'Early_Morning', 'Afternoon', 'Evening', 'Late_Night'), index=0)
        st.markdown('---')
        stops = st.selectbox('Transit', ('Direct', 'One', 'Two or more'), index=0)
        flight_class = st.selectbox('Class', ('Economy', 'Business'), index=0)
        st.markdown('---')
        duration = st.number_input('Flight Duration', min_value=0, max_value=50, step=1)
        days_left = st.number_input('Days Until Flight', min_value=1, max_value=90, step=1)
        st.markdown('---')

        submitted = st.form_submit_button('Predict')

        if stops == 'Direct': stops = 'zero'
        elif stops == 'One': stops = 'one'
        else: stops = 'two_or_more'

        data_inf = {
            'airline': airline,
            'source_city': source_city,
            'destination_city': destination_city,
            'departure_time': departure_time,
            'arrival_time': arrival_time,
            'stops': stops,
            'class': flight_class,
            'duration': duration,
            'days_left': int(days_left)
        }

    df = pd.DataFrame([data_inf])
    st.dataframe(df)

    if submitted:
        y_predict_new_price = best_model_dt.predict(df)
        st.write(f'# Ticket Price Prediction : {str(int(y_predict_new_price))} INR')

if __name__ == '__main__':
    runPredictor()