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

# --- THE STORY GAME (v12.0 - SACRED MELODIES EDITION) ---
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
        <p id="card-text" style="color: #555; font-size: 0.92rem; line-height: 1.5; font-style: italic;">Yeka, as you begin another year, I wanted to share some reflections on the beautiful qualities you carry. Tap to begin.</p>
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
    let basket = { x: 160, y: 440, w: 85, h: 14 };
    let items = [];
    let stars = [];
    let frame = 0;

    for(let i=0; i<30; i++) {
        stars.push({ x: Math.random()*400, y: Math.random()*500, size: Math.random()*2, opacity: Math.random() });
    }

    const milestones = {
        10: { 
            title: "Kindness (Ihsan)", 
            text: "'Kindness is a mark of faith.' Your gentleness with others is a beautiful reflection of your heart, Yeka.", 
            img: "✨" 
        },
        20: { 
            title: "Patience (Sabr)", 
            text: "'Allah is with the patient.' (2:153). Thank you for your Sabr with me—for still noticing me even when I tend to disappear.", 
            img: "🤍" 
        },
        30: { 
            title: "Faith (Iman)", 
            text: "Watching your journey of faith is inspiring. May your heart always remain firm and filled with Noor.", 
            img: "🌙" 
        },
        40: { 
            title: "Prayer (Salah)", 
            text: "May every Sujud bring you closer to peace, and may your heart always find tranquility in prayer.", 
            img: "🤲" 
        },
        50: { 
            title: "Destiny (Qadr)", 
            text: "I believe it was Qadr that allowed our paths to cross. I am so grateful for the chance to know you.", 
            img: "⭐" 
        },
        60: { 
            title: "Forgiveness", 
            text: "'Be forgiving and overlook.' (24:22). Your ability to see the good in people is a rare and noble trait.", 
            img: "🍃" 
        },
        70: { 
            title: "Gratitude (Shukr)", 
            text: "I am truly thankful to Allah for your presence. I hope to get to know you even more as time goes by.", 
            img: "🌸" 
        },
        80: { 
            title: "Eid Milad Yeka!", 
            text: "May Allah bless your path with light, shower you with mercy, and grant all your heartfelt duas. Happy Birthday, Yeka!", 
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
        card.style.transform = "translateY(-700px) rotate(8deg)";
        canvas.style.opacity = "1";
        setTimeout(() => { active = true; }, 600);
    }

    function showCard(data) {
        active = false;
        canvas.style.opacity = "0.2";
        sTitle.innerText = data.title;
        sText.innerText = data.text;
        sImg.innerText = data.img;
        card.style.transform = "translateY(0) rotate(" + (Math.random() * 4 - 2) + "deg)";
        
        if(score >= 80) { triggerFinalConfetti(); }
    }

    function triggerFinalConfetti() {
        var duration = 8 * 1000;
        var animationEnd = Date.now() + duration;
        var interval = setInterval(function() {
            var timeLeft = animationEnd - Date.now();
            if (timeLeft <= 0) return clearInterval(interval);
            confetti({ particleCount: 50, spread: 80, origin: { y: 0.6 }, colors: ['#2D5A52', '#D4AF37', '#ffffff'] });
        }, 300);
        document.getElementById('card-btn').innerText = "Replay Journey";
    }

    function move(e) {
        if (!active) return;
        let rect = canvas.getBoundingClientRect();
        let clientX = e.touches ? e.touches[0].clientX : e.clientX;
        let x = clientX - rect.left;
        basket.x = (x * (canvas.width / rect.width)) - basket.w / 2;
    }

    canvas.addEventListener('mousemove', move);
    canvas.addEventListener('touchmove', (e) => { e.preventDefault(); move(e); }, {passive: false});

    function update() {
        ctx.clearRect(0, 0, canvas.width, canvas.height);
        stars.forEach(s => {
            s.opacity += (Math.random() - 0.5) * 0.04;
            if(s.opacity < 0) s.opacity = 0; if(s.opacity > 1) s.opacity = 1;
            ctx.fillStyle = `rgba(45, 90, 82, ${s.opacity})`;
            ctx.beginPath(); ctx.arc(s.x, s.y, s.size, 0, Math.PI*2); ctx.fill();
        });

        if (active) {
            frame++;
            if (frame % 32 === 0) {
                items.push({ x: Math.random() * 370, y: -20, char: ['🌸','🌙','🎁','🤲','⭐'][Math.floor(Math.random()*5)] });
            }
            ctx.fillStyle = '#2D5A52';
            ctx.beginPath(); ctx.roundRect(basket.x, basket.y, basket.w, basket.h, 5); ctx.fill();

            for (let i = items.length - 1; i >= 0; i--) {
                items[i].y += 4.5;
                ctx.font = '28px serif';
                ctx.fillText(items[i].char, items[i].x, items[i].y);
                if (items[i].y > basket.y && items[i].y < basket.y + 20 &&
                    items[i].x > basket.x - 10 && items[i].x < basket.x + basket.w + 10) {
                    catchSound.currentTime = 0;
                    catchSound.play();
                    items.splice(i, 1);
                    score++;
                    pointsEl.innerText = score;
                    if (milestones[score]) showCard(milestones[score]);
                } else if (items[i].y > 510) {
                    items.splice(i, 1);
                }
            }
        }
        requestAnimationFrame(update);
    }
    update();
</script>
"""

components.html(game_html, height=650)

st.markdown("<p class='footer'>Eid Milad Yeka! <br> <i>A journey of the heart, built with gratitude.</i></p>", unsafe_allow_html=True)
