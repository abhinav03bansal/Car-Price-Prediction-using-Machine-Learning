import streamlit as st
import pickle
import numpy as np
import pandas as pd
data=pd.read_csv('T4DS.csv')
model=pickle.load(open('car.sav','rb'))
st.title("Welcome to Car Price Prediction")
car_name=data['Car_Name'].unique()
car_name=car_name.tolist()
name=st.selectbox('Select Car Name',car_name)
pp=st.number_input("Purchasing Price(in decimal lacs)")
dist=st.number_input("KiloMeters Driven")
fuel1=data['Fuel_Type'].unique()
fuel1=fuel1.tolist()
fuel=st.selectbox('Fuel Type',fuel1)
if fuel=='Petrol':
    fp=1
    fd=0
else:
    fp=0
    fd=1
age=st.slider("Age of Vehicle",0,20)
owner=st.slider("No of previous Owners",0,5)
trans1=data['Transmission'].unique()
trans1=trans1.tolist()
transmission=st.selectbox("Select Transmission Type",trans1)
if transmission=='Manual':
    transmission=1
else:
    transmission=0
sell1=data['Selling_type'].unique()
sell1=sell1.tolist()
seller=st.selectbox("Select the Seller",sell1)
if seller=='Individual':
    seller=1
else:
    seller=0
btn=st.button("Predict")
if btn:
    predict=model.predict([[pp,dist,owner,age,fd,fp,seller,transmission]])[0]
    print(predict)

    st.subheader(predict)