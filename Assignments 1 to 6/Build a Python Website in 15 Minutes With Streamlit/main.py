import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.set_page_config(page_title='Simple Data Dashboard', page_icon='📊')
st.write('##  Simple Data Dashboard')

uploaded_file = st.file_uploader('Choose a CSV file', type='csv')

if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)

    st.subheader('Data preview')
    st.write(df.head())

    st.subheader('Data Summary')
    st.write(df.describe())

    st.subheader('Filter Data')
    columns = df.columns.to_list()
    selected_columns = st.selectbox('Select Column to filter by: ', columns)
    unique_value = df[selected_columns].unique()
    selected_value = st.selectbox('Select Value ', unique_value)
    filter_df = df[df[selected_columns] == selected_value]
    st.write(filter_df)

    st.subheader('Address Data')
    x_column = st.selectbox('Select x-axis column', columns)
    y_column = st.selectbox('Select y-axis column', columns)

    if st.button('Generate Address'):
        st.line_chart(filter_df.set_index(x_column)[y_column])

else:
    st.write('waiting for file uploaded...')