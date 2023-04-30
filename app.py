# -*- coding: utf-8 -*-

import pickle
import streamlit as st

# loading the saved model
finalmodel = pickle.load(open('model_file.sav', 'rb'))

# page title and icon
st.set_page_config(page_title='Fake Credit Card Transaction Prediction', page_icon=':credit_card:')

# sidebar for navigation
st.sidebar.title('Navigation')
options = st.sidebar.selectbox('', ('Creadit Card Fraudlent Transaction Prediction', ))

# main page header
st.title('Credit Card Fraudlent transaction Detection')
st.write('Please enter the following details to check for fraudulent transactions:')

# input fields with improved style and layout
col1, col2, col3 = st.beta_columns(3)

with col1:
    time = st.text_input('Time', key='time')
    v1 = st.text_input('V1', key='v1')
    v2 = st.text_input('V2', key='v2')
    v3 = st.text_input('V3', key='v3')
    v4 = st.text_input('V4', key='v4')
    v5 = st.text_input('V5', key='v5')
    v6 = st.text_input('V6', key='v6')

with col2:
    v7 = st.text_input('V7', key='v7')
    v8 = st.text_input('V8', key='v8')
    v9 = st.text_input('V9', key='v9')
    v10 = st.text_input('V10', key='v10')
    v11 = st.text_input('V11', key='v11')
    v12 = st.text_input('V12', key='v12')
    v13 = st.text_input('V13', key='v13')

with col3:
    v14 = st.text_input('V14', key='v14')
    v15 = st.text_input('V15', key='v15')
    v16 = st.text_input('V16', key='v16')
    v17 = st.text_input('V17', key='v17')
    v18 = st.text_input('V18', key='v18')
    v19 = st.text_input('V19', key='v19')
    v20 = st.text_input('V20', key='v20')

v21 = st.text_input('V21', key='v21')
v22 = st.text_input('V22', key='v22')
v23 = st.text_input('V23', key='v23')
v24 = st.text_input('V24', key='v24')
v25 = st.text_input('V25', key='v25')
v26 = st.text_input('V26', key='v26')
v27 = st.text_input('V27', key='v27')
v28 = st.text_input('V28', key='v28')
amount = st.text_input('Amount', key='amount')

# prediction button with improved style and layout
if st.button('Check for Fraudulent Transaction'):
    prediction = finalmodel.predict([[time, v1, v2, v3, v4, v5, v6, v7, v8, v9, v10, v11, v12, v13, v14, v15, v16, v17, v18, v19, v20, v21, v22, v23, v24, v25, v26, v27, v28, amount]])
    if prediction[0] == 1:
       st.error('The details you entered have a fraudulent transaction.')
    else:
       st.success('The transaction is valid.') 
