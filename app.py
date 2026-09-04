import streamlit as str
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
    .footer {
        text-align: center;
        color: #ffb3ff;
        font-size: 1.2rem;
        margin-top: 50px;
    }
</style>
"""
st.markdown(custom_css, unsafe_allow_html=True)

# 3. Lottie Animation लोड करने का फंक्शन (कृष्ण जी या त्योहार से जुड़ा एनिमेशन)
def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

# एक सुंदर कृष्ण जी/मटकी एनिमेटेड JSON लिंक (LottieFiles से)
# नोट: आप चाहें तो lottiefiles.com से अपनी पसंद का कोई भी दूसरा लिंक बदल सकते हैं
lottie_krishna = load_lottieurl("https://lottiefiles.com") 

# 4. स्क्रीन पर कंटेंट दिखाना
st.markdown("<h1 class='main-title'>✨ Happy Janmashtami ✨</h1>", unsafe_allow_html=True)

if lottie_krishna:
    st_lottie(lottie_krishna, speed=1, reverse=False, loop=True, quality="high", height=400, key="krishna_anim")
else:
    # अगर एनिमेशन लोड न हो, तो बैकअप के लिए एक इमेज (यहाँ आप कृष्ण जी की कोई भी इमेज लिंक डाल सकते हैं)
    st.image("https://unsplash.com", caption="Jai Shree Krishna", use_container_width=True)

st.markdown("<p class='sub-title'>माखन चोर नन्द किशोर, बांधे जिसने प्रीत की डोर...<br>हरे कृष्णा! 🌸🪈</p>", unsafe_allow_html=True)

# 5. उत्सव का प्रभाव (गुब्बारे/पटाखे जैसा फील देने के लिए Streamlit का इन-बिल्ट बैलून)
st.balloons()
