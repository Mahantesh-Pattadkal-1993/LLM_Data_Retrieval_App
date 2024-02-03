import streamlit as st
from app_helper import generate_response 

# Title of the App
st.title("Tourist name Generator")

# Sidebar with Choice for Country
Country = st.sidebar.selectbox("Pick Country of your choice", ("Brazil", "France","Italy","Switzerlnd", "England"))

# Show Response
if Country:
    response = generate_response(CountryOfChoice=Country) # get response
    st.header(response["TouristPlace"].strip()) # show "tourist place" on the app page under title
    
    itinerary = response["Itinerary"].strip().split(",") # show itineraries on the app page under title  
    st.write("***Itinerary***")

    for item in itinerary:
        st.write("- ", item)

else:  # Default selection is "Brazil"
    response = generate_response(CountryOfChoice="Brazil") # get response
    st.header(response["TouristPlace"].strip()) # show "tourist place" on the app page under title
    
    itinerary = response["Itinerary"].strip().split(",") # show itineraries on the app page under title  
    st.write("***Itinerary***")

    for item in itinerary:
        st.write("- ", item)