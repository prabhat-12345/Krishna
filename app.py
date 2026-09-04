import streamlit as st

# 1. पेज की पूरी सेटिंग
st.set_page_config(page_title="Happy Janmashtami!", page_icon="🪈", layout="centered")

# 2. बैकग्राउंड, सुंदर टेक्स्ट और बिना इमेज वाला 100% पक्का एनिमेशन इफेक्ट
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

    /* एनिमेटेड बॉक्स की डिजाइन (जो स्क्रीन पर बिना इमेज के भी लोड होगा) */
    .krishna-art-box {
        width: 280px;
        height: 280px;
        margin: 20px auto;
        background: radial-gradient(circle, #3d0066 30%, #1a0033 100%);
        border-radius: 50%;
        border: 4px solid #FFD700;
        box-shadow: 0px 0px 30px #FFD700;
        position: relative;
        display: flex;
        flex-direction: column;
        justify-content: center;
        align-items: center;
        animation: floatMotion 3s ease-in-out infinite;
    }

    /* मोरपंख का एनिमेटेड रूप (Pure CSS) */
    .peacock-feather {
        width: 40px;
        height: 70px;
        background: linear-gradient(#00ccff, #0033cc);
        border-radius: 50% 50% 20% 20%;
        box-shadow: 0px 0px 15px #00ffcc, inset 0 0 10px #00ff00;
        position: relative;
        margin-bottom: 15px;
    }
    .peacock-feather::before {
        content: '';
        position: absolute;
        width: 16px;
        height: 30px;
        background: #ffcc00;
        border-radius: 50%;
        top: 15px;
        left: 12px;
        box-shadow: 0 0 5px #ff6600;
    }

    /* सुनहरी बांसुरी की डिजाइन (Pure CSS) */
    .golden-flute {
        width: 200px;
        height: 12px;
        background: linear-gradient(to bottom, #ffe066, #b38600);
        border-radius: 6px;
        box-shadow: 0px 0px 15px #FFD700;
        position: relative;
    }
    /* बांसुरी के छेद */
    .flute-holes {
        position: absolute;
        width: 100%;
        display: flex;
        justify-content: space-around;
        padding: 0 20px;
        box-sizing: border-box;
        top: 3px;
    }
    .hole {
        width: 6px;
        height: 6px;
        background: #1a0033;
        border-radius: 50%;
    }

    /* ऊपर-नीचे होने वाला स्मूथ मोशन */
    @keyframes floatMotion {
        0% { transform: translateY(0px) rotate(0deg); }
        50% { transform: translateY(-15px) rotate(2deg); }
        100% { transform: translateY(0px) rotate(0deg); }
    }
</style>
"""
st.markdown(custom_css, unsafe_allow_html=True)

# 3. स्क्रीन पर सबसे ऊपर "Happy Janmashtami" लिखना
st.markdown("<h1 class='main-title'>✨ Happy Janmashtami ✨</h1>", unsafe_allow_html=True)

# 4. बिना किसी इमेज के शुद्ध कोड से बना सुंदर कृष्ण कलाकृति बॉक्स
st.markdown(
    """
    <div class="krishna-art-box">
        <div class="peacock-feather"></div>
        <div class="golden-flute">
            <div class="flute-holes">
                <div class="hole"></div>
                <div class="hole"></div>
                <div class="hole"></div>
                <div class="hole"></div>
                <div class="hole"></div>
            </div>
        </div>
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
