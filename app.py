import streamlit as st

# 1. पेज की पूरी सेटिंग
st.set_page_config(page_title="Happy Janmashtami!", page_icon="🪈", layout="centered")

# 2. बैकग्राउंड और टेक्स्ट स्टाइल्स के लिए CSS
custom_css = """
<style>
    .stApp {
        background: linear-gradient(135deg, #1a0033 0%, #4d004d 100%) !important;
        color: #ffffff;
    }
    .main-title {
        font-family: 'Georgia', serif;
        color: #FFD700;
        text-align: center;
        font-size: 2.8rem;
        font-weight: bold;
        text-shadow: 0px 0px 15px #ff6600;
        margin-top: 10px;
        margin-bottom: 10px;
    }
    .sub-title {
        font-family: 'Georgia', serif;
        color: #00FFCC;
        text-align: center;
        font-size: 1.3rem;
        line-height: 1.8;
        margin-top: 20px;
        text-shadow: 1px 1px 5px #000;
    }
    .canvas-container {
        display: flex;
        justify-content: center;
        align-items: center;
        margin: 10px auto;
    }
</style>
"""
st.markdown(custom_css, unsafe_allow_html=True)

# 3. मुख्य हेडिंग
st.markdown("<h1 class='main-title'>✨ Happy Janmashtami ✨</h1>", unsafe_allow_html=True)

# 4. HTML Canvas + JavaScript एनिमेशन (यह सीधे स्क्रीन पर लाइव ड्रॉ और एनिमेट करेगा)
animation_html = """
<div class="canvas-container">
    <canvas id="krishnaCanvas" width="300" height="300" style="border-radius: 20px; box-shadow: 0px 0px 25px #FFD700; background: #2d004d;"></canvas>
</div>

<script>
    const canvas = document.getElementById('krishnaCanvas');
    const ctx = canvas.getContext('2d');
    let angle = 0;

    function draw() {
        ctx.clearRect(0, 0, canvas.width, canvas.height);
        
        // धीरे-धीरे ऊपर-नीचे होने का मोशन (Floating effect)
        let offsetY = Math.sin(angle) * 15;
        angle += 0.05;

        // 1. चमकता हुआ सुदर्शन चक्र / आभा मंडल (Background Glow)
        ctx.save();
        ctx.translate(150, 130 + offsetY);
        ctx.beginPath();
        let gradient = ctx.createRadialGradient(0, 0, 10, 0, 0, 90);
        gradient.addColorStop(0, 'rgba(255, 215, 0, 0.8)');
        gradient.addColorStop(0.5, 'rgba(255, 102, 0, 0.5)');
        gradient.addColorStop(1, 'rgba(0, 0, 0, 0)');
        ctx.fillStyle = gradient;
        ctx.arc(0, 0, 90, 0, Math.PI * 2);
        ctx.fill();
        ctx.restore();

        // 2. "श्री कृष्ण" सुंदर टेक्स्ट ड्रा करना
        ctx.save();
        ctx.translate(150, 130 + offsetY);
        ctx.font = "bold 36px 'Georgia', serif";
        ctx.textAlign = "center";
        ctx.textBaseline = "middle";
        
        // टेक्स्ट का गोल्डन कलर और ग्लो इफेक्ट
        ctx.shadowColor = "#FFD700";
        ctx.shadowBlur = 15;
        ctx.fillStyle = "#FFFFFF";
        ctx.fillText("श्री कृष्ण", 0, -10);
        ctx.restore();

        // 3. मोरपंख (Peacock Feather Outline)
        ctx.save();
        ctx.translate(150, 80 + offsetY);
        ctx.beginPath();
        ctx.ellipse(0, 0, 15, 25, Math.PI / 6, 0, Math.PI * 2);
        ctx.fillStyle = "#0099ff";
        ctx.fill();
        ctx.beginPath();
        ctx.ellipse(0, 0, 8, 15, Math.PI / 6, 0, Math.PI * 2);
        ctx.fillStyle = "#00ffcc";
        ctx.fill();
        ctx.restore();

        // 4. सोने की बांसुरी (Golden Flute) ड्रा करना
        ctx.save();
        ctx.translate(150, 170 + offsetY);
        
        // बांसुरी की डंडी
        ctx.beginPath();
        ctx.rect(-100, -5, 200, 10);
        ctx.fillStyle = "#FFD700";
        ctx.shadowColor = "#ff6600";
        ctx.shadowBlur = 10;
        ctx.fill();

        // बांसुरी के छेद (Holes)
        ctx.fillStyle = "#1a0033";
        ctx.shadowBlur = 0;
        for (let i = -60; i <= 60; i += 25) {
            ctx.beginPath();
            ctx.arc(i, 0, 3, 0, Math.PI * 2);
            ctx.fill();
        }
        ctx.restore();

        requestAnimationFrame(draw);
    }
    draw();
</script>
"""
st.components.v1.html(animation_html, height=340)

# 5. नीचे का बधाई संदेश
st.markdown(
    "<p class='sub-title'>माखन चोर नन्द किशोर, बांधे जिसने प्रीत की डोर...<br>हरे कृष्णा! 🌸🪈</p>", 
    unsafe_allow_html=True
)

# 6. गुब्बारे उड़ाना
st.balloons()
