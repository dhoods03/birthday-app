import streamlit as st
import streamlit.components.v1 as components

# --- PAGE CONFIG ---
st.set_page_config(page_title="A Journey for Yeka", page_icon="✨", layout="centered")

st.markdown("""
    <style>
    .stApp { background-color: #E5E0D8; }
    .header { color: #2D5A52; text-align: center; font-family: 'Georgia', serif; font-style: italic; margin-bottom: 0; }
    .footer { text-align: center; color: #2D5A52; font-family: 'Georgia', serif; opacity: 0.8; font-size: 0.8rem; margin-top: 20px; }
    </style>
    """, unsafe_allow_html=True)

st.markdown("<h1 class='header'>A Journey of Blessings</h1>", unsafe_allow_html=True)

# --- THE STORY GAME (v18.0 - AUDIO OVERRIDE) ---
game_html = """
<div id="wrapper" style="position: relative; width: 100%; height: 600px; display: flex; flex-direction: column; align-items: center; font-family: 'Georgia', serif; overflow: hidden; touch-action: none;">
    
    <audio id="bg-music" loop playsinline>
        <source src="https://www.soundhelix.com/examples/mp3/SoundHelix-Song-17.mp3" type="audio/mpeg">
    </audio>
    <audio id="catch-sound" playsinline>
        <source src="https://assets.mixkit.co/active_storage/sfx/2571/2571-preview.mp3" type="audio/mpeg">
    </audio>

    <div id="mute-btn" onclick="toggleMute()" style="position: absolute; bottom: 80px; left: 20px; z-index: 1000; background: rgba(45, 90, 82, 0.7); color: white; padding: 8px; border-radius: 50%; cursor: pointer; width: 30px; height: 30px; display: flex; align-items: center; justify-content: center; font-size: 1.2rem;">🔇</div>

    <div id="story-card" style="position: absolute; width: 310px; top: 40px; background: #fff; padding: 15px 15px 60px 15px; border: 1px solid #ddd; box-shadow: 0 15px 35px rgba(0,0,0,0.2); z-index: 100; transform: rotate(-1.5deg); transition: transform 0.5s;">
        <div id="image-placeholder" style="width: 100%; height: 180px; background: #2D5A52; display: flex; align-items: center; justify-content: center; color: #E5E0D8; font-size: 3.5rem; border-radius: 4px;">🌙</div>
        <h3 id="card-title" style="color: #2D5A52; margin-top: 15px; margin-bottom: 5px;">Bismillah</h3>
        <p id="card-text" style="color: #555; font-size: 0.92rem; line-height: 1.5; font-style: italic;">Yeka, a soul like yours is a gift. Tap to begin.</p>
        <button id="card-btn" onclick="startExperience()" style="position: absolute; bottom: 15px; right: 15px; background: #2D5A52; color: white; border: none; padding: 12px 24px; border-radius: 5px; cursor: pointer;">Begin →</button>
    </div>

    <canvas id="gameCanvas" width="400" height="500" style="background: #ffffff; border-radius: 20px; border: 4px solid #2D5A52; max-width: 95%; opacity: 0.2; transition: opacity 0.5s;"></canvas>
    
    <div id="score-ui" style="margin-top: 15px; color: #2D5A52; font-weight: bold; font-size: 1.1rem;">
        Blessings Collected: <span id="points">0</span> / 80
    </div>
</div>

<script src="https://cdn.jsdelivr.net/npm/canvas-confetti@1.5.1/dist/confetti.browser.min.js"></script>
<script>
    const canvas = document.getElementById('gameCanvas');
    const ctx = canvas.getContext('2d');
    const bgMusic = document.getElementById('bg-music');
    const catchSound = document.getElementById('catch-sound');
    const muteBtn = document.getElementById('mute-btn');
    const card = document.getElementById('story-card');
    
    let isMuted = true;
    let score = 0;
    let active = false;
    let basket = { x: 150, y: 440, w: 100, h: 20 };
    let items = [];

    function toggleMute() {
        isMuted = !isMuted;
        bgMusic.muted = isMuted;
        catchSound.muted = isMuted;
        muteBtn.innerText = isMuted ? "🔇" : "🔊";
        if (!isMuted) bgMusic.play();
    }

    function startExperience() {
        // Essential for iOS: Audio must be triggered by a click
        bgMusic.muted = false;
        isMuted = false;
        muteBtn.innerText = "🔊";
        
        let playPromise = bgMusic.play();
        if (playPromise !== undefined) {
            playPromise.then(_ => {
                console.log("Audio playing");
            }).catch(error => {
                console.log("Autoplay prevented, user must tap mute icon");
            });
        }
        
        card.style.transform = "translateY(-800px)";
        canvas.style.opacity = "1";
        setTimeout(() => { active = true; }, 500);
    }

    // [Rest of the movement and milestone logic remains the same as v17.0]
    // ... (logic abbreviated for clarity, but include your milestone text here)
</script>
"""
