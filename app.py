import streamlit as st

st.set_page_config(page_title="Happy Janmashtami!", page_icon="🪈", layout="centered")

# बैकग्राउंड कलर सेट करने के लिए छोटा कोड
st.markdown("<style>.stApp {background: linear-gradient(135deg, #1a0033 0%, #4d004d 100%) !important; color: white;}</style>", unsafe_allow_html=True)

# मुख्य हेडिंग
st.markdown("<h1 style='font-family:serif; color:#FFD700; text-align:center; text-shadow: 0px 0px 15px #ff6600;'>✨ Happy Janmashtami ✨</h1>", unsafe_allow_html=True)

# यहाँ है वो एनिमेटेड चक्र, मटकी और बांसुरी वाला डिज़ाइन (बिना किसी ट्रिपल कोट के झंझट के)
st.html("""
<div style="display: flex; justify-content: center; align-items: center; margin: 20px auto; width: 100%; max-width: 320px; animation: floatAnim 3s ease-in-out infinite;">
    <svg xmlns="http://w3.org" viewBox="0 0 400 400" width="100%" height="auto" style="border-radius: 25px; box-shadow: 0px 0px 35px #FFD700; background: radial-gradient(circle, #2d004d 40%, #150026 100%); padding: 15px;">
        <circle cx="200" cy="180" r="110" fill="none" stroke="#FFD700" stroke-width="4" stroke-dasharray="12,12" opacity="0.7">
            <animateTransform attributeName="transform" type="rotate" from="0 200 180" to="360 200 180" dur="20s" repeatCount="indefinite"/>
        </circle>
        <circle cx="200" cy="180" r="125" fill="none" stroke="#ff6600" stroke-width="2" stroke-dasharray="5,5" opacity="0.4">
            <animateTransform attributeName="transform" type="rotate" from="360 200 180" to="0 200 180" dur="15s" repeatCount="indefinite"/>
        </circle>
        <path d="M130,190 Q130,110 200,110 Q270,110 270,190 Q270,270 200,270 Q130,270 130,190 Z" fill="#b37400" stroke="#FFD700" stroke-width="5"/>
        <ellipse cx="200" cy="120" rx="40" ry="12" fill="#805200" stroke="#FFD700" stroke-width="4"/>
        <path d="M140,170 Q200,200 260,170" fill="none" stroke="#FFD700" stroke-width="3"/>
        <path d="M145,210 Q200,240 255,210" fill="none" stroke="#ff6600" stroke-width="3"/>
        <path d="M165,120 Q180,140 190,150 Q200,160 210,145 Q220,130 235,120 Q200,130 165,120 Z" fill="#ffffff" stroke="#e6e6e6" stroke-width="1"/>
        <g transform="translate(200, 75) rotate(-15)">
            <path d="M0,0 Q-35,-45 0,-90 Q35,-45 0,0 Z" fill="#0099ff" stroke="#00ffcc" stroke-width="2"/>
            <path d="M0,-15 Q-22,-47 0,-75 Q22,-47 0,-15 Z" fill="#00cc44"/>
            <circle cx="0" cy="-40" r="14" fill="#ffe066"/>
            <circle cx="0" cy="-40" r="8" fill="#0033cc"/>
            <path d="M0,0 Q15,45 25,80" fill="none" stroke="#00ffcc" stroke-width="3.5"/>
        </g>
        <g transform="translate(200, 310) rotate(-6)">
            <rect x="-140" y="-10" width="280" height="20" rx="10" fill="gold" stroke="#FFD700" stroke-width="3"/>
            <circle cx="-90" cy="0" r="5" fill="#150026"/><circle cx="-55" cy="0" r="5" fill="#150026"/><circle cx="-20" cy="0" r="5" fill="#150026"/><circle cx="15" cy="0" r="5" fill="#150026"/><circle cx="50" cy="0" r="5" fill="#150026"/><circle cx="85" cy="0" r="5" fill="#150026"/>
            <path d="M115,5 Q130,25 120,45" fill="none" stroke="#ff3333" stroke-width="3.5" stroke-linecap="round"/>
            <circle cx="120" cy="48" r="6" fill="#FFD700"/>
        </g>
    </svg>
</div>
<style>
    @keyframes floatAnim {
        0% { transform: translateY(0px); }
        50% { transform: translateY(-20px); }
        100% { transform: translateY(0px); }
    }
</style>
""")

# नीचे का बधाई संदेश
st.markdown("<p style='font-family:serif; color:#00FFCC; text-align:center; font-size:1.3rem; line-height:1.8; text-shadow: 1px 1px 5px #000;'>माखन चोर नन्द किशोर, बांधे जिसने प्रीत की डोर...<br>हरे कृष्णा! 🌸🪈</p>", unsafe_allow_html=True)

# बैलून इफ़ेक्ट
st.balloons()
