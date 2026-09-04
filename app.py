import streamlit as st
import os

# 1. पेज की पूरी प्रीमियम सेटिंग
st.set_page_config(page_title="Happy Janmashtami!", page_icon="🪈", layout="centered")

# 2. बैकग्राउंड कलर और फोटो को ऊपर-नीचे (Floating) एनिमेट करने के लिए CSS
custom_css = """
<style>
    /* ऐप का डार्क फेस्टिवल बैकग्राउंड */
    .stApp {
        background: linear-gradient(135deg, #120024 0%, #330033 50%, #4d004d 100%) !important;
        color: #ffffff;
    }
    
    /* मुख्य चमकती हेडिंग */
    .main-title {
        font-family: 'Georgia', serif;
        color: #FFD700;
        text-align: center;
        font-size: 3rem;
        font-weight: bold;
        text-shadow: 0px 0px 20px #ff6600, 0px 0px 10px #FFD700;
        margin-top: 15px;
        margin-bottom: 25px;
    }
    
    /* नीचे का बधाई संदेश */
    .sub-title {
        font-family: 'Georgia', serif;
        color: #00FFCC;
        text-align: center;
        font-size: 1.4rem;
        line-height: 1.8;
        margin-top: 30px;
        text-shadow: 1px 1px 8px #000000;
    }

    /* इमेज के चारों तरफ प्रीमियम बॉर्डर और तैरने वाला (Floating) एनीमेशन */
    .stImage img {
        border-radius: 25px !important;
        box-shadow: 0px 0px 35px #FFD700, 0px 0px 15px #ff6600 !important;
        border: 4px solid #FFD700 !important;
        animation: floatMotion 3s ease-in-out infinite !important;
    }

    /* स्मूथ ऊपर-नीचे होने का मोशन */
    @keyframes floatMotion {
        0% { transform: translateY(0px); }
        50% { transform: translateY(-18px); }
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

# 5. नीचे का सुंदर संदेश
st.markdown(
    "<p class='sub-title'>माखन चोर नन्द किशोर, बांधे जिसने प्रीत की डोर...<br>हरे कृष्णा! 🌸🪈</p>", 
    unsafe_allow_html=True
)

# 6. ऐप खुलते ही स्क्रीन पर गुब्बारे उड़ाना
st.balloons()
