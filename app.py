# -*- coding: utf-8 -*-

import pickle
import streamlit as st

# loading the saved model
finalmodel = pickle.load(open('model_file.sav', 'rb'))

# page title
st.set_page_config(page_title='Fake Credit Card Transaction Prediction', page_icon=':credit_card:')

# sidebar for navigation
st.sidebar.title('Navigation')
options = st.sidebar.selectbox('', ('Credit Card Fraudlent Transaction Prediction', ))

# getting the input data from the user
st.title('Transaction Prediction')
st.write('Please enter the following details to check for fraudulent transactions:')

color = 'gray'

# creating input boxes for transaction details
with st.form(key='credit_card_details'):
    col1, col2, col3 = st.columns(3)

    with col1:
        st.header('Time', style=color)
        time = st.number_input('', min_value=0, step=1)

        st.header('V1', style=color)
        v1 = st.number_input('', step=0.001)

        st.header('V4', style=color)
        v4 = st.number_input('', step=0.001)

        st.header('V5', style=color)
        v5 = st.number_input('', step=0.001)

        st.header('V6', style=color)
        v6 = st.number_input('', step=0.001)

        st.header('V8', style=color)
        v8 = st.number_input('', step=0.001)

        st.header('V9', style=color)
        v9 = st.number_input('', step=0.001)

        st.header('V11', style=color)
        v11 = st.number_input('', step=0.001)

        st.header('V12', style=color)
        v12 = st.number_input('', step=0.001)

        st.header('V13', style=color)
        v13 = st.number_input('', step=0.001)

        st.header('V14', style=color)
        v14 = st.number_input('', step=0.001)

        st.header('V16', style=color)
        v16 = st.number_input('', step=0.001)

        st.header('V17', style=color)
        v17 = st.number_input('', step=0.001)

        st.header('V18', style=color)
        v18 = st.number_input('', step=0.001)

        st.header('V19', style=color)
        v19 = st.number_input('', step=0.001)

        st.header('V21', style=color)
        v21 = st.number_input('', step=0.001)

        st.header('V23', style=color)
        v23 = st.number_input('', step=0.001)

        st.header('V25', style=color)
        v25 = st.number_input('', step=0.001)

        st.header('V26', style=color)
        v26 = st.number_input('', step=0.001)

        st.header('V27', style=color)
        v27 = st.number_input('', step=0.001)

    with col2:
        st.header('V2', style=color)
        v2 = st.number_input('', step=0.001)

        st.header('V3', style=color)
        v3 = st.number_input('', step=0.001)

        st.header('V7', style=color)
        v7 = st.number_input('', step=0.001)

        st.header('V10', style=color)
        v10 = st.number_input('', step=0.001)
with col3:
    st.header('V15', style=color)
    v15 = st.number_input('', step=0.001)

    st.header('V20', style=color)
    v20 = st.number_input('', step=0.001)

    st.header('V22', style=color)
    v22 = st.number_input('', step=0.001)

    st.header('V24', style=color)
    v24 = st.number_input('', step=0.001)

    st.header('V28', style=color)
    v28 = st.number_input('', step=0.001)

    st.header('Amount', style=color)
    amount = st.number_input('', step=0.001)
# creating a button for prediction
if st.button('Check for Fraudulent Transaction'):
    prediction = finalmodel.predict([[time, v1, v2, v3, v4, v5, v6, v7, v8, v9, v10, v11, v12, v13, v14, v15, v16, v17, v18, v19, v20, v21, v22, v23, v24, v25, v26, v27, v28, amount]])
    if prediction[0] == 1:
        st.error('The details you entered have a fraudulent transaction.')
    else:
        st.success('The transaction is valid.') 
