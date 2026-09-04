import streamlit as st

# 1. पेज की पूरी प्रीमियम सेटिंग
st.set_page_config(page_title="Happy Janmashtami!", page_icon="🪈", layout="centered")

# 2. एडवांस CSS: प्रीमियम डार्क थीम, चमकती हेडिंग और स्मूथ फ्लोटिंग एनीमेशन
custom_css = """
<style>
    /* ऐप का शानदार डार्क फेस्टिवल बैकग्राउंड */
    .stApp {
        background: linear-gradient(135deg, #120024 0%, #2d004d 50%, #4d004d 100%) !important;
        color: #ffffff;
    }
    
    /* मुख्य चमकती हुई हेडिंग */
    .main-title {
        font-family: 'Georgia', serif;
        color: #FFD700;
        text-align: center;
        font-size: 2.8rem;
        font-weight: bold;
        text-shadow: 0px 0px 15px #ff6600, 0px 0px 5px #FFD700;
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

    /* कृष्ण डिज़ाइन बॉक्स (Floating Effect) */
    .krishna-box {
        width: 280px;
        height: 280px;
        margin: 20px auto;
        background: radial-gradient(circle, #3d0066 30%, #120024 100%);
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

    /* मोरपंख (Pure CSS) */
    .peacock-feather {
        width: 35px;
        height: 60px;
        background: linear-gradient(#00ccff, #0033cc);
        border-radius: 50% 50% 20% 20%;
        box-shadow: 0px 0px 15px #00ffcc, inset 0 0 10px #00ff00;
        position: absolute;
        top: 25px;
        transform: rotate(15deg);
        z-index: 2;
    }
    .peacock-feather::before {
        content: '';
        position: absolute;
        width: 14px;
        height: 25px;
        background: #ffcc00;
        border-radius: 50%;
        top: 12px;
        left: 10px;
        box-shadow: 0 0 5px #ff6600;
    }

    /* सोने का मुकुट (Crown - Pure CSS) */
    .krishna-crown {
        width: 80px;
        height: 50px;
        background: linear-gradient(135deg, #ffe066, #b38600);
        clip-path: polygon(0% 100%, 20% 40%, 40% 0%, 50% 50%, 60% 0%, 80% 40%, 100% 100%);
        box-shadow: 0px 0px 15px #FFD700;
        position: absolute;
        top: 75px;
        border-radius: 5px;
    }

    /* तिलक (Tilak) */
    .tilak {
        width: 10px;
        height: 35px;
        background: #ff3333;
        border-radius: 0 0 5px 5px;
        position: absolute;
        top: 130px;
        box-shadow: 0 0 8px #ff3333;
    }
    .tilak::before {
        content: '';
        position: absolute;
        width: 16px;
        height: 25px;
        border: 2px solid #FFD700;
        border-top: none;
        border-radius: 0 0 8px 8px;
        left: -5px;
        top: -5px;
    }

    /* सुनहरी बांसुरी (Pure CSS) */
    .golden-flute {
        width: 220px;
        height: 14px;
        background: linear-gradient(to bottom, #ffe066, #b38600);
        border-radius: 7px;
        box-shadow: 0px 0px 15px #FFD700;
        position: absolute;
        bottom: 50px;
        transform: rotate(-8deg);
    }
    /* बांसुरी के छेद */
    .flute-holes {
        position: absolute;
        width: 100%;
        display: flex;
        justify-content: space-around;
        padding: 0 25px;
        box-sizing: border-box;
        top: 4px;
    }
    .hole {
        width: 6px;
        height: 6px;
        background: #120024;
        border-radius: 50%;
    }

    /* ऊपर-नीचे होने वाला स्मूथ मोशन */
    @keyframes floatMotion {
        0% { transform: translateY(0px) rotate(0deg); }
        50% { transform: translateY(-15px) rotate(1deg); }
        100% { transform: translateY(0px) rotate(0deg); }
    }
</style>
"""
st.markdown(custom_css, unsafe_allow_html=True)

# 3. स्क्रीन पर सबसे ऊपर "Happy Janmashtami" लिखना
st.markdown("<h1 class='main-title'>✨ Happy Janmashtami ✨</h1>", unsafe_allow_html=True)

# 4. बिना किसी बाहरी इमेज के शुद्ध कोड से बना सुंदर कृष्ण कलाकृति बॉक्स
st.markdown(
    """
    <div class="krishna-box">
        <div class="peacock-feather"></div>
        <div class="krishna-crown"></div>
        <div class="tilak"></div>
        <div class="golden-flute">
            <div class="flute-holes">
                <div class="hole"></div>
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
