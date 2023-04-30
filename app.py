# -*- coding: utf-8 -*-

import pickle
import streamlit as st
from streamlit_option_menu import option_menu


# loading the saved models

finalmodel = pickle.load(open('model_file.sav', 'rb'))


# sidebar for navigation
with st.sidebar:
    
    selected = option_menu('Credit Card ',
                          
                          ['Credit Card'],
                          icons=['activity'],
                          default_index=0)
    
    
if (selected == 'Transaction Prediction'):
    
    # page title
    st.title('Fake Credit Card Transaction Prediction')
    
    
    # getting the input data from the user
    col1, col2, col3 = st.columns(3)
    
    with col1:
        Pregnancies = st.text_input('Time')
        
    with col2:
        Glucose = st.text_input('V1')
    
    with col3:
        BloodPressure = st.text_input('V2')
    
    with col1:
        SkinThickness = st.text_input('V3')
    
    with col2:
        Insulin = st.text_input('V4')
    
    with col3:
        BMI = st.text_input('V5')
    
    with col1:
        DiabetesPedigreeFunction = st.text_input('V6')
    
    with col2:
        Age = st.text_input('V7')
    with col3:
        a = st.text_input('V8')
    
    with col1:
        b = st.text_input('V9')
    
    with col2:
        c = st.text_input('V10')
    
    with col3:
        d = st.text_input('V11')
    
    with col1:
        e = st.text_input('V12')
    
    with col2:
        f= st.text_input('V13')
    with col3:
        g= st.text_input('V14')
    
    with col1:
        h = st.text_input('V15')
    
    with col2:
        i= st.text_input('V16')
        
    with col3:
        j= st.text_input('V17')

    with col1:
        k = st.text_input('V18')
    
    with col2:
        l= st.text_input('V19')
        
    with col3:
        m= st.text_input('V20')
     
    with col1:
        n = st.text_input('V21')
    
    with col2:
        o= st.text_input('V22')
        
    with col3:
        p= st.text_input('V23')

    with col1:
        q = st.text_input('V24')
    
    with col2:
        r= st.text_input('V25')
        
    with col3:
        s= st.text_input('V26')

    with col1:
        t = st.text_input('V27')
    
    with col2:
        u= st.text_input('V28')
        
    with col3:
        v= st.text_input('Amount')
    
    
    
    
    
    # code for Prediction
    trans_result = ''
    
    # creating a button for Prediction
    
    if st.button('Transaction Prediction Result'):
        trans_prediction = finalmodel.predict([[Pregnancies, Glucose, BloodPressure, SkinThickness, Insulin, BMI, DiabetesPedigreeFunction, Age,a,b,c,d,e,f,g,h,i,j,k,l,m,n,o,p,q,r,s,t,u,v]])
        if (trans_prediction[0] == 1):
          trans_result = 'The Details you entered have fraudlent transaction'
        else:
          trans_result = 'Valid Transaction'

        
    st.success(trans_result)
