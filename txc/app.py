import streamlit as st
import page_home
import page_model

all_pages = [
        ["Prediction", page_home.app],
        ["Project Description and code", page_model.app]
        ]

def main():
    pages = []
    for page in all_pages:
        pages.append( {"title":page[0], "app":page[1]}  )
    app = st.sidebar.radio('Go To', pages, format_func = lambda app: app["title"])
    app['app']()
    st.sidebar.markdown("**Project work for Pilot-NLP Bootcamp, April 2021, The Erdos Institute**")
    st.sidebar.title("Team Members")
    st.sidebar.write("[Ghanashyam Khanal](https://www.linkedin.com/in/ghanashyam-khanal/)")
    st.sidebar.write("[Dyas Utomo](https://www.linkedin.com/in/dyasutomo/)")

if __name__=="__main__":
    main()
