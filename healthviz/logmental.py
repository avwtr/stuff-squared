import streamlit as st 
from streamlit_lottie import st_lottie
import requests
import json
from lottie import load_lottie
import time
from database import insert_mh
from datetime import datetime
from database import mh_df

def render_mental(name, username):
    h1, h2, h3 = st.columns(3)
    now = datetime.now()
    with h1: 
        lottie = load_lottie("lottie/mental.json")
        st_lottie(lottie, height = 100 , width = 100,key = "mental")
    with h2:
         st.header("Log Mental Health")
    with h3: 
        st.write("")
    st.write("")
    with st.form(key = "mental", clear_on_submit = True):
        one_to_ten = st.slider("On a scale from 1 - 10 how do you currently feel (10 being perfect)?", min_value  = 0, max_value = 10)
        st.write("")
        st.write("")

        emotions = st.multiselect("Select emotions that you currently feel", 
                                ["Happy", "Sad", "Angry", "Disappointed", "Excited", "Anxious", "Motivated", "Exhausted", 
                                "Unsure"])
        st.write("")
        st.write("")
        st.write("")
        note = st.text_area("Feel free to add a note to yourself. Describe how you feel, where your state of mind is, etc.")
        st.write("")
        st.write("")
        submit = st.form_submit_button("Submit mental health entry")

        if submit: 
            st.success("Entry Submitted")
            fixed = json.dumps(now, indent=4, sort_keys=True, default=str)
        
            func_call = mh_df()
            user_data_before = func_call[func_call["user"] == username]
            
            log_num = len(user_data_before) + 1
            key = f"mh-{log_num}-{username}"

            insert_mh(key, username, one_to_ten,emotions, note, fixed)

            
        