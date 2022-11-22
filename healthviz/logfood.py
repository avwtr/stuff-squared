import streamlit as st
from streamlit_lottie import st_lottie
import requests
import json
from lottie import load_lottie
import time
from database import insert_food
from datetime import datetime
from database import food_df




def render_logfood(name, username):
    h1, h2, h3  = st.columns(3)
    now = datetime.now()
    with h1: 
        lottie = load_lottie("lottie/food.json")
        st_lottie(lottie, height = 100 , width = 100,key = "food")
    with h2: 
        st.header("Log my meal")    
    with h3: 
        st.write("")
    st.write("")
    with st.form(key = "foodform", clear_on_submit = True):
        date = st.date_input("Date")
        mealtime = st.time_input("Enter the time of day that you consumed this meal")

        meal_type = st.selectbox("Select the type of meal", ("Breakfast", "Lunch", "Dinner", "Snack"), key = "1")
        st.write("")
        liq_or_solid = st.selectbox("Solid or Liquid Calories?", ("Solid", "Liquid"), key = "2")
        if liq_or_solid == "Solid":
            food_name = st.text_input("What did you eat?", key = "sol-name")
        if liq_or_solid == "Liquid":
            food_name = st.text_input("What did you drink?", key = "liq-name",)

        st.subheader("Nutritional Content")
        num_cals = st.number_input("How many calories was this meal?", key = "cals", min_value=0, max_value = 4000)

        st.write("Macros")
        protein = st.number_input("Enter the total protein content (grams - g)", key = "pro")
        fat = st.number_input("Enter the total fat content (grams - g)", key = "fat")
        carbs = st.number_input("Enter the total Carbohydrate content (grams - g)", key = "carbs")

        submit = st.form_submit_button("Submit meal entry")
        if submit:
            st.success("Entry Submitted")
            fixed_date1 = json.dumps(date, indent=4, sort_keys=True, default=str)
            fixed_date2 = json.dumps(now, indent=4, sort_keys=True, default=str)
            fixed_time = json.dumps(mealtime, indent=4, sort_keys=True, default=str)
            
            func_call = food_df()
            user_data_before = func_call[func_call["user"] == username]
            
            log_num = len(user_data_before) + 1
            key = f"food-{log_num}-{username}"

            insert_food(key, username, fixed_date1, fixed_time, meal_type, liq_or_solid, food_name, num_cals, protein, fat, carbs, fixed_date2)

