import streamlit as st

# 1. पेज की पूरी प्रीमियम सेटिंग
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

    /* एनीमेशन बॉक्स की स्टाइल */
    .gif-container {
        display: flex;
        justify-content: center;
        align-items: center;
        margin: 20px auto;
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

# 4. Giphy से सीधे लाइव श्री कृष्ण जी का 3D एनिमेशन एम्बेड करना (यह कभी ब्लॉक नहीं होगा)
# इसमें बिना किसी एरर बॉक्स के, सीधे लाइव हिलती-डुलती कृष्ण जी की सुंदर छवि दिखेगी
krishna_gif_html = """
<div class="gif-container">
    <iframe src="https://giphy.com" 
            width="300" 
            height="300" 
            frameBorder="0" 
            style="border-radius: 25px; box-shadow: 0px 0px 35px #FFD700, 0px 0px 15px #ff6600; pointer-events: none;" 
            allowFullScreen>
    </iframe>
</div>
"""
st.markdown(krishna_gif_html, unsafe_allow_html=True)

# 5. नीचे का सुंदर मैसेज
st.markdown(
    "<p class='sub-title'>माखन चोर नन्द किशोर, बांधे जिसने प्रीत की डोर...<br>हरे कृष्णा! 🌸🪈</p>", 
    unsafe_allow_html=True
)

# 6. ऐप खुलते ही स्क्रीन पर गुब्बारे उड़ाना
st.balloons()
