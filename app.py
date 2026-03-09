import streamlit as st
import streamlit.components.v1 as components

# --- PAGE CONFIG ---
st.set_page_config(page_title="A Journey for You", page_icon="✨", layout="centered")

st.markdown("""
    <style>
    .stApp { background-color: #E5E0D8; }
    .header { color: #2D5A52; text-align: center; font-family: 'Georgia', serif; font-style: italic; margin-bottom: 0; }
    .footer { text-align: center; color: #2D5A52; font-family: 'Georgia', serif; opacity: 0.6; font-size: 0.8rem; margin-top: 20px; }
    </style>
    """, unsafe_allow_html=True)

st.markdown("<h1 class='header'>The Collection of Moments</h1>", unsafe_allow_html=True)

# --- THE PREMIUM STORY GAME ---
game_html = """
<div id="wrapper" style="position: relative; width: 100%; display: flex; flex-direction: column; align-items: center; font-family: 'Georgia', serif;">
    
    <div id="story-card" style="position: absolute; width: 320px; top: 20px; background: #fff; padding: 15px 15px 60px 15px; border: 1px solid #ddd; box-shadow: 0 15px 35px rgba(0,0,0,0.2); z-index: 100; transform: rotate(-2deg); transition: all 0.5s ease;">
        <div id="image-placeholder" style="width: 100%; height: 200px; background: #2D5A52; display: flex; align-items: center; justify-content: center; color: #E5E0D8; font-size: 3rem;">✨</div>
        <h3 id="card-title" style="color: #2D5A52; margin-top: 15px;">Chapter 1</h3>
        <p id="card-text" style="color: #555; font-size: 0.95rem; line-height: 1.4;">Some people make the world brighter just by being in it. Tap to start collecting the stars.</p>
        <button onclick="nextStep()" style="position: absolute; bottom: 15px; right: 15px; background: #2D5A52; color: white; border: none; padding: 8px 20px; border-radius: 5px; cursor: pointer;">Continue →</button>
    </div>

    <canvas id="gameCanvas" width="400" height="500" style="background: #ffffff; border-radius: 20px; border: 4px solid #2D5A52; max-width: 100%; opacity: 0.3; transition: opacity 1s;"></canvas>
    
    <div id="score-ui" style="margin-top: 15px; color: #2D5A52; font-weight: bold;">Progress: <span id="points">0</span> / 40</div>
</div>

<script>
    const canvas = document.getElementById('gameCanvas');
    const ctx = canvas.getContext('2d');
    const card = document.getElementById('story-card');
    const sTitle = document.getElementById('card-title');
    const sText = document.getElementById('card-text');
    const sImg = document.getElementById('image-placeholder');
    const pointsEl = document.getElementById('points');

    let score = 0;
    let active = false;
    let basket = { x: 160, y: 440, w: 80, h: 12 };
    let items = [];
    let frame = 0;

    const milestones = {
        10: { title: "The Radiance", text: "In every environment, you're the light that balances the room. Your energy is unmatched.", img: "🌟" },
        25: { title: "The Impact", text: "I've analyzed the data: your kindness has a 100% success rate in making people's days better.", img: "💎" },
        40: { title: "The Goal", text: "You've reached the end of the journey, but the best part is just beginning...", img: "🎂" }
    };

    function nextStep() {
        if (score >= 40) { location.reload(); return; }
        card.style.transform = "translateY(-600px) rotate(10deg)";
        canvas.style.opacity = "1";
        setTimeout(() => { active = true; }, 500);
    }

    function showCard(data) {
        active = false;
        canvas.style.opacity = "0.3";
        sTitle.innerText = data.title;
        sText.innerText = data.text;
        sImg.innerText = data.img;
        card.style.transform = "translateY(0) rotate(" + (Math.random() * 6 - 3) + "deg)";
    }

    // Controls
    function move(e) {
        if (!active) return;
        let rect = canvas.getBoundingClientRect();
        let x = (e.type.includes('touch') ? e.touches[0].clientX : e.clientX) - rect.left;
        basket.x = (x * (canvas.width / rect.width)) - basket.w / 2;
    }
    canvas.addEventListener('mousemove', move);
    canvas.addEventListener('touchmove', (e) => { e.preventDefault(); move(e); }, {passive: false});

    function update() {
        if (active) {
            frame++;
            if (frame % 40 === 0) {
                items.push({ x: Math.random() * 370, y: -20, char: ['🌸','✨','🍰','⭐'][Math.floor(Math.random()*4)] });
            }
            ctx.clearRect(0, 0, canvas.width, canvas.height);
            ctx.fillStyle = '#2D5A52';
            ctx.roundRect(basket.x, basket.y, basket.w, basket.h, 5);
            ctx.fill();

            for (let i = items.length - 1; i >= 0; i--) {
                items[i].y += 4;
                ctx.font = '24px serif';
                ctx.fillText(items[i].char, items[i].x, items[i].y);

                if (items[i].y > basket.y && items[i].x > basket.x && items[i].x < basket.x + basket.w) {
                    items.splice(i, 1);
                    score++;
                    pointsEl.innerText = score;
                    if (milestones[score]) showCard(milestones[score]);
                } else if (items[i].y > 500) items.splice(i, 1);
            }
        }
        requestAnimationFrame(update);
    }
    update();
</script>
"""

components.html(game_html, height=650)

st.markdown("<p class='footer'>Designed for a very special person. <br> <i>May your year be full of beautiful data.</i></p>", unsafe_allow_html=True)
