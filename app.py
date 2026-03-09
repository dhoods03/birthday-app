import streamlit as st
import time
import pandas as pd

# Set Page Config for Mobile & Web
st.set_page_config(page_title="Signal Analysis v2.0", page_icon="📟")

# --- CUSTOM CSS: EMERALD & SAND THEME ---
st.markdown("""
    <style>
    .stApp { background-color: #E5E0D8; }
    .title-text { 
        color: #2D5A52; 
        font-family: 'Courier New', monospace; 
        text-align: center; 
        border-bottom: 2px solid #2D5A52; 
        padding-bottom: 10px;
        margin-bottom: 20px;
    }
    .metric-box { 
        background-color: #ffffff; 
        padding: 20px; 
        border-radius: 12px; 
        border-left: 6px solid #2D5A52; 
        margin: 10px 0;
        box-shadow: 2px 2px 10px rgba(0,0,0,0.05);
    }
    .metric-title { color: #2D5A52; font-weight: bold; font-size: 0.9rem; text-transform: uppercase; }
    .metric-value { color: #1a1a1a; font-size: 1.1rem; }
    .reveal-text { 
        color: #2D5A52; 
        font-size: 3.5rem; 
        font-weight: bold; 
        text-align: center; 
        margin-top: 40px; 
        letter-spacing: 4px;
        line-height: 1.2;
    }
    /* Button Styling */
    .stButton>button {
        background-color: #2D5A52 !important;
        color: white !important;
        border-radius: 20px !important;
        width: 100%;
    }
    </style>
    """, unsafe_allow_html=True)

# Initialize Session State
if 'stage' not in st.session_state:
    st.session_state.stage = 'start'

# --- HEADER ---
st.markdown("<h1 class='title-text'>SYSTEM: ATTRIBUTE ANALYZER</h1>", unsafe_allow_html=True)

# --- STAGE 1: INITIALIZATION ---
if st.session_state.stage == 'start':
    st.write("### Welcome, Subject 001.")
    st.info("Biometric scan required to access encrypted birthday data.")
    if st.button("INITIALIZE SCAN SEQUENCE"):
        st.session_state.stage = 'scanning'
        st.rerun()

# --- STAGE 2: DATA PROCESSING ---
elif st.session_state.stage == 'scanning':
    progress_bar = st.progress(0)
    status_text = st.empty()
    
    # Simulating data crunching
    steps = [
        ("Accessing Neural Network...", 20),
        ("Calibrating Aesthetic Sensors...", 45),
        ("Computing Kindness Variance...", 70),
        ("Stabilizing Output Signal...", 100)
    ]
    
    for text, percent in steps:
        status_text.text(text)
        progress_bar.progress(percent)
        time.sleep(1.0)
    
    st.session_state.stage = 'results'
    st.rerun()

# --- STAGE 3: THE DATA SUMMARY ---
elif st.session_state.stage == 'results':
    st.subheader("📊 Subject Analysis Report")
    
    # Displaying metrics in a clean grid
    c1, c2 = st.columns(2)
    with c1:
        st.markdown("""<div class='metric-box'><div class='metric-title'>Kindness Quotient</div>
                    <div class='metric-value'>99.9th Percentile</div></div>""", unsafe_allow_html=True)
        st.markdown("""<div class='metric-box'><div class='metric-title'>Intelligence</div>
                    <div class='metric-value'>System Maximum</div></div>""", unsafe_allow_html=True)
    with c2:
        st.markdown("""<div class='metric-box'><div class='metric-title'>Aesthetic Symmetry</div>
                    <div class='metric-value'>Perfect Match</div></div>""", unsafe_allow_html=True)
        st.markdown("""<div class='metric-box'><div class='metric-title'>Future Outlook</div>
                    <div class='metric-value'>Exceptionally Bright</div></div>""", unsafe_allow_html=True)
    
    st.divider()
    if st.button("EXECUTE FINAL REVEAL"):
        st.session_state.stage = 'reveal'
        st.rerun()

# --- STAGE 4: THE PERMANENT REVEAL ---
elif st.session_state.stage == 'reveal':
    st.balloons()
    st.markdown("<h1 class='reveal-text'>ENJOY YOUR DAY!</h1>", unsafe_allow_html=True)
    st.markdown("<p style='text-align:center; color:#2D5A52; font-size: 1.2rem; font-family: monospace;'>[ SIGNAL STABLE | ACCESS GRANTED ]</p>", unsafe_allow_html=True)
    
    st.write("---")
    st.write("### Note from the Developer:")
    st.write("You are the best data point I've ever analyzed. Have an amazing birthday.")
    
    if st.button("Restart Scan"):
        st.session_state.stage = 'start'
        st.rerun()
