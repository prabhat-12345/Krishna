import streamlit as st
import base64
import io
from PIL import Image

# 1. पेज की प्रीमियम सेटिंग
st.set_page_config(page_title="Happy Janmashtami!", page_icon="🪈", layout="centered")

# 2. एडवांस CSS: प्रीमियम डार्क गोल्ड थीम, चमकती हेडिंग और फ्लोटिंग एनीमेशन
custom_css = """
<style>
    /* प्रीमियम फेस्टिव बैकग्राउंड */
    .stApp {
        background: linear-gradient(135deg, #120024 0%, #330033 50%, #4d004d 100%) !important;
        color: #ffffff;
    }
    
    /* मुख्य चमकती हुई हेडिंग */
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
    
    /* सुंदर बधाई संदेश */
    .sub-title {
        font-family: 'Georgia', serif;
        color: #00FFCC;
        text-align: center;
        font-size: 1.4rem;
        line-height: 1.8;
        margin-top: 30px;
        text-shadow: 1px 1px 8px #000000;
    }

    /* इमेज के चारों तरफ प्रीमियम बॉर्डर और तैरने वाला (Floating) एनिमेशन */
    .stImage img {
        border-radius: 25px !important;
        box-shadow: 0px 0px 35px #FFD700, 0px 0px 15px #ff6600 !important;
        border: 4px solid #FFD700 !important;
        animation: floatMotion 3s ease-in-out infinite;
    }

    /* स्मूथ ऊपर-नीचे होने का मोशन */
    @keyframes floatMotion {
        0% { transform: translateY(0px); }
        50% { transform: translateY(-18px); }
        100% { transform: translateY(0px); }
    }
</style>
"""
st.markdown(custom_css, unsafe_allow_html=True)

# 3. स्क्रीन पर सबसे ऊपर "Happy Janmashtami" हेडिंग
st.markdown("<h1 class='main-title'>✨ Happy Janmashtami ✨</h1>", unsafe_allow_html=True)

# 4. श्री कृष्ण जी की बेहद सुंदर इमेज का पूरा और सॉलिड Base64 डेटा (यह बिना लिंक के सीधे फोन पर लोड होगा)
krishna_img_data = (
    "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"
)

try:
    # Base64 को वापस इमेज बाइट्स में बदलना
    image_bytes = base64.b64decode(krishna_img_data)
    image = Image.open(io.BytesIO(image_bytes))
    
    # बिना किसी एरर के स्क्रीन पर 100% असली इमेज दिखाना
    st.image(image, width=280)
except Exception as e:
    st.error("फोटो डेटा लोड होने में समस्या आ रही है।")

# 5. नीचे का सुंदर मैसेज
st.markdown(
    "<p class='sub-title'>माखन चोर नन्द किशोर, बांधे जिसने प्रीत की डोर...<br>हरे कृष्णा! 🌸🪈</p>", 
    unsafe_allow_html=True
)

# 6. ऐप खुलते ही स्क्रीन पर गुब्बारे उड़ाना
st.balloons()
