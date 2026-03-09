import streamlit as st
import streamlit.components.v1 as components

# --- PAGE CONFIG ---
st.set_page_config(page_title="A Tiny Journey", page_icon="📖", layout="centered")

st.markdown("""
    <style>
    .stApp { background-color: #E5E0D8; }
    .header { color: #2D5A52; text-align: center; font-family: 'Georgia', serif; font-style: italic; }
    </style>
    """, unsafe_allow_html=True)

st.markdown("<h1 class='header'>The Journey of Joy</h1>", unsafe_allow_html=True)

# --- THE STORY GAME (HTML5/JS) ---
game_html = """
<div id="game-wrapper" style="background: #E5E0D8; display: flex; flex-direction: column; align-items: center; font-family: 'Georgia', serif; touch-action: none;">
    
    <div id="story-overlay" style="position: absolute; width: 350px; height: 450px; background: rgba(255,255,255,0.95); border: 3px solid #2D5A52; border-radius: 20px; z-index: 10; display: flex; flex-direction: column; align-items: center; justify-content: center; padding: 20px; text-align: center; box-shadow: 0 10px 30px rgba(0,0,0,0.1);">
        <h2 id="story-title" style="color: #2D5A52;">Chapter 1</h2>
        <p id="story-text" style="color: #444; line-height: 1.6;">Once upon a time, a very special person had a birthday... Tap to start the collection!</p>
        <button onclick="closeStory()" style="background: #2D5A52; color: white; border: none; padding: 10px 25px; border-radius: 20px; cursor: pointer; font-family: serif;">Continue</button>
    </div>

    <canvas id="gameCanvas" width="400" height="500" style="background: #ffffff; border: 4px solid #2D5A52; border-radius: 15px; max-width: 100%;"></canvas>
    
    <div id="ui" style="margin-top: 15px; color: #2D5A52; text-align: center;">
        <span id="score" style="font-weight: bold; font-size: 1.2rem;">Collected: 0 / 50</span>
    </div>
</div>

<script>
    const canvas = document.getElementById('gameCanvas');
    const ctx = canvas.getContext('2d');
    const overlay = document.getElementById('story-overlay');
    const sTitle = document.getElementById('story-title');
    const sText = document.getElementById('story-text');
    const scoreEl = document.getElementById('score');

    let score = 0;
    let isPaused = true;
    let basket = { x: 160, y: 450, w: 80, h: 15 };
    let items = [];
    let frame = 0;

    const storyNodes = {
        15: { title: "The Spark", text: "You bring so much energy into the world. Every smile you share is like a data point of pure happiness." },
        30: { title: "The Constant", text: "In a world of variables, your kindness is the one thing that never changes. You're truly one of a kind." },
        45: { title: "The Horizon", text: "The next chapter of your life is going to be the best one yet. Are you ready for the final surprise?" }
    };

    function move(e) {
        if (isPaused) return;
        let rect = canvas.getBoundingClientRect();
        let mouseX = (e.type.includes('touch') ? e.touches[0].clientX : e.clientX) - rect.left;
        basket.x = (mouseX * (canvas.width / rect.width)) - basket.w / 2;
    }

    canvas.addEventListener('mousemove', move);
    canvas.addEventListener('touchmove', (e) => { e.preventDefault(); move(e); }, {passive: false});

    function closeStory() {
        overlay.style.display = "none";
        isPaused = false;
        if (score >= 50) location.reload(); // Reset if finished
    }

    function triggerStory(node) {
        isPaused = true;
        sTitle.innerText = node.title;
        sText.innerText = node.text;
        overlay.style.display = "flex";
    }

    function spawnItem() {
        const icons = ['✨', '🌸', '🎁', '🍰', '⭐'];
        items.push({
            x: Math.random() * (canvas.width - 30),
            y: -20,
            speed: 3,
            char: icons[Math.floor(Math.random() * icons.length)]
        });
    }

    function update() {
        if (!isPaused) {
            frame++;
            if (frame % 45 === 0) spawnItem();
            ctx.clearRect(0, 0, canvas.width, canvas.height);

            // Basket
            ctx.fillStyle = '#2D5A52';
            ctx.beginPath();
            ctx.roundRect(basket.x, basket.y, basket.w, basket.h, 10);
            ctx.fill();

            // Items
            for (let i = items.length - 1; i >= 0; i--) {
                let it = items[i];
                it.y += it.speed;
                ctx.font = '24px serif';
                ctx.fillText(it.char, it.x, it.y);

                if (it.y > basket.y && it.x > basket.x && it.x < basket.x + basket.w) {
                    items.splice(i, 1);
                    score++;
                    scoreEl.innerText = "Collected: " + score + " / 50";
                    if (storyNodes[score]) triggerStory(storyNodes[score]);
                    if (score >= 50) win();
                } else if (it.y > canvas.height) {
                    items.splice(i, 1);
                }
            }
        }
        requestAnimationFrame(update);
    }

    function win() {
        isPaused = true;
        sTitle.innerText = "HAPPY BIRTHDAY!";
        sText.innerHTML = "<b style='font-size: 1.5rem;'>ENJOY YOUR DAY!</b><br><br>You've completed the journey. May your year be as wonderful as you are.";
        overlay.style.display = "flex";
    }

    update();
</script>
"""

components.html(game_html, height=650)

st.write("---")
st.markdown("<p style='text-align: center; color: #2D5A52; font-family: serif; opacity: 0.8;'><i>“The best data points in life aren't numbers, they're moments.”</i></p>", unsafe_allow_html=True)
