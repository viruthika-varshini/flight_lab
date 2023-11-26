import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import plotly.express as px
from PIL import Image

st.set_page_config(
    page_title='Flight Price Prediction - EDA',
    layout='wide',
    initial_sidebar_state='expanded'
)

def runEDA():
    #Title
    st.title('Flight Price Prediction')

    #Sub Header
    st.subheader('EDA for Flight Price Prediction')

    #Description
    st.write('Page Created by Gilang Wiradhyaksa (SBY-001)')

    st.markdown('---')

    '''
    On this Page we will do a simple exploration,
    Database Used is Flight Price Prediction.
    Dataset Source is from Kaggle
    '''

    #show dataframe
    st.title('Dataset')
    df = pd.read_csv('flight_price_prediction.csv')
    st.dataframe(df)

    plt.style.use('default')
    st.write('## Histogram Price')
    fig = plt.figure(figsize=(15,5))
    sns.histplot(df['price'], bins=20, kde=True).set(title='Price')
    st.pyplot(fig)
    st.write('Based on the histogram plot, we can see that most of the flight having price less than 10k INR (Indian Rupee). But for few flight price is goes up to 120k INR, this probably the price of business class.')
    st.markdown('---')

    st.write('## Airlines Flights Count')
    df_airlines = df.groupby(['airline']).agg(counts=('flight', 'count')).sort_values(by=['counts'], ascending=False)
    fig, ax = plt.subplots(ncols=1, figsize=(15, 5))
    ax.pie(df_airlines['counts'], labels=df_airlines['counts'].index, autopct='%.2f%%')
    ax.set_title("Airlines Flight Count")
    st.pyplot(fig)
    st.write('The flight is dominated by `Vistara` Airlines with more than 127k flights. Their biggest competitor is `Air India` with 80k flights.')
    st.markdown('---')

    st.write('## Flight Stops/Transit Count')
    df_stops = df.groupby(['stops']).agg(counts=('airline', 'count'))
    fig, ax = plt.subplots(ncols=1, figsize=(15, 5))
    ax.pie(df_stops['counts'], labels=df_stops['counts'].index, autopct='%.2f%%')
    ax.set_title("Flight Stops (Transit) Count")
    st.pyplot(fig)
    st.write('Most of flight on this dataset is having one transit. Only 12% of the data that is a direct flight.')
    st.markdown('---')

    df_departure = df.groupby(['departure_time']).agg({'price':'mean'}).sort_values(by=['price'], ascending=True)
    fig = plt.figure(figsize=(7, 5))
    sns.barplot(data=df_departure, x=df_departure.index.to_list(), y='price', orient='v').set(title='Average price per Departure Time')
    st.pyplot(fig)
    st.write('From the bar plot above we can see that Late Night ticket average price is cheapest compared to other time. Meanwhile night and morning flight have the most expensive average price.')
    st.markdown('---')

    plt.style.use('dark_background')
    fig = plt.figure(figsize=(20,8))
    sns.lineplot(data=df, x='duration', y='price', hue='class', palette='hls')
    plt.title('Ticket Price Versus Flight Duration Based on Class',fontsize=20)
    plt.xlabel('Duration', fontsize=15)
    plt.ylabel('Price', fontsize=15)
    st.pyplot(fig)
    st.write('Based on the line graph above, we can see that as the flight duration increase the ticket price is also increases in both the Economy and Business classes')
    st.markdown('---')

    fig = plt.figure(figsize=(20,8))
    sns.lineplot(data=df, x='days_left', y='price', color='blue')
    plt.title('Days Left For Departure Versus Ticket Price',fontsize=20)
    plt.xlabel('Days Left for Departure',fontsize=15)
    plt.ylabel('Price',fontsize=15)
    st.pyplot(fig)
    st.write('Based on the line graph above, we can see that as the flight duration increase the ticket price is also increases in both the Economy and Business classes')
    st.markdown('---')

if __name__ == '__main__':
    runEDA()