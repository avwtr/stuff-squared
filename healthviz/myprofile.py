import streamlit as st 
from streamlit_lottie import st_lottie
import requests
import json
from lottie import load_lottie
import time
from database import insert_mh
from datetime import datetime
from database import insert_body
from database import body_df

def render_myprof(name, username):

    st.subheader(f"Hello, {name}")
    func_call = body_df()
    user_data_before = func_call[func_call["user"] == username]
    
    
    #insert_body("workout-2-avawter123", "avawter123", "170", "80", "14", "11-22-22")
    with st.expander("Enter a Body Composition Update (Weight, Muscle Mass, Body Fat %)"):
        with st.form(key = "body-comp", clear_on_submit = True):
            now = datetime.now()
            fixed = json.dumps(now, indent=4, sort_keys=True, default=str)

            curr_weight = st.number_input("Log your current weight", key = "weight", min_value = 0, max_value = 550)
            curr_body_fat = st.number_input("Log your current body fat percentage (%)", key = "body-fat", min_value = 0, max_value = 100)
            st.caption("If you don't know, you can just leave it at zero")
            curr_muscle = st.number_input("Log your total lean muscle mass (lbs)", key = "lean-muscle", min_value = 0, max_value = 500)
            submit = st.form_submit_button("Submit entry")

            if submit:
                workout_num = len(user_data_before) + 1
                key = f"workout-{workout_num}-{username}"
                insert_body(key, username, curr_weight,curr_muscle , curr_body_fat, fixed)
                st.success("Entry submitted")
    st.write(" ")
    st.write(" ")
    st.write(" ")

    func_call_2 = body_df()
    user_data_after = func_call_2[func_call_2["user"] == username]

    metric1, metric2, metric3 = st.columns(3)
 
    if len(user_data_after) > 1: 
        initial_weight = user_data_after["current_weight"].tolist()[-2]
        second_weight = user_data_after["current_weight"].tolist()[-1]
        delta = initial_weight - second_weight
        metric1.metric("Most recent Weight(lbs)", f"{second_weight}", f"Weight Change: {delta}")
        #st.caption("Change is calculated based on your two most recent entries")

    elif len(user_data_after) == 1:
        second_weight = user_data_after["current_weight"].tolist()[-1]
        metric1.metric("Most recent Weight(lbs)", f"{second_weight}", f"Only 1 entry found")
        #st.caption("Change is calculated based on your two most recent entries")

    elif len(user_data_after) == 0:
         metric1.metric("Most recent Weight(lbs)", "No Entries Detected yet")

    filt_to_lm = user_data_after["lean_muscle"]
    if len(filt_to_lm) > 1:
        initial_lm = user_data_after["lean_muscle"].tolist()[-2]
        second_lm = user_data_after["lean_muscle"].tolist()[-1]
        delta = initial_lm - second_lm
        metric2.metric("Lean Muscle Mass Change (lbs)",f"{second_lm}", f"{delta} lbs")
        #st.caption("Change is calculated based on your two most recent entries")

    elif len(filt_to_lm) == 1: 
        second_lm  = user_data_after["lean_muscle"].tolist()[-1]
        metric2.metric("Lean Muscle Mass Change (lbs)",f"{second_lm}", f"Only 1 entry found")
        #st.caption("Change is calculated based on your two most recent entries")

    elif len(filt_to_lm) == 0:
        metric2.metric("Lean Muscle Mass Change (lbs)", "No Entries Detected Yet")

    filt_to_bf = user_data_after["body_fat_percentage"]
    if len(filt_to_bf) > 1: 
        initial_bf = user_data_after["body_fat_percentage"].tolist()[-2]
        second_bf = user_data_after["body_fat_percentage"].tolist()[-1]
        delta = initial_bf - second_bf
        metric3.metric("Body Fat % (Change)", f"{second_bf}%", f"{delta}")
        #st.caption("Change is calculated based on your two most recent entries")

    elif len(filt_to_bf) == 1:
        second_bf = user_data_after["body_fat_percentage"].tolist()[-1]
        metric3.metric("Body Fat % (Change)", f"{second_bf}%", "Only 1 entry found")
        #st.caption("Change is calculated based on your two most recent entries")

    elif len(filt_to_bf) == 0:
        metric3.metric("Body Fat % (Change)", "No Entries Detected Yet")


    st.write(" ")
    st.write(" ")
    st.write(" ")
    st.write(" ")

    my_health_priorities = st.multiselect("Choose your Top Health 3 priorities (in order)", 
                                    ["Get stronger", "Lose Weight", "Gain Weight", "Improve athletic performance",
                                    "Feel good", "Improve general health", "Training for something specific (an event, role, etc.)", 
                                    "Improve mental health"])
    st.caption("The app will only recognize your top 3 selected choices (in order)")

    choices = my_health_priorities[:3]
    j = 0
    for i in choices: 
        st.write(f"#{j+1}: {i}")
        j+=1

        
    
    

 

