import streamlit as st

# 1. पेज की पूरी सेटिंग
st.set_page_config(page_title="Happy Janmashtami!", page_icon="🪈", layout="centered")

# 2. बैकग्राउंड और फ्लोटिंग एनिमेशन के लिए CSS
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
        margin-bottom: 25px;
    }
    .sub-title {
        font-family: 'Georgia', serif;
        color: #00FFCC;
        text-align: center;
        font-size: 1.3rem;
        line-height: 1.8;
        margin-top: 25px;
        text-shadow: 1px 1px 5px #000;
    }
    .image-container {
        display: flex;
        justify-content: center;
        align-items: center;
        margin: 10px auto;
        animation: floatMotion 3s ease-in-out infinite;
    }
    
    /* ऊपर-नीचे होने का मोशन */
    @keyframes floatMotion {
        0% { transform: translateY(0px); }
        50% { transform: translateY(-15px); }
        100% { transform: translateY(0px); }
    }
</style>
"""
st.markdown(custom_css, unsafe_allow_html=True)

# 3. मुख्य हेडिंग
st.markdown("<h1 class='main-title'>✨ Happy Janmashtami ✨</h1>", unsafe_allow_html=True)

# 4. आईफ्रेम (iframe) का उपयोग करके सीधे लाइव फोटो एम्बेड करना जो ब्लॉक नहीं होगी
# इसमें कृष्ण जी की बहुत ही मनमोहक बाल रूप की तस्वीर दिखाई देगी
iframe_html = """
<div class="image-container">
    <iframe src="https://giphy.com" 
            width="300" 
            height="300" 
            frameBorder="0" 
            style="border-radius: 20px; box-shadow: 0px 0px 25px #FFD700; pointer-events: none;" 
            allowFullScreen>
    </iframe>
</div>
"""
st.components.v1.html(iframe_html, height=330)

# 5. नीचे का बधाई संदेश
st.markdown(
    "<p class='sub-title'>माखन चोर नन्द किशोर, बांधे जिसने प्रीत की डोर...<br>हरे कृष्णा! 🌸🪈</p>", 
    unsafe_allow_html=True
)

# 6. गुब्बारे उड़ाना
st.balloons()
