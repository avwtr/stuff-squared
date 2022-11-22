import streamlit_authenticator as stauth
import streamlit as st
import database as db
from datetime import datetime
import json


def render_create():
    with st.form(key = "create user", clear_on_submit = True):
        names = []
        usernames = [st.text_input("Create a username")]
        f_names = [st.text_input("Enter first name")]
        l_names = [st.text_input("Enter last name")]
        passwords = [st.text_input("Create a password", type = "password")]
        phone_num = [st.text_input("Enter your phone number")]
        n = f"{f_names[0]} {l_names[0]}"
        now = datetime.now()
        fixed_now = json.dumps(now, indent=4, sort_keys=True, default=str)
        names.append(n)
        hashed_passwords = [stauth.Hasher(passwords).generate()]
        if st.form_submit_button("Create my account"):
            db.insert_user(usernames[0], names[0], hashed_passwords[0][0], phone_num[0], fixed_now)