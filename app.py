import streamlit as st

# 1. पेज की पूरी प्रीमियम सेटिंग
st.set_page_config(page_title="Happy Janmashtami!", page_icon="🪈", layout="centered")

# बैकग्राउंड कलर सेट करने के लिए छोटा कोड
st.markdown("<style>.stApp {background: linear-gradient(135deg, #120024 0%, #2d004d 50%, #4d004d 100%) !important; color: white;}</style>", unsafe_allow_html=True)

# मुख्य हेडिंग
st.markdown("<h1 style='font-family:serif; color:#FFD700; text-align:center; text-shadow: 0px 0px 20px #ff6600, 0px 0px 10px #FFD700;'>✨ Happy Janmashtami ✨</h1>", unsafe_allow_html=True)

# 2. यहाँ है वो एनिमेटेड कृष्ण जी का चेहरा, मोरपंख और बांसुरी (st.html के साथ)
st.html("""
<div style="display: flex; justify-content: center; align-items: center; margin: 20px auto; width: 100%; max-width: 340px; animation: floatAnim 3s ease-in-out infinite;">
    <svg xmlns="http://w3.org" viewBox="0 0 400 450" width="100%" height="auto" style="border-radius: 25px; box-shadow: 0px 0px 35px #FFD700; background: radial-gradient(circle, #2d004d 40%, #120024 100%); padding: 15px;">
        <circle cx="200" cy="200" r="130" fill="none" stroke="#FFD700" stroke-width="3" stroke-dasharray="8,8" opacity="0.5"/>
        <circle cx="200" cy="200" r="145" fill="none" stroke="#ff6600" stroke-width="1.5" opacity="0.3"/>
        <path d="M120,180 Q100,140 130,110 Q110,80 150,80 Q170,50 210,60 Q250,50 270,90 Q310,100 290,140 Q310,180 280,210 Q290,250 270,280" fill="none" stroke="#00e5ff" stroke-width="2.5" opacity="0.7"/>
        <g transform="translate(230, 60) rotate(15)">
            <path d="M0,0 Q-35,-45 0,-90 Q35,-45 0,0 Z" fill="#0099ff" stroke="#00ffcc" stroke-width="2"/>
            <path d="M0,-15 Q-22,-47 0,-75 Q22,-47 0,-15 Z" fill="#00cc44"/>
            <circle cx="0" cy="-40" r="14" fill="#ffe066"/>
            <circle cx="0" cy="-40" r="8" fill="#0033cc"/>
            <path d="M0,0 Q10,40 15,65" fill="none" stroke="#00ffcc" stroke-width="3"/>
        </g>
        <path d="M180,100 L185,160 L175,210 Q170,230 185,245 Q210,265 240,240 Q265,215 260,170" fill="none" stroke="#ffffff" stroke-width="3.5" stroke-linecap="round"/>
        <path d="M187,110 Q192,135 192,145 Q192,135 197,110 Z" fill="#FFD700" stroke="#ff6600" stroke-width="1"/>
        <circle cx="192" cy="152" r="3" fill="#ff3333"/>
        <path d="M145,150 Q165,140 182,153" fill="none" stroke="#00ffcc" stroke-width="2.5" stroke-linecap="round"/>
        <path d="M195,152 Q215,138 235,148" fill="none" stroke="#00ffcc" stroke-width="2.5" stroke-linecap="round"/>
        <path d="M152,163 Q168,175 180,165" fill="none" stroke="#ffffff" stroke-width="3" stroke-linecap="round"/>
        <path d="M198,164 Q214,174 228,161" fill="none" stroke="#ffffff" stroke-width="3" stroke-linecap="round"/>
        <path d="M187,222 Q200,230 215,220" fill="none" stroke="#ff3366" stroke-width="3.5" stroke-linecap="round"/>
        <g transform="translate(210, 235) rotate(-12)">
            <rect x="-110" y="-8" width="240" height="16" rx="8" fill="gold" stroke="#FFD700" stroke-width="2"/>
            <circle cx="-70" cy="0" r="4" fill="#120024"/><circle cx="-40" cy="0" r="4" fill="#120024"/><circle cx="-10" cy="0" r="4" fill="#120024"/><circle cx="20" cy="0" r="4" fill="#120024"/><circle cx="50" cy="0" r="4" fill="#120024"/><circle cx="80" cy="0" r="4" fill="#120024"/>
            <path d="M100,4 Q112,20 108,35" fill="none" stroke="#ff3333" stroke-width="3" stroke-linecap="round"/>
            <circle cx="108" cy="38" r="4" fill="#FFD700"/>
        </g>
        <path d="M175,270 Q210,310 245,265" fill="none" stroke="#FFD700" stroke-width="2" stroke-dasharray="4,4"/>
    </svg>
</div>
<style>
    @keyframes floatAnim {
        0% { transform: translateY(0px); }
        50% { transform: translateY(-15px); }
        100% { transform: translateY(0px); }
    }
</style>
""")

# नीचे का बधाई संदेश
st.markdown("<p style='font-family:serif; color:#00FFCC; text-align:center; font-size:1.3rem; line-height:1.8; text-shadow: 1px 1px 5px #000;'>माखन चोर नन्द किशोर, बांधे जिसने प्रीत की डोर...<br>हरे कृष्णा! 🌸🪈</p>", unsafe_allow_html=True)

# बैलून इफ़ेक्ट
st.balloons()
