import streamlit as st
import numpy as np
import pickle
import pandas as pd

model = pickle.load(open("predictPrice.pkl", "rb"))

st.title('Football Player Price Prediction')
big_club_options = [0,1]

Page_views = st.number_input('Enter Page Views')
Fpl_Value = st.number_input('Enter Fpl_Value')
Fpl_Selection = st.slider(min_value=0.01, max_value= 100.00, label="Fpl_Selection Percentage")
Fpl_Points = st.number_input('Enter Fpl_Points')
Big_Club = st.selectbox(options= big_club_options, label= "Big Club (Yes --> 1 , No --> 2 )")


def predict():
    x = pd.DataFrame([])
    x[["page_views",	"fpl_value",	"fpl_sel",	"fpl_points",	"big_club"]] = [[Page_views,Fpl_Value,Fpl_Selection/100,Fpl_Points,Big_Club]]
    price = model.predict(x)
    label = price[0]
    print(type(label))
    print(label)
    st.success('The Price of Player is : ' + str(label) + ' :thumbsup:')
    
trigger = st.button('Predict', on_click=predict)