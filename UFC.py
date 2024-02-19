import streamlit as st
from api import get_fighter, get_upcoming_events, get_event

st.title("UFC Fighter and Event Information")

# Sidebar for navigation
page = st.sidebar.selectbox("Choose a page", ["Fighter Information", "Upcoming Events", "Event Information"])

if page == "Fighter Information":
    st.header("Fighter Information")
    fighter_query = st.text_input("Enter fighter's name:")
    if st.button("Get Fighter Information"):
        try:
            fighter_info = get_fighter(fighter_query)
            st.write(fighter_info)
        except BaseException as e:
            st.error(f"Error: {str(e)}")

elif page == "Upcoming Events":
    st.header("Upcoming Events")
    upcoming_events = get_upcoming_events()
    st.write(upcoming_events)

elif page == "Event Information":
    st.header("Event Information")
    event_query = st.text_input("Enter event name:")
    if st.button("Get Event Information"):
        try:
            event_info = get_event(event_query)
            st.write(event_info)
        except BaseException as e:
            st.error(f"Error: {str(e)}")
