import streamlit as st

# 1. पेज की पूरी सेटिंग
st.set_page_config(page_title="Happy Janmashtami!", page_icon="🪈", layout="centered")

# 2. बैकग्राउंड और फ्लोटिंग एनिमेशन के लिए CSS
custom_css = """
<style>
    /* ऐप का शानदार डार्क फेस्टिवल बैकग्राउंड */
    .stApp {
        background: linear-gradient(135deg, #1a0033 0%, #4d004d 100%) !important;
        color: #ffffff;
    }
    
    /* मुख्य चमकती हुई हेडिंग */
    .main-title {
        font-family: 'Georgia', serif;
        color: #FFD700;
        text-align: center;
        font-size: 2.8rem;
        font-weight: bold;
        text-shadow: 0px 0px 15px #ff6600;
        margin-top: 10px;
        margin-bottom: 20px;
    }
    
    /* नीचे का बधाई संदेश */
    .sub-title {
        font-family: 'Georgia', serif;
        color: #00FFCC;
        text-align: center;
        font-size: 1.3rem;
        line-height: 1.8;
        margin-top: 25px;
        text-shadow: 1px 1px 5px #000;
    }

    /* कलाकृति के लिए स्पेशल एनिमेटेड कंटेनर */
    .krishna-svg-box {
        display: flex;
        justify-content: center;
        align-items: center;
        margin: 20px auto;
        width: 100%;
        max-width: 320px;
        animation: floatMotion 3s ease-in-out infinite;
    }

    /* ऊपर-नीचे होने का स्मूथ मोशन (Floating Effect) */
    @keyframes floatMotion {
        0% { transform: translateY(0px); }
        50% { transform: translateY(-20px); }
        100% { transform: translateY(0px); }
    }
</style>
"""
st.markdown(custom_css, unsafe_allow_html=True)

# 3. स्क्रीन पर सबसे ऊपर "Happy Janmashtami" लिखना
st.markdown("<h1 class='main-title'>✨ Happy Janmashtami ✨</h1>", unsafe_allow_html=True)

# 4. बिना किसी बाहरी लिंक या बड़ी इमेज के शुद्ध कोड से बनी सुंदर कृष्ण मटकी, मोरपंख और बांसुरी (SVG Art)
# यह सीधे स्क्रीन पर तुरंत लोड होगी और कभी ब्लॉक नहीं हो सकती
krishna_svg_art = """
<div class="krishna-svg-box">
    <svg xmlns="http://w3.org" viewBox="0 0 400 400" width="100%" height="auto" style="border-radius: 20px; box-shadow: 0px 0px 30px #FFD700; background: #2d004d; padding: 20px;">
        <!-- चमकता हुआ सुदर्शन चक्र बैकग्राउंड -->
        <circle cx="200" cy="180" r="110" fill="none" stroke="#FFD700" stroke-width="4" stroke-dasharray="10,10" opacity="0.6"/>
        <circle cx="200" cy="180" r="125" fill="none" stroke="#ff6600" stroke-width="2" opacity="0.4"/>
        
        <!-- मक्खन की मटकी (Dahi Handi) -->
        <path d="M140,180 Q140,110 200,110 Q260,110 260,180 Q260,260 200,260 Q140,260 140,180 Z" fill="#b37400" stroke="#FFD700" stroke-width="4"/>
        <path d="M150,140 Q200,160 250,140" fill="none" stroke="#FFD700" stroke-width="3"/>
        <!-- मटकी का गला और डिजाइन -->
        <ellipse cx="200" cy="120" rx="35" ry="10" fill="#805200" stroke="#FFD700" stroke-width="4"/>
        <path d="M165,120 Q200,135 235,120" fill="none" stroke="#ffffff" stroke-width="5" stroke-linecap="round"/>
        
        <!-- मोरपंख (Peacock Feather) -->
        <g transform="translate(200, 70) rotate(-15)">
            <path d="M0,0 Q-30,-40 0,-80 Q30,-40 0,0 Z" fill="#0099ff" stroke="#00ffcc" stroke-width="2"/>
            <path d="M0,-15 Q-18,-42 0,-65 Q18,-42 0,-15 Z" fill="#00cc44"/>
            <circle cx="0" cy="-35" r="12" fill="#ffe066"/>
            <circle cx="0" cy="-35" r="7" fill="#0033cc"/>
            <path d="M0,0 Q10,40 20,70" fill="none" stroke="#00ffcc" stroke-width="3"/>
        </g>
        
        <!-- सुनहरी बांसुरी (Golden Flute) -->
        <g transform="translate(200, 290) rotate(-5)">
            <rect x="-130" y="-8" width="260" height="16" rx="8" fill="gold" stroke="#FFD700" stroke-width="2"/>
            <!-- बांसुरी के छेद -->
            <circle cx="-80" cy="0" r="4" fill="#1a0033"/>
            <circle cx="-50" cy="0" r="4" fill="#1a0033"/>
            <circle cx="-20" cy="0" r="4" fill="#1a0033"/>
            <circle cx="10" cy="0" r="4" fill="#1a0033"/>
            <circle cx="40" cy="0" r="4" fill="#1a0033"/>
            <circle cx="70" cy="0" r="4" fill="#1a0033"/>
            <!-- लाल धागा / लटकन -->
            <path d="M110,4 Q120,25 115,40" fill="none" stroke="#ff3333" stroke-width="3" stroke-linecap="round"/>
            <circle cx="115" cy="43" r="5" fill="#ffcc00"/>
        </g>
    </svg>
</div>
"""
st.components.v1.html(krishna_svg_art, height=350)

# 5. नीचे का सुंदर मैसेज
st.markdown(
    "<p class='sub-title'>माखन चोर नन्द किशोर, बांधे जिसने प्रीत की डोर...<br>हरे कृष्णा! 🌸🪈</p>", 
    unsafe_allow_html=True
)

# 6. ऐप खुलते ही गुब्बारे उड़ाना
st.balloons()
