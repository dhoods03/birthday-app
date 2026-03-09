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

# --- THE STORY GAME (v21.0 - FUNNY STICKERS EDITION) ---
game_html = """
<div id="wrapper" style="position: relative; width: 100%; height: 600px; display: flex; flex-direction: column; align-items: center; font-family: 'Georgia', serif; overflow: hidden; touch-action: none;">
    
    <audio id="bg-music" loop playsinline>
        <source src="https://cdn.pixabay.com/audio/2022/03/10/audio_c1e0b5d5d9.mp3" type="audio/mpeg">
    </audio>
    <audio id="catch-sound" playsinline>
        <source src="https://assets.mixkit.co/active_storage/sfx/2571/2571-preview.mp3" type="audio/mpeg">
    </audio>

    <div id="story-card" style="position: absolute; width: 310px; top: 40px; background: #fff; padding: 15px 15px 60px 15px; border: 1px solid #ddd; box-shadow: 0 15px 35px rgba(0,0,0,0.2); z-index: 100; transform: rotate(-1.5deg); transition: transform 0.5s cubic-bezier(0.175, 0.885, 0.32, 1.275);">
        <div id="image-placeholder" style="width: 100%; height: 180px; background: #2D5A52; display: flex; align-items: center; justify-content: center; color: #E5E0D8; font-size: 3.5rem; border-radius: 4px;">🌙</div>
        <h3 id="card-title" style="color: #2D5A52; margin-top: 15px; margin-bottom: 5px;">Bismillah</h3>
        <p id="card-text" style="color: #555; font-size: 0.92rem; line-height: 1.5; font-style: italic;">Yeka, a soul like yours is a gift. Tap to walk through the wisdom, light, and a few random things you carry in your heart.</p>
        <button id="card-btn" onclick="startExperience()" style="position: absolute; bottom: 15px; right: 15px; background: #2D5A52; color: white; border: none; padding: 12px 24px; border-radius: 5px; cursor: pointer; font-family: 'Georgia', serif; font-size: 1rem;">Begin →</button>
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
    const card = document.getElementById('story-card');
    const sTitle = document.getElementById('card-title');
    const sText = document.getElementById('card-text');
    const sImg = document.getElementById('image-placeholder');
    const pointsEl = document.getElementById('points');
    const bgMusic = document.getElementById('bg-music');
    const catchSound = document.getElementById('catch-sound');

    let score = 0;
    let active = false;
    let basket = { x: 150, y: 440, w: 100, h: 20 };
    let items = [];
    let frame = 0;

    const milestones = {
        10: { title: "On Kindness", text: "'A good word is like a good tree...' (14:24). Your kindness is that beautiful tree, Yeka.", img: "✨" },
        20: { title: "On Sabr", text: "'Be patient with beautiful patience.' (70:5). Your strength is in how beautifully you remain steady.", img: "🤍" },
        30: { title: "On Faith", text: "'He found you lost and guided you.' (93:7). Watching you trust His light is a beautiful lesson in Iman.", img: "🌙" },
        40: { title: "On Sujud", text: "'The closest a servant comes to his Lord is when he is in Sujud.' May your prayers always be your sanctuary.", img: "🤲" },
        50: { title: "On Qadr", text: "'Allah knows, while you know not.' (2:216). Your trust in His timing is inspiring.", img: "⭐" },
        60: { title: "On Forgiveness", text: "...if a person forgives, his reward is due from Allah.' (42:40). Your noble heart is proof.", img: "🍃" },
        70: { title: "On Shukr", text: "'If you are grateful, I will surely increase you.' (14:7). May Allah multiply your joy.", img: "🌸" },
        80: { title: "Eid Milad Yeka!", text: "May Allah grant every secret dua you've ever whispered. Happy Birthday, Yeka!", img: "🎁" }
    };

    const funnyStickers = ['😴', '🫠', '😎', '🍕', '🐱', '🥑', '💨'];

    function startExperience() {
        bgMusic.muted = false;
        catchSound.muted = false;
        bgMusic.play().catch(e => console.log("Audio play blocked"));
        card.style.transform = "translateY(-800px) scale(0.5)";
        canvas.style.opacity = "1";
        setTimeout(() => { active = true; }, 500);
    }

    function showCard(data) {
        active = false;
        canvas.style.opacity = "0.2";
        sTitle.innerText = data.title;
        sText.innerText = data.text;
        sImg.innerText = data.img;
        card.style.transform = "translateY(0) scale(1) rotate(" + (Math.random() * 4 - 2) + "deg)";
        if(score >= 80) triggerFinalConfetti();
    }

    function triggerFinalConfetti() {
        confetti({ particleCount: 150, spread: 70, origin: { y: 0.6 } });
        document.getElementById('card-btn').innerText = "Replay Journey";
    }

    function handleTouch(e) {
        if (!active) return;
        let rect = canvas.getBoundingClientRect();
        let touchX = e.touches[0].clientX - rect.left;
        let scaleX = canvas.width / rect.width;
        basket.x = (touchX * scaleX) - basket.w / 2;
    }

    canvas.addEventListener('touchmove', (e) => { e.preventDefault(); handleTouch(e); }, {passive: false});
    canvas.addEventListener('mousemove', (e) => { 
        let rect = canvas.getBoundingClientRect();
        basket.x = ((e.clientX - rect.left) * (canvas.width / rect.width)) - basket.w / 2;
    });

    function update() {
        ctx.clearRect(0, 0, canvas.width, canvas.height);
        if (active) {
            frame++;
            if (frame % 22 === 0) {
                let isFunny = Math.random() > 0.8;
                items.push({ 
                    x: Math.random() * 370, 
                    y: -20, 
                    char: isFunny ? funnyStickers[Math.floor(Math.random()*funnyStickers.length)] : ['🌸','🌙','🎁','🤲','⭐'][Math.floor(Math.random()*5)],
                    type: isFunny ? 'joke' : 'blessing'
                });
            }
            
            ctx.fillStyle = '#2D5A52';
            ctx.beginPath(); ctx.roundRect(basket.x, basket.y, basket.w, basket.h, 10); ctx.fill();

            for (let i = items.length - 1; i >= 0; i--) {
                items[i].y += 7; 
                ctx.font = '32px serif';
                ctx.fillText(items[i].char, items[i].x, items[i].y);
                
                if (items[i].y > basket.y && items[i].y < basket.y + 25 &&
                    items[i].x > basket.x - 15 && items[i].x < basket.x + basket.w + 15) {
                    
                    if(items[i].type === 'blessing') {
                        catchSound.currentTime = 0;
                        catchSound.play();
                        score++;
                        pointsEl.innerText = score;
                        if (milestones[score]) showCard(milestones[score]);
                    }
                    items.splice(i, 1);
                } else if (items[i].y > 520) items.splice(i, 1);
            }
        }
        requestAnimationFrame(update);
    }
    update();
</script>
"""

components.html(game_html, height=650)

st.markdown("<p class='footer'>Eid Milad Yeka! <br> <i>Wisdom, Light, and a sleepy cat.</i></p>", unsafe_allow_html=True)
