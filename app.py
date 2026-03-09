import streamlit as st
import streamlit.components.v1 as components

# --- PAGE CONFIG ---
st.set_page_config(page_title="For You", page_icon="🌙", layout="centered")

# --- CUSTOM CSS ---
st.markdown("""
    <style>
    .stApp { background-color: #E5E0D8; }
    .title { 
        color: #2D5A52; 
        font-family: 'Georgia', serif; 
        text-align: center; 
        margin-top: 30px;
        font-style: italic;
    }
    </style>
    """, unsafe_allow_html=True)

st.markdown("<h1 class='title'>The Frequency of You</h1>", unsafe_allow_html=True)

# --- THE ROMANTIC OSCILLOSCOPE (HTML/JS) ---
osc_html = """
<div id="container" style="background: #E5E0D8; display: flex; flex-direction: column; align-items: center; font-family: 'Georgia', serif;">
    <canvas id="canvas" style="width: 100%; height: 350px; background: #E5E0D8; cursor: pointer;"></canvas>
    <div id="msg" style="margin-top: 10px; color: #2D5A52; font-size: 1.1rem; text-align: center; font-style: italic;">
        The world is quiet... <br>Tap the heart and say something beautiful.
    </div>
</div>

<script>
    const canvas = document.getElementById('canvas');
    const ctx = canvas.getContext('2d');
    const msg = document.getElementById('msg');
    
    let audioCtx, analyser, dataArray, bufferLength;
    let revealed = false;
    let glow = 0;

    function init() {
        if (audioCtx) return;
        audioCtx = new (window.AudioContext || window.webkitAudioContext)();
        analyser = audioCtx.createAnalyser();
        analyser.fftSize = 1024;

        navigator.mediaDevices.getUserMedia({ audio: true }).then(stream => {
            const source = audioCtx.createMediaStreamSource(stream);
            source.connect(analyser);
            bufferLength = analyser.frequencyBinCount;
            dataArray = new Uint8Array(bufferLength);
            msg.innerHTML = "Your voice makes the heart beat... <br>Keep speaking to unlock your message.";
            draw();
        });
    }

    function draw() {
        if (revealed) return;
        requestAnimationFrame(draw);
        analyser.getByteTimeDomainData(dataArray);

        ctx.clearRect(0, 0, canvas.width, canvas.height);
        
        let volume = 0;
        for (let i = 0; i < bufferLength; i++) {
            volume += Math.abs(128 - dataArray[i]);
        }

        // Heart pulsing logic
        let pulse = 1 + (volume / 2000); 
        if (volume > 500) glow += 0.5;

        const centerX = canvas.width / 2;
        const centerY = canvas.height / 2;
        
        // Draw the Oscilloscope Heart
        ctx.strokeStyle = '#2D5A52';
        ctx.shadowBlur = 15;
        ctx.shadowColor = '#2D5A52';
        ctx.lineWidth = 4;
        ctx.beginPath();

        // Parametric Heart Formula modified by audio data
        for (let i = 0; i <= Math.PI * 2; i += 0.05) {
            let audioMod = (dataArray[Math.floor(i * 10)] / 128.0) - 1.0;
            let r = (1 - Math.sin(i)) * (pulse + audioMod * 0.5);
            let x = centerX + 100 * r * Math.cos(i);
            let y = centerY - 130 * r * Math.sin(i) + 50; 
            
            if (i === 0) ctx.moveTo(x, y);
            else ctx.lineTo(x, y);
        }
        ctx.closePath();
        ctx.stroke();

        if (glow >= 100) {
            revealed = true;
            msg.innerHTML = "<h1 style='font-size: 2.5rem; margin:0; color: #2D5A52;'>ENJOY YOUR DAY!</h1><p style='color: #2D5A52;'>You are the only frequency I ever want to hear.</p>";
            // Static glowing heart
            ctx.shadowBlur = 30;
            ctx.stroke();
        }
    }

    canvas.addEventListener('click', init);
</script>
"""

components.html(osc_html, height=500)

st.write("---")
st.markdown("<p style='text-align: center; color: #2D5A52; font-style: italic; opacity: 0.6;'>Created with love just for you.</p>", unsafe_allow_html=True)
