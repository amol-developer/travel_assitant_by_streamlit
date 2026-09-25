import streamlit as st
import truststore
truststore.inject_into_ssl()
from google import genai
from dotenv import load_dotenv
import time
load_dotenv()

client = genai.Client()
st.set_page_config(
    page_title="developer_Amol",
    page_icon="✈️",
    layout="wide"
)

st.markdown("""
<style>
.title-box {
    background: linear-gradient(135deg, #4facfe, #00f2fe);
    padding: 25px;
    border-radius: 15px;
    text-align: center;
    margin-bottom: 25px;
    box-shadow: 0px 5px 15px rgba(0,0,0,0.2);
}

.title-box h1 {
    color: black;
    font-size: 42px;
    margin: 0;
}

.title-box p {
    color: black;
    font-size: 18px;
    margin-top: 8px;
}

.title-box h6 {
    color: green;
    font-size: 18px;
    margin-top: 8px;
</style>

<div class="title-box">
    <h1>🌍 WithTraveller</h1>
    <p>🚗 Your smart companion for planning amazing journeys</p>
    <h6>Your trip, your style, your budget 🌤️</h6>
</div>
""", unsafe_allow_html=True)






location=st.text_input("where you want to go ")
days=st.number_input("how many days to want to go for trip ",min_value=1,max_value=50)
trip_type=st.selectbox("Who are you traveling with ",["Family","solo","Friends","Partner"],placeholder="select")
trip_budgeat=st.radio("What is your budget for this trip",["Luxury","Moderate","Budget-friendly"])

with st.popover("ℹ️", ):
    st.markdown("### Budget Types")

    st.markdown("""
    **💰 Budget-Friendly**  
    Focuses on affordable hotels, public transport, and low-cost activities.

    **💳 Moderate**  
    A balance between comfort and cost, with mid-range hotels, transportation,
    and activities.

    **✨ Luxury**  
    Focuses on premium hotels, private transportation, fine dining,
    and high-end experiences.
    """)
trip_mode=st.selectbox("How will you travel on this trip",
                      ["Flight", "Train", "Bus / Travels", "Car", "Bike", "Not sure yet", "suggest the best for me"],
                      index=None,
                      placeholder="Choose a travel mode...")



if trip_mode is None:
        st.warning("⚠️ Please select at least one travel mode before continuing.")
        st.stop()
language=st.selectbox("which language do you preper ",["English","hindi","Marathi","spanish","France"])    
prompt=f"""you are an intelligent and planner .
            user wants to he/she wants to go to {location} and go for {days} days .
            user trip type : {trip_type},user budget status for trip : {trip_budgeat},
            user travel way/type : {trip_mode},answer in language : {language},
            plan a trip and share answer is bullet formate"""
if st.button("Plan trip 🧗"):
    interaction = client.interactions.create(
        model="gemini-3.5-flash-lite",
        input=prompt)
    with st.spinner("wait for it...",show_time=True):
        time.sleep(5)
    st.write("your trip location is ",location)
    st.write("you plan trip for ",days," days")
    
    st.success("ALL THE BEST for your journey ✈️ here are some fab suggestion !!")
    
    st.write(interaction.output_text)
    st.image("imagestravel.jpg",caption="Explore your nest destination")
