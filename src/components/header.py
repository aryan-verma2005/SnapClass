import streamlit as st
from pathlib import Path
import base64


def header_home():
    logo_url = "https://i.ibb.co/YTYGn5qV/logo.png"

    st.markdown(f"""
        <div style="display:flex; flex-direction:column; align-items:center; justify-content:center; margin:1rem 0 2.5rem">
            <img src='{logo_url}' style='height:96px; margin-bottom:1rem' />
            <h1 class='snapclass-home-title'>SNAP<br/>CLASS</h1>
        </div>   
                
                """, unsafe_allow_html=True)

def header_dashboard():
    logo_url = "https://i.ibb.co/YTYGn5qV/logo.png"
    st.markdown(f"""
        <div style="display:flex; align-items:center; justify-content:center; gap:12px; margin-bottom:1rem">
            <img src='{logo_url}' style='height:70px;' />
            <h2 style='text-align:left; color:#102a2a; margin:0'>SNAP<br/>CLASS</h2>
        </div>   
                
                """, unsafe_allow_html=True)