import streamlit as st
from streamlit_option_menu import option_menu
from healthviz import render_healthviz
from logdaily import render_logdaily
from logfood import render_logfood
from logmental import render_mental
from myprofile import render_myprof

def render_main(name, username):
    with st.sidebar:
        selected = option_menu(
            menu_title = None,
            options = ["My HealthViz", "Log Daily Activity", "Log Food Intake", "Log Mental Health", "My Profile"],
            icons = ["house", "activity", "cup-straw", "yin-yang", "person"]
        )

    if selected == "My HealthViz":
        render_healthviz(name, username)
    if selected == "Log Daily Activity":
        render_logdaily(name, username)
    if selected == "Log Food Intake":
        render_logfood(name, username)
    if selected == "Log Mental Health":
        render_mental(name, username)
    if selected == "My Profile":
        render_myprof(name, username)

