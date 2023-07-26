import streamlit as st
import LangChainHelper
st.title("Business Name Generator along with services")

type = st.sidebar.text_input("Enter the type of business")

if type:
    response = LangChainHelper.generate_name(type)
    st.header(response['business_name'].strip())
    services= response['services'].strip().split(",")
    st.write("-----Services-----")
    for items in services:
     st.write("-",items)
