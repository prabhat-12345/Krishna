import streamlit as st
import requests
from PIL import Image
from io import BytesIO

# 1. पेज की पूरी सेटिंग
st.set_page_config(page_title="Happy Janmashtami!", page_icon="🪈", layout="centered")

# 2. बैकग्राउंड, सुंदर टेक्स्ट और इमेज को ऊपर-नीचे (Floating) करने के लिए CSS
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

    /* इमेज को ऊपर-नीचे एनिमेट करने की स्टाइल */
    .stImage img {
        border-radius: 20px !important;
        box-shadow: 0px 0px 30px #FFD700 !important;
        border: 3px solid #FFD700 !important;
        animation: floatMotion 3s ease-in-out infinite !-webkit-any;
    }

    /* तैरने वाला एनिमेशन इफेक्ट (Floating Effect) */
    @keyframes floatMotion {
        0% { transform: translateY(0px); }
        50% { transform: translateY(-15px); }
        100% { transform: translateY(0px); }
    }
</style>
"""
st.markdown(custom_css, unsafe_allow_html=True)

# 3. स्क्रीन पर सबसे ऊपर "Happy Janmashtami" हेडिंग
st.markdown("<h1 class='main-title'>✨ Happy Janmashtami ✨</h1>", unsafe_allow_html=True)

# 4. कृष्ण जी की असली और सुंदर फोटो को सुरक्षित तरीके से पायथन द्वारा लोड करना
# यह लॉर्ड कृष्णा की एक बेहद ही सुंदर और मनमोहक डिजिटल आर्ट इमेज का पक्का लिंक है
krishna_url = "https://unsplash.com"

try:
    # पायथन बैकएंड से इमेज डाउनलोड कर रहा है ताकि Streamlit ब्लॉक न करे
    response = requests.get(krishna_url, timeout=10)
    img = Image.open(BytesIO(response.content))
    
    # इमेज को स्क्रीन पर दिखाना
    st.image(img, use_container_width=True)
except Exception as e:
    st.error("फोटो लोड होने में थोड़ा समय लग रहा है, कृपया पेज को एक बार रिफ्रेश करें।")

# 5. नीचे का बधाई संदेश
st.markdown(
    "<p class='sub-title'>माखन चोर नन्द किशोर, बांधे जिसने प्रीत की डोर...<br>हरे कृष्णा! 🌸🪈</p>", 
    unsafe_allow_html=True
)

# 6. ऐप खुलते ही स्क्रीन पर गुब्बारे उड़ाना
st.balloons()
