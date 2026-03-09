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

st.markdown("<h1 class='header'>A Journey of Moments</h1>", unsafe_allow_html=True)

# --- THE STORY GAME: SWEET EID MILAD YEKA EDITION ---
game_html = """
<div id="wrapper" style="position: relative; width: 100%; height: 600px; display: flex; flex-direction: column; align-items: center; font-family: 'Georgia', serif; overflow: hidden;">
    
    <div id="story-card" style="position: absolute; width: 300px; top: 50px; background: #fff; padding: 15px 15px 60px 15px; border: 1px solid #ddd; box-shadow: 0 15px 35px rgba(0,0,0,0.2); z-index: 100; transform: rotate(-2deg); transition: transform 0.6s cubic-bezier(0.23, 1, 0.32, 1);">
        <div id="image-placeholder" style="width: 100%; height: 180px; background: #2D5A52; display: flex; align-items: center; justify-content: center; color: #E5E0D8; font-size: 3.5rem; border-radius: 4px;">🌙</div>
        <h3 id="card-title" style="color: #2D5A52; margin-top: 15px; margin-bottom: 5px;">A Little Surprise</h3>
        <p id="card-text" style="color: #555; font-size: 0.95rem; line-height: 1.5; font-style: italic;">Yeka, some people make the world feel a little softer and much brighter just by being in it. Tap to begin a small journey I made for you.</p>
        <button id="card-btn" onclick="nextStep()" style="position: absolute; bottom: 15px; right: 15px; background: #2D5A52; color: white; border: none; padding: 10px 20px; border-radius: 5px; cursor: pointer; font-family: 'Georgia', serif;">Start →</button>
    </div>

    <canvas id="gameCanvas" width="400" height="500" style="background: #ffffff; border-radius: 20px; border: 4px solid #2D5A52; max-width: 95%; opacity: 0.2; transition: opacity 0.8s;"></canvas>
    
    <div id="score-ui" style="margin-top: 15px; color: #2D5A52; font-weight: bold; font-size: 1.1rem;">
        Collecting Joy: <span id="points">0</span> / 40
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

    let score = 0;
    let active = false;
    let basket = { x: 160, y: 440, w: 85, h: 14 };
    let items = [];
    let frame = 0;

    const milestones = {
        10: { title: "Your Warmth", text: "You have a way of making everything feel a bit more peaceful. Your kindness is a gift to everyone who knows you.", img: "✨" },
        25: { title: "A Rare Soul", text: "It's rare to find someone who is as brilliant as they are gentle. Thank you for being exactly who you are, Yeka.", img: "🌸" },
        40: { title: "Eid Milad Yeka!", text: "May your day be as beautiful as your heart, and may this new year bring you all the happiness you deserve.", img: "🎁" }
    };

    function nextStep() {
        if (score >= 40) { location.reload(); return; }
        card.style.transform = "translateY(-700px) rotate(10deg)";
        canvas.style.opacity = "1";
        setTimeout(() => { active = true; }, 600);
    }

    function showCard(data) {
        active = false;
        canvas.style.opacity = "0.2";
        sTitle.innerText = data.title;
        sText.innerText = data.text;
        sImg.innerText = data.img;
        card.style.transform = "translateY(0) rotate(" + (Math.random() * 6 - 3) + "deg)";
        
        if(score >= 40) {
            var duration = 5 * 1000;
            var animationEnd = Date.now() + duration;
            var defaults = { startVelocity: 30, spread: 360, ticks: 60, zIndex: 0 };
            function randomInRange(min, max) { return Math.random() * (max - min) + min; }
            var interval = setInterval(function() {
                var timeLeft = animationEnd - Date.now();
                if (timeLeft <= 0) { return clearInterval(interval); }
                var particleCount = 50 * (timeLeft / duration);
                confetti(Object.assign({}, defaults, { particleCount, origin: { x: randomInRange(0.1, 0.3), y: Math.random() - 0.2 }, colors: ['#2D5A52', '#D4AF37'] }));
                confetti(Object.assign({}, defaults, { particleCount, origin: { x: randomInRange(0.7, 0.9), y: Math.random() - 0.2 }, colors: ['#ffffff', '#2D5A52'] }));
            }, 250);
            document.getElementById('card-btn').innerText = "Play Again";
        }
    }

    function move(e) {
        if (!active) return;
        let rect = canvas.getBoundingClientRect();
        let clientX = e.touches ? e.touches[0].clientX : e.clientX;
        let x = clientX - rect.left;
        basket.x = (x * (canvas.width / rect.width)) - basket.w / 2;
        if (basket.x < 0) basket.x = 0;
        if (basket.x > canvas.width - basket.w) basket.x = canvas.width - basket.w;
    }

    canvas.addEventListener('mousemove', move);
    canvas.addEventListener('touchmove', (e) => { e.preventDefault(); move(e); }, {passive: false});

    function update() {
        if (active) {
            frame++;
            if (frame % 35 === 0) {
                items.push({ x: Math.random() * (canvas.width - 30), y: -20, char: ['🌸','🌙','🎁','🧁','⭐'][Math.floor(Math.random()*5)] });
            }
            ctx.clearRect(0, 0, canvas.width, canvas.height);
            ctx.fillStyle = '#2D5A52';
            ctx.beginPath();
            ctx.roundRect(basket.x, basket.y, basket.w, basket.h, 5);
            ctx.fill();

            for (let i = items.length - 1; i >= 0; i--) {
                items[i].y += 4;
                ctx.font = '28px serif';
                ctx.fillText(items[i].char, items[i].x, items[i].y);
                if (items[i].y > basket.y && items[i].y < basket.y + 20 &&
                    items[i].x > basket.x - 10 && items[i].x < basket.x + basket.w + 10) {
                    items.splice(i, 1);
                    score++;
                    pointsEl.innerText = score;
                    if (milestones[score]) showCard(milestones[score]);
                } else if (items[i].y > 510) { items.splice(i, 1); }
            }
        }
        requestAnimationFrame(update);
    }
    update();
</script>
"""

components.html(game_html, height=650)

st.markdown("<p class='footer'>Eid Milad Yeka! <br> <i>Sending you all the best today and always.</i></p>", unsafe_allow_html=True)
