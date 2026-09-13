import streamlit as st
def subject_card(name, code, section, stats=None, footer_callback=None):
    html = f"""
        <div style="background:#ffffff; border-top:4px solid #ef806b; padding:1.35rem; border-radius:12px; border:1px solid #d9e1dc; margin-bottom:1rem; box-shadow:0 8px 20px rgba(16,42,42,.06)">
        <h3 style="margin:0; color:#102a2a; font-size:1.35rem">{name}</h3>
        <p style="color:#637271; margin:.65rem 0 1rem">Code: <span style="background:#b8e2d0; color:#102a2a; padding:3px 8px; border-radius:5px; font-weight:700">{code}</span> &nbsp;|&nbsp; Section: {section}</p>
        
        """
    
    if stats:
        html+= """
        <div style="display:flex; gap:8px; flex-wrap:wrap;">
        """
        for icon, label, value in stats:
            html+= f'<div style="background:#f1f5f2; color:#637271; padding:6px 10px; border-radius:7px; font-size:.9rem">{icon} <b style="color:#102a2a">{value}</b> {label}</div>'
        
        html+= "</div>"

    st.markdown(html, unsafe_allow_html=True)

    if footer_callback:
        footer_callback()