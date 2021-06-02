import streamlit as st

def Footer():
    hide_streamlit_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            footer:after {
            content:'copyright: Ghanashyam Khanal and Dyas Utomo, 2021; Made with Streamlit';
	    visibility: visible;
	    display: block;
	    position: relative;
            text-align:center;
            color:#4A6AD0;
	    #background-color: #CBD1C3; 
	    padding: 5px;
	    top: 2px; }
            </style>
            """
    st.markdown(hide_streamlit_style, unsafe_allow_html=True) 


