import streamlit as st
import streamlit_authenticator as stauth
from streamlit_lottie import st_lottie
from lottie import load_lottie
import time
from database import insert_workout
from database import workout_df
from datetime import datetime
import json



def render_logdaily(name, username):

    now = datetime.now()
    h1, h2, h3 = st.columns(3)
    with h1:
        lottie = load_lottie("lottie/weights.json")
        st_lottie(lottie, height = 100 , width = 100,key = "weights")
    with h2: 
        st.header("Log my Workout")
    with h3: 
        st.write("")

    date = st.date_input("Workout Date")

    st.write(" ")
    st.write(" ")
    st.write(" ")

    workout_type = st.multiselect("Select workout type completed (can select multiple if applicable)",
    ["Cardio", "Strength/Weight Lifting", "Sports/Recreation"])
    st.write(" ")
    
    if "Cardio" in workout_type:
        with st.form(key = "log-cardio", clear_on_submit = True):
            st.subheader("Cardio Session")
            workout_note = st.text_area("Enter a workout label/title, or any relevant notes regarding this cardio session")
            st.write("")
            workout_start = st.time_input("Time of Day that you started this workout", key = "cardio-start")
            workout_end = st.time_input("Time of Day that you finished this workout", key = "cardio-finish")
            st.write("")
            sub_activity = st.multiselect("What type of Cardio session did you complete?", ['Run', 'Walk', 'Hike', 'Bike', 'Stairs'])
            st.caption("Select multiple if applicable")
            sub_act_metric = st.number_input("How many miles of cardio did you complete?", key = "cardio-metric")
            st.write("")
            intensity_level = st.select_slider('Indicate the intesity level of your cardio session',
                                        options=['Recovery', 'Comfortable','High Performance', 'Complete Exhaustion'])

            calorie_burn = st.number_input("How many calories did you burn?", min_value = 0, max_value = 10000, key = "cardio-cal")
            st.caption("If unsure, just estimate")

            if st.form_submit_button("Submit Cardio Entry"):
                    fixed_date = json.dumps(now, indent=4, sort_keys=True, default=str)
                    fixed_time_initial = json.dumps(workout_start, indent=4, sort_keys=True, default=str)
                    fixed_time_final = json.dumps(workout_end, indent=4, sort_keys=True, default=str)
    
                    func_call = workout_df()
                    user_data_before = func_call[func_call["user"] == username]
                    log_num = len(user_data_before) + 1
                    key = f"workout-{log_num}-{username}"

                    insert_workout(key, username, fixed_date, fixed_time_initial, fixed_time_final, "Cardio", sub_activity, 
                                    calorie_burn, sub_act_metric, intensity_level)
                    st.success("Cardio Entry Submitted")

    if "Strength/Weight Lifting" in workout_type:
        with st.form(key = "log-strength", clear_on_submit = True):
            st.subheader("Strength Session")
            workout_note = st.text_area("Enter a workout label/title, or any relevant notes regarding this strength session")
            st.write("")
            workout_start = st.time_input("Time of Day that you started this workout", key = "strength-start")
            workout_end = st.time_input("Time of Day that you finished this workout", key = "strength-finish")
            st.write("")
            sub_activity = st.multiselect("What muscle groups did you work?", ["Biceps", "Back", "Chest", "Triceps", "Legs (Quads)", "Legs (Hamstrings)", "Legs (Glutes)",
                                                                    "Legs (Calves)", "Shoulders","Forearms"], key = "strength-sub")
            st.caption("Select multiple if applicable")
            sub_act_metric = st.number_input("How many unique exercises did you complete in total?", key = "strength-metric")
            st.write("")
            intensity_level = st.select_slider('Indicate the overall intesity level of your strength session',
                                        options=['Recovery', 'Comfortable','High Performance', 'Complete Exhaustion'])

            calorie_burn = st.number_input("How many calories did you burn?", min_value = 0, max_value = 10000, key = "strength-cal")
            st.caption("If unsure, just estimate")

            if st.form_submit_button("Submit Strength Entry"):
                    fixed_date = json.dumps(now, indent=4, sort_keys=True, default=str)
                    fixed_time_initial = json.dumps(workout_start, indent=4, sort_keys=True, default=str)
                    fixed_time_final = json.dumps(workout_end, indent=4, sort_keys=True, default=str)
                    
                    func_call = workout_df()
                    user_data_before = func_call[func_call["user"] == username]
                    log_num = len(user_data_before) + 1
                    key = f"workout-{log_num}-{username}"

                    insert_workout(key, username, fixed_date, fixed_time_initial, fixed_time_final, "Strength", sub_activity, 
                                    calorie_burn, sub_act_metric, intensity_level)
                    st.success("Strength Entry Submitted")

    if "Sports/Recreation" in workout_type:
        with st.form(key = "log-rec", clear_on_submit = True):
            st.subheader("Recreation Session")
            workout_note = st.text_area("Enter a workout label/title, or any relevant notes regarding this recreation session")
            st.write("")
            workout_start = st.time_input("Time of Day that you started this workout", key = "rec-start")
            workout_end = st.time_input("Time of Day that you finished this workout", key = "rec-finish")
            st.write("")
            sub_activity = st.multiselect("What type of activity did you complete?", ["Basketball", "Swimming", "Tennis", "Baseball", "Football", "Soccer", "Volleyball",
                                                                    "Tennis", "Ping Pong", "Surfing"], key = "rec-sub")
            st.caption("Select multiple if applicable")
            sub_act_metric = 0
            st.write("")
            intensity_level = st.select_slider('Indicate the overall intesity level of your recreation session',
                                        options=['Recovery', 'Comfortable','High Performance', 'Complete Exhaustion'])

            calorie_burn = st.number_input("How many calories did you burn?", min_value = 0, max_value = 10000, key = "strength-cal")
            st.caption("If unsure, just estimate")

            if st.form_submit_button("Submit Recreation Entry"):
                    fixed_date = json.dumps(now, indent=4, sort_keys=True, default=str)
                    fixed_time_initial = json.dumps(workout_start, indent=4, sort_keys=True, default=str)
                    fixed_time_final = json.dumps(workout_end, indent=4, sort_keys=True, default=str)
                    
                    func_call = workout_df()
                    user_data_before = func_call[func_call["user"] == username]
                    log_num = len(user_data_before) + 1
                    key = f"workout-{log_num}-{username}"

                    insert_workout(key, username, fixed_date, fixed_time_initial, fixed_time_final, "Recreation", sub_activity, 
                                    calorie_burn, sub_act_metric, intensity_level)
                    st.success("Recreation Entry Submitted")


            












                    




            



