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
    const ctx = canvas.getContext('2d');
    const scoreEl = document.getElementById('score');
    const levelEl = document.getElementById('level');
    const hintEl = document.getElementById('hint');

    let score = 0;
    let level = 1;
    let winState = false;
    let basket = { x: 175, y: 450, w: 90, h: 15 };
    let items = [];
    let frame = 0;
    let spawnRate = 50;
    let speedMult = 1;

    function move(e) {
        let rect = canvas.getBoundingClientRect();
        let mouseX = (e.type.includes('touch') ? e.touches[0].clientX : e.clientX) - rect.left;
        basket.x = (mouseX * (canvas.width / rect.width)) - basket.w / 2;
        if (basket.x < 0) basket.x = 0;
        if (basket.x > canvas.width - basket.w) basket.x = canvas.width - basket.w;
    }

    canvas.addEventListener('mousemove', move);
    canvas.addEventListener('touchmove', (e) => { e.preventDefault(); move(e); }, {passive: false});

    function spawnItem() {
        const types = ['🎂', '🎈', '✨', '🎁', '⭐', '🧁', '🌸', '🍭'];
        items.push({
            x: Math.random() * (canvas.width - 30),
            y: -30,
            speed: (2 + Math.random() * 3) * speedMult,
            char: types[Math.floor(Math.random() * types.length)]
        });
    }

    function update() {
        if (winState) return;
        frame++;
        if (frame % spawnRate === 0) spawnItem();

        ctx.clearRect(0, 0, canvas.width, canvas.height);

        // Draw Basket (Friendly Rounded Design)
        ctx.fillStyle = '#2D5A52';
        ctx.beginPath();
        ctx.roundRect(basket.x, basket.y, basket.w, basket.h, 10);
        ctx.fill();

        // Items Logic
        for (let i = items.length - 1; i >= 0; i--) {
            let item = items[i];
            item.y += item.speed;

            ctx.font = '28px serif';
            ctx.fillText(item.char, item.x, item.y);

            // Catch Item
            if (item.y > basket.y - 10 && item.y < basket.y + basket.h && 
                item.x > basket.x - 10 && item.x < basket.x + basket.w) {
                items.splice(i, 1);
                score++;
                checkLevel();
                updateUI();
            } 
            // Miss Item (No penalty, just remove it)
            else if (item.y > canvas.height) {
                items.splice(i, 1);
            }
        }
        requestAnimationFrame(update);
    }

    function checkLevel() {
        if (score === 15 && level === 1) { level = 2; speedMult = 1.3; spawnRate = 40; }
        if (score === 30 && level === 2) { level = 3; speedMult = 1.6; spawnRate = 30; }
        if (score >= 50) triggerWin();
    }

    function updateUI() {
        scoreEl.innerText = "Points: " + score;
        levelEl.innerText = "Level: " + level;
    }

    function triggerWin() {
        winState = true;
        ctx.clearRect(0, 0, canvas.width, canvas.height);
        ctx.textAlign = 'center';
        ctx.fillStyle = '#2D5A52';
        
        ctx.font = 'bold 35px Helvetica';
        ctx.fillText("ENJOY YOUR DAY!", canvas.width/2, canvas.height/2);
        ctx.font = '18px Helvetica';
        ctx.fillText("You've collected all the joy!", canvas.width/2, canvas.height/2 + 50);
        hintEl.innerText = "🏆 SUCCESS! 🏆";
        
        // Add a small restart button just in case she wants to play again
        const btn = document.createElement("button");
        btn.innerHTML = "Play Again";
        btn.style = "margin-top:20px; padding:10px 20px; background:#2D5A52; color:white; border:none; border-radius:20px; cursor:pointer;";
        btn.onclick = () => location.reload();
        document.getElementById('ui').appendChild(btn);
    }

    update();
</script>
"""

components.html(game_html, height=680)

st.write("---")
st.markdown("<p style='text-align: center; color: #2D5A52; font-size: 0.8rem;'><b>System Status:</b> Infinite Joy Mode Enabled | No Data Loss Possible</p>", unsafe_allow_html=True)
