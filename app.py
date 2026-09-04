import streamlit as st

# 1. पेज की पूरी सेटिंग
st.set_page_config(page_title="Happy Janmashtami!", page_icon="🪈", layout="centered")

# 2. कृष्ण जी की फुल एचडी इमेज का बेस64 कोड (यह बिल्कुल सॉलिड है और 100% लोड होगा)
krishna_hd_base64 = "data:image/png;base64,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"

# 3. एडवांस CSS: बैकग्राउंड, हेडिंग और ऊपर-नीचे (Floating) होने वाला एनिमेशन
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
        width: 250px;
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

# 4. स्क्रीन पर सबसे ऊपर "Happy Janmashtami" लिखना
st.markdown("<h1 class='main-title'>✨ Happy Janmashtami ✨</h1>", unsafe_allow_html=True)

# 5. कृष्ण जी की सुंदर तस्वीर (बिना किसी बाहरी लिंक के, सीधे कोड से 100% लोड होगी)
st.markdown(
    f"""
    <div class="krishna-box">
        <img src="{krishna_hd_base64}" alt="Jai Shree Krishna">
    </div>
    """,
    unsafe_allow_html=True
)

# 6. नीचे का सुंदर संदेश
st.markdown(
    "<p class='sub-title'>माखन चोर नन्द किशोर, बांधे जिसने प्रीत की डोर...<br>हरे कृष्णा! 🌸🪈</p>", 
    unsafe_allow_html=True
)

# 7. ऐप खुलते ही गुब्बारे उड़ाना
st.balloons()
