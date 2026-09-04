import streamlit as st
import requests
from streamlit_lottie import st_lottie

# 1. पेज की सेटिंग (Title और Favicon)
st.set_page_config(page_title="Happy Janmashtami!", page_icon="🪈", layout="centered")

# 2. बैकग्राउंड को सुंदर (Dark Festive) बनाने के लिए CSS
custom_css = """
<style>
    .stApp {
        background: linear-gradient(135deg, #1a0033 0%, #4d004d 100%);
        color: #ffffff;
    }
    .main-title {
        font-family: 'Georgia', serif;
        color: #FFD700;
        text-align: center;
        font-size: 3rem;
        font-weight: bold;
        text-shadow: 2px 2px 10px #ff6600;
        margin-top: 20px;
    }
    .sub-title {
        font-family: 'Courier New', monospace;
        color: #00FFCC;
        text-align: center;
        font-size: 1.5rem;
        margin-bottom: 30px;
    }
</style>
"""
st.markdown(custom_css, unsafe_allow_html=True)

# 3. Lottie Animation लोड करने का फंक्शन
def load_lottieurl(url):
    try:
        r = requests.get(url)
        if r.status_code == 200:
            return r.json()
    except:
        return None

# त्योहार से जुड़ा एनिमेशन लिंक
lottie_krishna = load_lottieurl("https://lottie.host") 

# 4. स्क्रीन पर कंटेंट दिखाना
st.markdown("<h1 class='main-title'>✨ Happy Janmashtami ✨</h1>", unsafe_allow_html=True)

if lottie_krishna:
    st_lottie(lottie_krishna, speed=1, reverse=False, loop=True, quality="high", height=400, key="krishna_anim")
else:
    # बैकअप इमेज
    st.image("https://unsplash.com", caption="Jai Shree Krishna", use_container_width=True)

st.markdown("<p class='sub-title'>माखन चोर नन्द किशोर, बांधे जिसने प्रीत की डोर...<br>हरे कृष्णा! 🌸🪈</p>", unsafe_allow_html=True)

# 5. उत्सव का प्रभाव (गुब्बारे)
st.balloons()
