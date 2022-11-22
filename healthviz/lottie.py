import json
import streamlit as st
from streamlit_lottie import st_lottie

def load_lottie(path: str):
    with open(path, "r") as fi:
        return json.load(fi)