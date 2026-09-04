import streamlit as st
import os

# 1. पेज की पूरी प्रीमियम VLVIP सेटिंग
st.set_page_config(page_title="Happy Janmashtami!", page_icon="🪈", layout="centered")

# 2. एडवांस CSS: पीला रंग हटाकर सुपर प्रीमियम नियॉन ग्लो और मॉडर्न डिज़ाइन इफेक्ट्स
custom_css = """
<style>
    /* ऐप का शानदार डार्क और मॉडर्न फेस्टिव बैकग्राउंड */
    .stApp {
        background: linear-gradient(135deg, #0d001a 0%, #1a0033 50%, #2d004d 100%) !important;
        color: #ffffff;
    }
    
    /* मुख्य चमकती हुई मॉडर्न हेडिंग */
    .main-title {
        font-family: 'Georgia', serif;
        color: #ffffff;
        text-align: center;
        font-size: 3rem;
        font-weight: bold;
        text-shadow: 0px 0px 10px #ff007f, 0px 0px 20px #ff007f, 0px 0px 30px #9900ff;
        margin-top: 20px;
        margin-bottom: 25px;
        letter-spacing: 2px;
    }
    
    /* नीचे का सुंदर और साफ बधाई संदेश */
    .sub-title {
        font-family: 'Georgia', serif;
        color: #00ffcc;
        text-align: center;
        font-size: 1.4rem;
        line-height: 1.8;
        margin-top: 35px;
        text-shadow: 0px 0px 10px rgba(0, 255, 204, 0.5);
        font-weight: 500;
    }

    /* पीले बॉर्डर को हटाकर प्रीमियम नियॉन पिंक/पर्पल ग्लो और स्मूथ फ्लोटिंग */
    .stImage img {
        border-radius: 25px !important;
        box-shadow: 0px 0px 30px #ff007f, 0px 0px 15px #9900ff !important;
        border: 2px solid rgba(255, 0, 127, 0.4) !important;
        animation: superFloat 4s ease-in-out infinite !important;
    }

    /* और भी ज़्यादा स्मूथ और वीआईपी ऊपर-नीचे तैरने का मोशन */
    @keyframes superFloat {
        0% { transform: translateY(0px) scale(1); }
        50% { transform: translateY(-15px) scale(1.01); }
        100% { transform: translateY(0px) scale(1); }
    }
</style>
"""
st.markdown(custom_css, unsafe_allow_html=True)

# 3. स्क्रीन पर सबसे ऊपर "Happy Janmashtami" हेडिंग
st.markdown("<h1 class='main-title'>✨ Happy Janmashtami ✨</h1>", unsafe_allow_html=True)

# 4. तुम्हारी अपलोडेड फोटो 'images (52).jpeg' से सीधे लोड करना
image_path = "images (52).jpeg"

if os.path.exists(image_path):
    st.image(image_path, use_container_width=True)
else:
    st.warning("कृपया ऐप को लोड होने के लिए 5 सेकंड का समय दें या पेज को एक बार रिफ्रेश करें।")

# 5. नीचे का सुंदर VIP संदेश
st.markdown(
    "<p class='sub-title'>माखन चोर नन्द किशोर, बांधे जिसने प्रीत की डोर...<br>हरे कृष्णा! 🌸🪈</p>", 
    unsafe_allow_html=True
)

# 6. ऐप खुलते ही स्क्रीन पर गुब्बारे उड़ाना
st.balloons()
