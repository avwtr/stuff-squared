import streamlit as st
import streamlit_authenticator as stauth
from streamlit_option_menu import option_menu
import database as db
from create import render_create
from main import render_main

st.set_page_config(page_title='Healthviz', layout = 'wide', page_icon = 'assets/chart.png', initial_sidebar_state = 'auto')


hide_streamlit_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            </style>
            """
st.markdown(hide_streamlit_style, unsafe_allow_html=True) 


pl1= st.empty()
pl2 = st.empty()
pl3 = st.empty()
pl4 = st.empty()
pl5 = st.empty()
pl6 = st.empty()
pl7 = st.empty()
pl8 = st.empty()
pl9 = st.empty()
pl10 = st.empty()
pl11 = st.empty()


pl1.image("assets/newlogo.png")


pl2.caption("The goal of HealthViz is to be a simple, but powerful analytics/tracking tool for your health and fitness")

pl3.subheader("How it works:")
pl4.write("Log your daily workouts, meals, and mental health status")
pl5.write("On the backend, we will keep track of this data for you, and visualize your metrics on your HealthViz dashboard")

pl6.subheader("Value Proposition: ")
pl7.write("- Help users easily track key health data")
pl8.write("- Provide users with powerful insights and data visualizations regarding their health")
pl9.write("- Use quantitative insights from their health data to improve their lives, and optimize their daily regimen.")





users = db.fetch_users()
usernames = [user["key"] for user in users]
names = [user["name"] for user in users]
hashes = [user["password"] for user in users]   
authenticator = stauth.Authenticate(names, usernames, hashes, "dashboard", "cookiemonster",cookie_expiry_days = 30)
name, authentication_status, username = authenticator.login("Login", "main")
st.session_state["user"] = username
st.session_state["name"] = name



if (authentication_status == False):
    st.error("Username/password is incorrect")
if (authentication_status == None) or (authentication_status == False):
    st.subheader("New here? - Create an account below")
    render_create()
if authentication_status:
    pl1.empty()
    pl2.empty()
    pl3.empty()
    pl4.empty()
    pl5.empty()
    pl6.empty()
    pl7.empty()
    pl8.empty()
    pl9.empty()
    pl10.empty()
    pl11.empty()
    render_main(name, username)
    authenticator.logout("Logout", "sidebar")
