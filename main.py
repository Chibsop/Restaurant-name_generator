import streamlit as st
import langchainhelper

st.title("Ideal Bike Finder")

bike_help = st.text_input("Type what kind of bike you are looking for...")

if st.button("Find Bikes"):
    st.write("Finding bikes...")
    if bike_help:
        response = langchainhelper.generate_bike_name_and_items(bike_help)

        # st.header(response['bike_name_and_items']['bike_name'].strip())
        bike_items = response['bike_name_and_items'].split(",")
        st.write("BIKE ITEMS  ")
        for item in bike_items:
            st.write(f"- {item.strip()}")
    else:
        st.write("Please enter your bike requirements.")