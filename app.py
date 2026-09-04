import streamlit as st

# 1. पेज की पूरी सेटिंग
st.set_page_config(page_title="Happy Janmashtami!", page_icon="🪈", layout="centered")

# 2. एडवांस CSS: बैकग्राउंड, हेडिंग और ऊपर-नीचे (Floating) होने वाला एनिमेशन
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

    /* कृष्ण जी की फोटो के लिए स्पेशल एनिमेटेड कंटेनर */
    .krishna-box {
        display: flex;
        justify-content: center;
        align-items: center;
        margin: 20px auto;
    }
    
    /* फोटो की स्टाइल और ऊपर-नीचे होने का मोशन (Floating Effect) */
    .krishna-box img {
        width: 280px;
        max-width: 90%;
        border-radius: 15px;
        box-shadow: 0px 0px 25px #FFD700;
        animation: floatMotion 3s ease-in-out infinite;
    }

    /* एनिमेट करने का नियम (20 पिक्सेल ऊपर और नीचे जाना) */
    @keyframes floatMotion {
        0% {
            transform: translateY(0px);
        }
        50% {
            transform: translateY(-20px);
        }
        100% {
            transform: translateY(0px);
        }
    }
</style>
"""
st.markdown(custom_css, unsafe_allow_html=True)

# 3. स्क्रीन पर सबसे ऊपर "Happy Janmashtami" लिखना
st.markdown("<h1 class='main-title'>✨ Happy Janmashtami ✨</h1>", unsafe_allow_html=True)

# 4. कृष्ण जी की सुंदर तस्वीर (Wikimedia से डायरेक्ट और पक्का लिंक)
# यह लिंक हमेशा ओपन होगा और इसमें CSS एनिमेशन लगा हुआ है
safe_krishna_url = "https://wikimedia.org"

st.markdown(
    f"""
    <div class="krishna-box">
        <img src="{safe_krishna_url}" alt="Jai Shree Krishna">
    </div>
    """,
    unsafe_allow_html=True
)

# 5. नीचे का सुंदर मैसेज
st.markdown(
    "<p class='sub-title'>माखन चोर नन्द किशोर, बांधे जिसने प्रीत की डोर...<br>हरे कृष्णा! 🌸🪈</p>", 
    unsafe_allow_html=True
)

# 6. ऐप खुलते ही गुब्बारे उड़ाना
st.balloons()
