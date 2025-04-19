import streamlit as st
import pandas as pd
import plotly.express as px
df = pd.read_csv('vehicles_us.csv') #load data

df['is_4wd'] = df['is_4wd'].fillna(0).astype(int) #filling blank cells with 0 and converting to integer

df = df[df['price'] <= 100000] # filter to remove large outliers

# Header
st.header('Used Car Market Analysis Dashboard')

# Dropdown: Select vehicle type
vehicle_types = df['type'].dropna().unique()
vehicle_types.sort()
selected_type = st.selectbox('Select vehicle type:', ['All'] + list(vehicle_types))

# Filter by vehicle type
if selected_type != 'All':
    df = df[df['type'] == selected_type]

# Scatter Plot
st.subheader('How Price Relates to Time on Market')
fig = px.scatter(df, x='days_listed', y='price', color='type', title='Price vs. Time on Market', labels={'days_listed': 'Days on Market', 'price': 'Price ($)'})
st.plotly_chart(fig)

st.subheader("Price Distribution")
#Histogram for price distribution
fig_hist = px.histogram(df, x="price", nbins=50, title="Vehicle Price Distribution")
st.plotly_chart(fig_hist)