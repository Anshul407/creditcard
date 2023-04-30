# -*- coding: utf-8 -*-

import pickle
import streamlit as st

# loading the saved model
finalmodel = pickle.load(open('model_final.sav', 'rb'))

# page title
st.set_page_config(page_title='Fake Credit Card Transaction Prediction', page_icon=':credit_card:')

# sidebar for navigation
st.sidebar.title('Navigation')
options = st.sidebar.selectbox('', ('Fraudlent Transaction Prediction', ))

# getting the input data from the user
st.title('Fraudlent Transaction Prediction')
st.write('Please enter the following details to check for fraudulent transactions:')

time = st.text_input('Time')
v1 = st.text_input('V1')
v2 = st.text_input('V2')
v3 = st.text_input('V3')
v4 = st.text_input('V4')
v5 = st.text_input('V5')
v6 = st.text_input('V6')
v7 = st.text_input('V7')
v8 = st.text_input('V8')
v9 = st.text_input('V9')
v10 = st.text_input('V10')
v11 = st.text_input('V11')
v12 = st.text_input('V12')
v13 = st.text_input('V13')
v14 = st.text_input('V14')
v15 = st.text_input('V15')
v16 = st.text_input('V16')
v17 = st.text_input('V17')
v18 = st.text_input('V18')
v19 = st.text_input('V19')
v20 = st.text_input('V20')
v21 = st.text_input('V21')
v22 = st.text_input('V22')
v23 = st.text_input('V23')
v24 = st.text_input('V24')
v25 = st.text_input('V25')
v26 = st.text_input('V26')
v27 = st.text_input('V27')
v28 = st.text_input('V28')
amount = st.text_input('Amount')

# creating a button for prediction
if st.button('Check for Fraudulent Transaction'):
    prediction = finalmodel.predict([[time, v1, v2, v3, v4, v5, v6, v7, v8, v9, v10, v11, v12, v13, v14, v15, v16, v17, v18, v19, v20, v21, v22, v23, v24, v25, v26, v27, v28, amount]])
    if prediction[0] == 1:
        st.error('The details you entered have a fraudulent transaction.')
    else:
        st.success('The transaction is valid.')
