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

# --- THE STORY GAME (v15.0 - NOOR OF THE SOUL EDITION) ---
game_html = """
<div id="wrapper" style="position: relative; width: 100%; height: 600px; display: flex; flex-direction: column; align-items: center; font-family: 'Georgia', serif; overflow: hidden;">
    
    <audio id="bg-music" loop>
        <source src="https://cdn.pixabay.com/audio/2022/03/10/audio_c1e0b5d5d9.mp3" type="audio/mpeg">
    </audio>
    <audio id="catch-sound">
        <source src="https://assets.mixkit.co/active_storage/sfx/2571/2571-preview.mp3" type="audio/mpeg">
    </audio>

    <div id="story-card" style="position: absolute; width: 310px; top: 40px; background: #fff; padding: 15px 15px 60px 15px; border: 1px solid #ddd; box-shadow: 0 15px 35px rgba(0,0,0,0.2); z-index: 100; transform: rotate(-1.5deg); transition: transform 0.6s cubic-bezier(0.23, 1, 0.32, 1);">
        <div id="image-placeholder" style="width: 100%; height: 180px; background: #2D5A52; display: flex; align-items: center; justify-content: center; color: #E5E0D8; font-size: 3.5rem; border-radius: 4px;">🌙</div>
        <h3 id="card-title" style="color: #2D5A52; margin-top: 15px; margin-bottom: 5px;">Bismillah</h3>
        <p id="card-text" style="color: #555; font-size: 0.92rem; line-height: 1.5; font-style: italic;">Yeka, another year is a gift from Al-Wahhab. Tap to begin a journey through the light you bring into the world.</p>
        <button id="card-btn" onclick="startExperience()" style="position: absolute; bottom: 15px; right: 15px; background: #2D5A52; color: white; border: none; padding: 10px 20px; border-radius: 5px; cursor: pointer; font-family: 'Georgia', serif;">Begin →</button>
    </div>

    <canvas id="gameCanvas" width="400" height="500" style="background: #ffffff; border-radius: 20px; border: 4px solid #2D5A52; max-width: 95%; opacity: 0.2; transition: opacity 0.8s;"></canvas>
    
    <div id="score-ui" style="margin-top: 15px; color: #2D5A52; font-weight: bold; font-size: 1.1rem;">
        Blessings Collected: <span id="points">0</span> / 80
    </div>
</div>

<script src="https://cdn.jsdelivr.net/npm/canvas-confetti@1.5.1/dist/confetti.browser.min.js"></script>
<script>
    const canvas = document.getElementById('gameCanvas');
    const ctx = canvas.getContext('2d');
    const card = document.getElementById('story-card');
    const sTitle = document.getElementById('card-title');
    const sText = document.getElementById('card-text');
    const sImg = document.getElementById('image-placeholder');
    const pointsEl = document.getElementById('points');
    const bgMusic = document.getElementById('bg-music');
    const catchSound = document.getElementById('catch-sound');

    let score = 0;
    let active = false;
    let basket = { x: 160, y: 440, w: 90, h: 16 };
    let items = [];
    let stars = [];
    let frame = 0;

    for(let i=0; i<30; i++) {
        stars.push({ x: Math.random()*400, y: Math.random()*500, size: Math.random()*2, opacity: Math.random() });
    }

    const milestones = {
        10: { 
            title: "Your Ihsan (Excellence)", 
            text: "'Allah loves those who do good.' The way you carry yourself with such kindness is a form of worship, Yeka. May it always be your guiding light.", 
            img: "✨" 
        },
        20: { 
            title: "Your Sabr (Steadfastness)", 
            text: "'Allah is with the patient.' (2:153). Your heart remains a steady, constant light through every season. That strength is a rare and beautiful blessing.", 
            img: "🤍" 
        },
        30: { 
            title: "Your Iman (Faith)", 
            text: "Watching the way you trust in His plan is a reminder of what true faith looks like. May your heart always find its home in Noor.", 
            img: "🌙" 
        },
        40: { 
            title: "Your Sujud (Peace)", 
            text: "May every moment you spend in prayer wrap your soul in tranquility. You deserve a peace that is as deep as your devotion.", 
            img: "🤲" 
        },
        50: { 
            title: "His Qadr (Wisdom)", 
            text: "Allah is the best of planners. I am deeply grateful to His Qadr for allowing our worlds to touch and for the chance to see the goodness in you.", 
            img: "⭐" 
        },
        60: { 
            title: "Your Forgiving Nature", 
            text: "To forgive is a trait of the noble. Your ability to see the purity in others is a reflection of the purity within your own soul.", 
            img: "🍃" 
        },
        70: { 
            title: "Your Shukr (Gratitude)", 
            text: "A grateful heart is a magnet for miracles. May Allah continue to increase you in blessings for the gratitude you show every day.", 
            img: "🌸" 
        },
        80: { 
            title: "Eid Milad Yeka!", 
            text: "May this year be a testament to His mercy. May Allah grant every secret dua you've ever whispered. Happy Birthday, Yeka!", 
            img: "🎁" 
        }
    };

    function startExperience() {
        bgMusic.volume = 0.4;
        bgMusic.play();
        nextStep();
    }

    function nextStep() {
        if (score >= 80) { location.reload(); return; }
        card.style.transform =
