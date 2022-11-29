import streamlit as st
from dalle import img_gen
from database import insert_case
from datetime import datetime
import json

st.set_page_config(page_title='portal', page_icon = 'assets/portal-favi.png')

hide_streamlit_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            </style>
            """
st.markdown(hide_streamlit_style, unsafe_allow_html=True) 
now = datetime.now()
fixed = json.dumps(now, indent=4, sort_keys=True, default=str)

h1, h2, h3 = st.columns(3)
with h1:
    st.write("")
with h2: 
    st.image("assets/portal.png")
    st.write("")
    st.write("")
    st.write("The portal uses machine learning to turn your prompt (text), into a unique, AI generated image")
    st.caption("Ex: 'A unicorn on mars'")
with h3:
    st.write("")
st.write("")
st.write("")
b1, b2, b3 = st.columns(3)
with b1: 
    st.write("")
with b2: 
    prompt = st.text_input("Enter your prompt")
    st.write("")
    st.write("")
    submit = st.button("Generate my Image")
with b3: 
    st.write("")
if submit: 
    with b2: 
        resp = img_gen(prompt)
        st.write("")
        st.write("")
        st.image(resp)
        st.caption(prompt)
        insert_case(prompt, fixed)
