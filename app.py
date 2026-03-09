import streamlit as st
import streamlit.components.v1 as components

# --- PAGE CONFIG ---
st.set_page_config(page_title="Birthday Catch!", page_icon="🎮", layout="centered")

st.markdown("""
    <style>
    .stApp { background-color: #E5E0D8; }
    .header { color: #2D5A52; text-align: center; font-family: 'Helvetica', sans-serif; margin-bottom: 0; }
    </style>
    """, unsafe_allow_html=True)

st.markdown("<h1 class='header'>THE JOY COLLECTOR</h1>", unsafe_allow_html=True)

# --- THE MINI GAME (HTML5 CANVAS) ---
game_html = """
<div id="game-container" style="background: #E5E0D8; display: flex; flex-direction: column; align-items: center; font-family: sans-serif; touch-action: none;">
    <canvas id="gameCanvas" width="400" height="500" style="background: #ffffff; border: 4px solid #2D5A52; border-radius: 15px; cursor: crosshair; max-width: 100%;"></canvas>
    <div id="ui" style="margin-top: 15px; color: #2D5A52; text-align: center;">
        <h2 id="score">Score: 0 / 10</h2>
        <p id="hint">Drag to catch the falling emeralds!</p>
    </div>
</div>

<script>
    const canvas = document.getElementById('gameCanvas');
    const ctx = canvas.getContext('2d');
    const scoreEl = document.getElementById('score');
    const hintEl = document.getElementById('hint');

    let score = 0;
    let gameOver = false;
    let basket = { x: 175, y: 450, w: 70, h: 20 };
    let items = [];
    let frame = 0;

    // Movement logic (Mouse & Touch)
    function move(e) {
        let rect = canvas.getBoundingClientRect();
        let root = document.documentElement;
        let mouseX = (e.type.includes('touch') ? e.touches[0].clientX : e.clientX) - rect.left;
        basket.x = mouseX - basket.w / 2;
        
        // Keep basket in bounds
        if (basket.x < 0) basket.x = 0;
        if (basket.x > canvas.width - basket.w) basket.x = canvas.width - basket.w;
    }

    canvas.addEventListener('mousemove', move);
    canvas.addEventListener('touchmove', (e) => { e.preventDefault(); move(e); }, {passive: false});

    function spawnItem() {
        const types = ['🎂', '🎈', '✨', '🎁', '⭐'];
        items.push({
            x: Math.random() * (canvas.width - 30),
            y: -30,
            speed: 2 + Math.random() * 3,
            char: types[Math.floor(Math.random() * types.length)]
        });
    }

    function update() {
        if (gameOver) return;
        frame++;
        if (frame % 40 === 0) spawnItem();

        ctx.clearRect(0, 0, canvas.width, canvas.height);

        // Draw Basket
        ctx.fillStyle = '#2D5A52';
        ctx.beginPath();
        ctx.roundRect(basket.x, basket.y, basket.w, basket.h, 10);
        ctx.fill();

        // Draw and update Items
        for (let i = items.length - 1; i >= 0; i--) {
            let item = items[i];
            item.y += item.speed;

            ctx.font = '24px serif';
            ctx.fillText(item.char, item.x, item.y);

            // Collision Check
            if (item.y > basket.y && item.y < basket.y + basket.h && 
                item.x > basket.x && item.x < basket.x + basket.w) {
                items.splice(i, 1);
                score++;
                scoreEl.innerText = "Score: " + score + " / 10";
                
                if (score >= 10) {
                    win();
                }
            } else if (item.y > canvas.height) {
                items.splice(i, 1);
            }
        }
        requestAnimationFrame(update);
    }

    function win() {
        gameOver = true;
        ctx.clearRect(0, 0, canvas.width, canvas.height);
        ctx.fillStyle = '#2D5A52';
        ctx.textAlign = 'center';
        ctx.font = 'bold 30px Helvetica';
        ctx.fillText("ENJOY YOUR DAY!", canvas.width/2, canvas.height/2);
        ctx.font = '16px Helvetica';
        ctx.fillText("You've collected enough joy for the year!", canvas.width/2, canvas.height/2 + 40);
        hintEl.innerText = "🎉 Mission Accomplished! 🎉";
    }

    update();
</script>
"""

components.html(game_html, height=650)

st.divider()
st.markdown("<p style='text-align: center; color: #2D5A52; opacity: 0.6;'>System Calibration: SUCCESS | Happiness Levels: OPTIMAL</p>", unsafe_allow_html=True)
