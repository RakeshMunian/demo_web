import streamlit as st
st.title("Welcome all of you")
st.header("python")

st.markdown("I Love pune ")
st.code("""for I in range (1,5,1):
        print ("hello")""")
import pandas as pd

datasets = pd.read_csv("excel.csv")
st.dataframe(datasets)
name = st.text_input("Enter Your Name :")
Fname = st.text_input("Enter your Father name :")
Address = st.text_area("Enter address :")
classdata = st.selectbox("Enter your class :", (1,2,3,4,5,6,))


button = st.button("Done")
if button :
    st.markdown(f"""""
Name : {name}
Father : {Fname}
Address : {Address}
class : {classdata}""")