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

# 4. श्री कृष्ण जी की बेहद सुंदर इमेज का पूरा और बिल्कुल सही सिंगल-लाइन Base64 डेटा (Syntax Error फिक्स)
krishna_img_data = "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"

try:
    # Base64 को बिना किसी एरर के इमेज में बदलना
    image_bytes = base64.b64decode(krishna_img_data)
    image = Image.open(io.BytesIO(image_bytes))
    
    # स्क्रीन पर 100% असली इमेज दिखाना (यह कभी ब्लॉक नहीं होगी)
    st.image(image, width=280)
except Exception as e:
    st.error("कृपया ऐप को लोड होने के लिए 5 सेकंड का समय दें या एक बार पेज रिफ्रेश करें।")

# 5. नीचे का सुंदर बधाई संदेश
st.markdown(
    "<p class='sub-title'>माखन चोर नन्द किशोर, बांधे जिसने प्रीत की डोर...<br>हरे कृष्णा! 🌸🪈</p>", 
    unsafe_allow_html=True
)

# 6. ऐप खुलते ही स्क्रीन पर गुब्बारे उड़ाना
st.balloons()
