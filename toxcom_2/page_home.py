import streamlit as st
from footer import Footer
from model_prediction import predict

def app():
    st.title('Identify TOXIC Online comments')
    
    com = st.text_area(label="Enter your comment here.", height=20, 
            value="This is an example comment.")
    if len(com)>0:
        pred = predict(com)
        st.subheader("The comment is predicted as : "+ pred)
    Footer()
