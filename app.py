import streamlit as st
import streamlit.components.v1 as components

# --- PAGE CONFIG ---
st.set_page_config(page_title="The Birthday Quest", page_icon="🎮", layout="centered")

st.markdown("""
    <style>
    .stApp { background-color: #E5E0D8; }
    .header { color: #2D5A52; text-align: center; font-family: 'Helvetica', sans-serif; }
    </style>
    """, unsafe_allow_html=True)

st.markdown("<h1 class='header'>THE JOY COLLECTOR: PRO EDITION</h1>", unsafe_allow_html=True)

game_html = """
<div id="game-container" style="background: #E5E0D8; display: flex; flex-direction: column; align-items: center; font-family: sans-serif; touch-action: none;">
    <canvas id="gameCanvas" width="400" height="500" style="background: #ffffff; border: 4px solid #2D5A52; border-radius: 15px; cursor: crosshair; max-width: 100%; box-shadow: 0 10px 30px rgba(0,0,0,0.1);"></canvas>
    <div id="ui" style="margin-top: 15px; color: #2D5A52; text-align: center; width: 100%;">
        <div style="display: flex; justify-content: space-around; font-weight: bold; font-size: 1.2rem;">
            <span id="score">Items: 0</span>
            <span id="level">Level: 1</span>
            <span id="lives">Lives: ❤️❤️❤️</span>
        </div>
        <p id="hint" style="margin-top: 10px;">Reach 45 points for the final surprise!</p>
    </div>
</div>

<script>
    const canvas = document.getElementById('gameCanvas');
    const ctx = canvas.getContext('2d');
    const scoreEl = document.getElementById('score');
    const levelEl = document.getElementById('level');
    const livesEl = document.getElementById('lives');
    const hintEl = document.getElementById('hint');

    let score = 0;
    let level = 1;
    let lives = 3;
    let gameOver = false;
    let winState = false;
    let basket = { x: 175, y: 450, w: 80, h: 15 };
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
        const types = ['🎂', '🎈', '✨', '🎁', '⭐', '🧁'];
        items.push({
            x: Math.random() * (canvas.width - 30),
            y: -30,
            speed: (2 + Math.random() * 3) * speedMult,
            char: types[Math.floor(Math.random() * types.length)]
        });
    }

    function update() {
        if (gameOver || winState) return;
        frame++;
        if (frame % spawnRate === 0) spawnItem();

        ctx.clearRect(0, 0, canvas.width, canvas.height);

        // Draw Basket
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
            // Miss Item
            else if (item.y > canvas.height) {
                items.splice(i, 1);
                lives--;
                updateUI();
                if (lives <= 0) endGame(false);
            }
        }
        requestAnimationFrame(update);
    }

    function checkLevel() {
        if (score === 10 && level === 1) { level = 2; speedMult = 1.4; spawnRate = 35; }
        if (score === 25 && level === 2) { level = 3; speedMult = 1.8; spawnRate = 25; basket.w = 60; }
        if (score >= 45) endGame(true);
    }

    function updateUI() {
        scoreEl.innerText = "Items: " + score;
        levelEl.innerText = "Level: " + level;
        livesEl.innerText = "Lives: " + "❤️".repeat(lives);
    }

    function endGame(victory) {
        ctx.clearRect(0, 0, canvas.width, canvas.height);
        ctx.textAlign = 'center';
        ctx.fillStyle = '#2D5A52';
        
        if (victory) {
            winState = true;
            ctx.font = 'bold 35px Helvetica';
            ctx.fillText("ENJOY YOUR DAY!", canvas.width/2, canvas.height/2);
            ctx.font = '18px Helvetica';
            ctx.fillText("You mastered the levels of joy!", canvas.width/2, canvas.height/2 + 50);
            hintEl.innerText = "🏆 PERFECTION ACHIEVED 🏆";
        } else {
            gameOver = true;
            ctx.font = 'bold 30px Helvetica';
            ctx.fillText("OVAL OVERLOAD!", canvas.width/2, canvas.height/2);
            ctx.font = '16px Helvetica';
            ctx.fillText("Tap to try again and unlock the gift.", canvas.width/2, canvas.height/2 + 40);
            canvas.onclick = () => location.reload();
        }
    }

    update();
</script>
"""

components.html(game_html, height=650)

st.write("---")
st.markdown("<p style='text-align: center; color: #2D5A52;'><b>Game Data:</b> High Performance Mode | Target: 45 Points</p>", unsafe_allow_html=True)
