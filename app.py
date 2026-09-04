import streamlit as st

# 1. पेज की पूरी सेटिंग
st.set_page_config(page_title="Happy Janmashtami!", page_icon="🪈", layout="centered")

# 2. एडवांस CSS: फेस्टिवल थीम, बैकग्राउंड और स्मूथ फ्लोटिंग एनिमेशन
custom_css = """
<style>
    /* ऐप का शानदार डार्क फेस्टिव बैकग्राउंड */
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
        margin-bottom: 25px;
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

    /* एनिमेटेड कलाकृति के लिए कंटेनर */
    .krishna-design-container {
        display: flex;
        justify-content: center;
        align-items: center;
        margin: 20px auto;
        width: 100%;
        max-width: 320px;
        animation: floatAnimation 3s ease-in-out infinite;
    }

    /* ऊपर-नीचे होने वाला स्मूथ मोशन (Floating Effect) */
    @keyframes floatAnimation {
        0% { transform: translateY(0px); }
        50% { transform: translateY(-20px); }
        100% { transform: translateY(0px); }
    }
</style>
"""
st.markdown(custom_css, unsafe_allow_html=True)

# 3. स्क्रीन पर सबसे ऊपर "Happy Janmashtami" लिखना
st.markdown("<h1 class='main-title'>✨ Happy Janmashtami ✨</h1>", unsafe_allow_html=True)

# 4. शुद्ध SVG कोड से बना कृष्ण जी का प्रीमियम एनिमेटेड डिजाइन (यह कभी ब्लॉक नहीं होगा)
krishna_animated_design = """
<div class="krishna-design-container">
    <svg xmlns="http://w3.org" viewBox="0 0 400 400" width="100%" height="auto" style="border-radius: 25px; box-shadow: 0px 0px 35px #FFD700; background: radial-gradient(circle, #2d004d 40%, #150026 100%); padding: 15px;">
        
        <!-- 1. सुदर्शन चक्र / आध्यात्मिक आभा मंडल (Glowing Aura) -->
        <circle cx="200" cy="180" r="110" fill="none" stroke="#FFD700" stroke-width="4" stroke-dasharray="12,12" opacity="0.7">
            <animateTransform attributeName="transform" type="rotate" from="0 200 180" to="360 200 180" dur="20s" repeatCount="indefinite"/>
        </circle>
        <circle cx="200" cy="180" r="125" fill="none" stroke="#ff6600" stroke-width="2" stroke-dasharray="5,5" opacity="0.4">
            <animateTransform attributeName="transform" type="rotate" from="360 200 180" to="0 200 180" dur="15s" repeatCount="indefinite"/>
        </circle>
        
        <!-- 2. माखन चोर की मटकी (Dahi Handi) -->
        <path d="M130,190 Q130,110 200,110 Q270,110 270,190 Q270,270 200,270 Q130,270 130,190 Z" fill="#b37400" stroke="#FFD700" stroke-width="5"/>
        <ellipse cx="200" cy="120" rx="40" ry="12" fill="#805200" stroke="#FFD700" stroke-width="4"/>
        
        <!-- मटकी पर सुंदर गोपी डिजाइन और सजावट -->
        <path d="M140,170 Q200,200 260,170" fill="none" stroke="#FFD700" stroke-width="3"/>
        <path d="M145,210 Q200,240 255,210" fill="none" stroke="#ff6600" stroke-width="3"/>
        
        <!-- पवित्र माखन (Holy Butter/Makhan overflowing) -->
        <path d="M165,120 Q180,140 190,150 Q200,160 210,145 Q220,130 235,120 Q200,130 165,120 Z" fill="#ffffff" stroke="#e6e6e6" stroke-width="1"/>
        <circle cx="190" cy="155" r="5" fill="#ffffff"/>
        <circle cx="205" cy="165" r="4" fill="#ffffff"/>

        <!-- 3. दिव्य मोरपंख (Peacock Feather) -->
        <g transform="translate(200, 75) rotate(-15)">
            <!-- बाहरी पंख -->
            <path d="M0,0 Q-35,-45 0,-90 Q35,-45 0,0 Z" fill="#0099ff" stroke="#00ffcc" stroke-width="2"/>
            <!-- हरा भाग -->
            <path d="M0,-15 Q-22,-47 0,-75 Q22,-47 0,-15 Z" fill="#00cc44"/>
            <!-- चमकदार केंद्र (Eye of the feather) -->
            <circle cx="0" cy="-40" r="14" fill="#ffe066"/>
            <circle cx="0" cy="-40" r="8" fill="#0033cc"/>
            <!-- पंख की डंडी -->
            <path d="M0,0 Q15,45 25,80" fill="none" stroke="#00ffcc" stroke-width="3.5"/>
        </g>
        
        <!-- 4. दिव्य सुनहरी बांसुरी (Sacred Golden Flute) -->
        <g transform="translate(200, 310) rotate(-6)">
            <rect x="-140" y="-10" width="280" height="20" rx="10" fill="url(#flute-gradient)" stroke="#FFD700" stroke-width="3" filter="url(#glow)"/>
            <!-- बांसुरी के छिद्र (Flute Holes) -->
            <circle cx="-90" cy="0" r="5" fill="#150026"/>
            <circle cx="-55" cy="0" r="5" fill="#150026"/>
            <circle cx="-20" cy="0" r="5" fill="#150026"/>
            <circle cx="15" cy="0" r="5" fill="#150026"/>
            <circle cx="50" cy="0" r="5" fill="#150026"/>
            <circle cx="85" cy="0" r="5" fill="#150026"/>
            
            <!-- बांसुरी से लटकता हुआ सुंदर लाल और रेशमी धागा (Tassels) -->
            <path d="M115,5 Q130,25 120,45" fill="none" stroke="#ff3333" stroke-width="3.5" stroke-linecap="round"/>
            <circle cx="120" cy="48" r="6" fill="#FFD700"/>
            <path d="M120,54 L115,70 M120,54 L120,72 M120,54 L125,70" stroke="#ffcc00" stroke-width="2"/>
        </g>
        
        <!-- ग्रेडिएंट और ग्लो इफेक्ट्स डेफिनिशन -->
        <defs>
            <linearGradient id="flute-gradient" x1="0%" y1="0%" x2="0%" y2="100%">
                <stop offset="0%" style="stop-color:#fff099;stop-opacity:1" />
                <stop offset="40%" style="stop-color:#d4af37;stop-opacity:1" />
                <stop offset="100%" style="stop-color:#aa8000;stop-opacity:1" />
            </linearGradient>
            <filter id="glow" x="-20%" y="-20%" width="140%" height="140%">
                <feGaussianBlur stdDeviation="2" result="blur" />
                <feComposite in="SourceGraphic" in2="blur" operator="over" />
            </filter>
        </defs>
    </svg>
</div>
"""
st.markdown(krishna_animated_design, unsafe_allow_html=True)

# 5. नीचे का सुंदर मैसेज
st.markdown(
    "<p class='sub-title'>माखन चोर नन्द किशोर, बांधे जिसने प्रीत की डोर...<br>हरे कृष्णा! 🌸🪈</p>", 
    unsafe_allow_html=True
)

# 6. ऐप खुलते ही स्क्रीन पर गुब्बारे उड़ाना
st.balloons()
