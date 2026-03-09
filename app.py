import streamlit as st
import streamlit.components.v1 as components

# --- PAGE CONFIG ---
st.set_page_config(page_title="A Journey for Yeka", page_icon="✨", layout="centered")

st.markdown("""
    <style>
    .stApp { background-color: #E5E0D8; }
    .header { color: #2D5A52; text-align: center; font-family: 'Georgia', serif; font-style: italic; margin-bottom: 0; }
    .footer { text-align: center; color: #2D5A52; font-family: 'Georgia', serif; opacity: 0.8; font-size: 0.9rem; margin-top: 20px; }
    </style>
    """, unsafe_allow_html=True)

st.markdown("<h1 class='header'>The Collection of Moments</h1>", unsafe_allow_html=True)

# --- THE STORY GAME: EID MILAD YEKA EDITION ---
game_html = """
<div id="wrapper" style="position: relative; width: 100%; height: 600px; display: flex; flex-direction: column; align-items: center; font-family: 'Georgia', serif; overflow: hidden;">
    
    <div id="story-card" style="position: absolute; width: 300px; top: 50px; background: #fff; padding: 15px 15px 60px 15px; border: 1px solid #ddd; box-shadow: 0 15px 35px rgba(0,0,0,0.2); z-index: 100; transform: rotate(-2deg); transition: transform 0.6s cubic-bezier(0.23, 1, 0.32, 1);">
        <div id="image-placeholder" style="width: 100%; height: 180px; background: #2D5A52; display: flex; align-items: center; justify-content: center; color: #E5E0D8; font-size: 3.5rem; border-radius: 4px;">🌙</div>
        <h3 id="card-title" style="color: #2D5A52; margin-top: 15px; margin-bottom: 5px;">The Beginning</h3>
        <p id="card-text" style="color: #555; font-size: 0.95rem; line-height: 1.5; font-style: italic;">Life is a series of data points, but some points
