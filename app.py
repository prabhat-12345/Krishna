import streamlit as st

# 1. पेज की सेटिंग
st.set_page_config(page_title="Happy Janmashtami!", page_icon="🪈", layout="centered")

# 2. बैकग्राउंड, सुंदर टेक्स्ट और इमेज को ऊपर-नीचे (Floating) एनिमेट करने के लिए CSS
custom_css = """
<style>
    /* ऐप का बैकग्राउंड */
    .stApp {
        background: linear-gradient(135deg, #1a0033 0%, #4d004d 100%);
        color: #ffffff;
    }
    
    /* मुख्य हेडिंग */
    .main-title {
        font-family: 'Georgia', serif;
        color: #FFD700;
        text-align: center;
        font-size: 3rem;
        font-weight: bold;
        text-shadow: 2px 2px 15px #ff6600;
        margin-top: 20px;
        margin-bottom: 20px;
    }
    
    /* बधाई संदेश */
    .sub-title {
        font-family: 'Georgia', serif;
        color: #00FFCC;
        text-align: center;
        font-size: 1.4rem;
        line-height: 1.8;
        margin-top: 30px;
        text-shadow: 1px 1px 5px #000;
    }

    /* कृष्ण जी की फोटो को ऊपर-नीचे एनिमेट करने का CSS */
    .krishna-container {
        display: flex;
        justify-content: center;
        align-items: center;
        margin: 20px auto;
    }
    
    .floating-img {
        width: 320px; /* आप चाहें तो साइज छोटा-बड़ा कर सकते हैं */
        border-radius: 20px;
        box-shadow: 0px 0px 25px #FFD700;
        animation: float 3s ease-in-out infinite;
    }

    /* ऊपर-नीचे होने वाला एनिमेशन इफेक्ट */
    @keyframes float {
        0% {
            transform: translateY(0px);
        }
        50% {
            transform: translateY(-20px); /* 20 पिक्सेल ऊपर जाएगा */
        }
        100% {
            transform: translateY(0px);
        }
    }
</style>
"""
st.markdown(custom_css, unsafe_allow_html=True)

# 3. स्क्रीन पर "Happy Janmashtami" हेडिंग
st.markdown("<h1 class='main-title'>✨ Happy Janmashtami ✨</h1>", unsafe_allow_html=True)

# 4. कृष्ण जी की सुंदर फोटो (Floating Animation के साथ)
# यहाँ एक बेहतरीन और हाई-क्वालिटी कृष्ण जी की तस्वीर का डायरेक्ट लिंक डाला है
krishna_image_url = "https://unsplash.com"

st.markdown(
    f"""
    <div class="krishna-container">
        <img class="floating-img" src="{krishna_image_url}" alt="Jai Shree Krishna">
    </div>
    """,
    unsafe_allow_html=True
)

# 5. नीचे का बधाई संदेश
st.markdown(
    "<p class='sub-title'>माखन चोर नन्द किशोर, बांधे जिसने प्रीत की डोर...<br>हरे कृष्णा! 🌸🪈</p>", 
    unsafe_allow_html=True
)

# 6. स्क्रीन पर गुब्बारे उड़ाने के लिए
st.balloons()
