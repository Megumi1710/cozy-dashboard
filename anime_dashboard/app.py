import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import json
import random
import os
from streamlit_lottie import st_lottie
from PIL import Image


# =========================
# PAGE CONFIG
# =========================

st.set_page_config(
    page_title="Cozy Anime Dashboard",
    page_icon="🌸",
    layout="wide"
)


# =========================
# CUSTOM CSS
# =========================

st.markdown(
    """
    <style>

    .stApp {
        background: linear-gradient(to bottom right, #ffe6f2, #f5e6ff);
    }

    h1,h2,h3 {
        color: #ff66b2;
        font-family: cursive;
    }

    .stButton>button {
        background-color: #ffb6d9;
