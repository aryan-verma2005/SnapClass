import streamlit as st


def style_background_home():
    st.markdown("""
        <style>
            .stApp { background: #102a2a !important; }
            .stApp div[data-testid="stColumn"] {
                background: #f7f5ef !important;
                border: 1px solid rgba(247, 245, 239, 0.18) !important;
                border-radius: 18px !important;
                padding: 2rem !important;
            }
        </style>
    """, unsafe_allow_html=True)


def style_background_dashboard():
    st.markdown("""
        <style>
            .stApp { background: #f7f5ef !important; }
        </style>
    """, unsafe_allow_html=True)


def style_base_layout():
    st.markdown("""
        <style>
            @import url('https://fonts.googleapis.com/css2?family=DM+Sans:wght@400;500;600;700&family=Space+Grotesk:wght@500;600;700&display=swap');

            :root {
                --ink: #102a2a;
                --muted: #637271;
                --paper: #f7f5ef;
                --panel: #ffffff;
                --mint: #b8e2d0;
                --coral: #ef806b;
                --line: #d9e1dc;
            }

            #MainMenu, footer, header { visibility: hidden; }
            .stApp, [data-testid="stAppViewContainer"] {
                color: var(--ink);
                font-family: 'DM Sans', sans-serif;
            }
            .block-container {
                max-width: 1180px !important;
                padding: 2.5rem 2rem 3rem !important;
            }
            h1, h2, h3, h4 {
                color: var(--ink) !important;
                font-family: 'Space Grotesk', sans-serif !important;
                letter-spacing: 0 !important;
            }
            h1 { font-size: clamp(2.5rem, 5vw, 4.5rem) !important; line-height: 0.98 !important; }
            h2 { font-size: 2rem !important; line-height: 1.05 !important; }
            h3 { font-size: 1.25rem !important; }
            .snapclass-home-title {
                color: #ef806b !important;
                margin: 0 !important;
                text-align: center;
                text-shadow: 3px 3px 0 #b8e2d0;
            }
            p, label, [data-testid="stCaptionContainer"] { color: var(--muted); }
            [data-testid="stDivider"] { border-color: var(--line) !important; }

            button {
                min-height: 2.7rem !important;
                border-radius: 9px !important;
                border: 1px solid var(--ink) !important;
                background: var(--ink) !important;
                color: #ffffff !important;
                font-family: 'DM Sans', sans-serif !important;
                font-weight: 700 !important;
                transition: transform 160ms ease, box-shadow 160ms ease !important;
            }
            button[kind="secondary"] {
                background: var(--coral) !important;
                border-color: var(--coral) !important;
                color: var(--ink) !important;
            }
            button[kind="tertiary"] {
                background: transparent !important;
                border-color: var(--line) !important;
                color: var(--ink) !important;
            }
            button:hover {
                transform: translateY(-2px) !important;
                box-shadow: 0 5px 0 rgba(16, 42, 42, 0.16) !important;
            }
            input, textarea, [data-baseweb="select"] > div {
                border-radius: 9px !important;
                border-color: var(--line) !important;
                background: var(--panel) !important;
            }
            [data-testid="stCameraInput"], [data-testid="stFileUploader"] {
                border: 1px dashed #a9bbb3 !important;
                border-radius: 12px !important;
                background: rgba(184, 226, 208, 0.2) !important;
            }
            @media (max-width: 640px) {
                .block-container { padding: 1.25rem 1rem 2rem !important; }
                .stApp div[data-testid="stColumn"] { padding: 1.25rem !important; }
            }
        </style>
    """, unsafe_allow_html=True)