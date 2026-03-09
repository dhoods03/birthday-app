import streamlit as st
import streamlit.components.v1 as components

# --- PAGE CONFIG ---
st.set_page_config(page_title="The Birthday Quest", page_icon="🎁", layout="centered")

st.markdown("""
    <style>
    .stApp { background-color: #E5E0D8; }
    .header { color: #2D5A52; text-align: center; font-family: 'Helvetica', sans-serif; }
    </style>
    """, unsafe_allow_html=True)

st.markdown("<h1 class='header'>THE JOY COLLECTOR</h1>", unsafe_allow_html=True)

game_html = """
<div id="game-container" style="background: #E5E0D8; display: flex; flex-direction: column; align-items: center; font-family: sans-serif; touch-action: none;">
    <canvas id="gameCanvas" width="400" height="500" style="background: #ffffff; border: 4px solid #2D5A52; border-radius: 15px; cursor: crosshair; max-width: 100%; box-shadow: 0 10px 30px rgba(0,0,0,0.1);"></canvas>
    <div id="ui" style="margin-top: 15px; color: #2D5A52; text-align: center; width: 100%;">
        <div style="display: flex; justify-content: center; gap: 40px; font-weight: bold; font-size: 1.2rem;">
            <span id="score">Points: 0</span>
            <span id="level">Level: 1</span>
        </div>
        <p id="hint" style="margin-top: 10px; font-style: italic;">Collect 50 items to unlock your message!</p>
    </div>
</div>

<script>
    const canvas = document.getElementById('gameCanvas');
    const ctx = canvas.getContext('2d
