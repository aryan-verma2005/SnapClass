import streamlit as st



def style_background_home():

    st.markdown("""
        <style>

                .stApp {
                    background: #5865F2 !important;
                }

                .stApp div[data-testid="stColumn"]{
                    background-color: transparent !important;
                    padding: 0 !important;
                    }
        </style>  

                """
            ,unsafe_allow_html=True)
    

def style_background_dashboard():

    st.markdown("""
        <style>

                .stApp {
                    background: #E0E3FF !important;
                }

        </style>  

                """
            ,unsafe_allow_html=True)
    

    

def style_base_layout():
# asdasd
    st.markdown("""
        <style>
        @import url('https://fonts.googleapis.com/css2?family=Climate+Crisis:YEAR@1979&display=swap');
        @import url('https://fonts.googleapis.com/css2?family=Outfit:wght@100..900&display=swap');

                
         /* Hide Top Bar of streamlit */
                
            #MainMenu, footer, header {
                visibility: hidden;
            }
                
            .block-container {
                padding-top:1.5rem !important;    
            }

            h1 {
                font-family: 'Climate Crisis', sans-serif !important;
                font-size: 3.5rem !important;
                line-height: 1.1 !important;
                margin-bottom:0rem !important;
            }
                

            h2 {
                font-family: 'Climate Crisis', sans-serif !important;
                font-size: 2rem !important;
                line-height:0.9 !important;
                margin-bottom:0rem !important;
            }

            h1, h2 {
                color: #111111 !important;
                text-align: center !important;
            }
                
            h3, h4, p {
                font-family: 'Outfit', sans-serif;    
            }
                

            .stButton > button{
                border-radius: 1.5rem !important;
                background-color: #EB459E !important;
                color: white !important;
                min-height: 50px !important;
                height: 50px !important;
                width: 155px !important;
                padding: 0.35rem 0.75rem !important;
                border: none !important;
                font-family: 'Outfit', sans-serif !important;
                font-size: 1rem !important;
                transition: transform 0.25s ease-in-out !important;
                }

            .stButton > button:hover{
                transform: scale(1.05) !important;
                background-color: #EB459E !important;
                color: white !important;
            }
        </style>  

                """
            ,unsafe_allow_html=True)