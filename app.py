import streamlit as st

# 1. पेज की पूरी सेटिंग
st.set_page_config(page_title="Happy Janmashtami!", page_icon="🪈", layout="centered")

# 2. ऐप का शानदार फेस्टिव बैकग्राउंड और टेक्स्ट स्टाइल्स के लिए CSS
custom_css = """
<style>
    /* ऐप का डार्क और चमकीला फेस्टिवल बैकग्राउंड */
    .stApp {
        background: linear-gradient(135deg, #1a0033 0%, #4d004d 100%) !important;
        color: #ffffff;
    }
    
    /* मुख्य हेडिंग */
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
    
    /* नीचे का सुंदर मैसेज */
    .sub-title {
        font-family: 'Georgia', serif;
        color: #00FFCC;
        text-align: center;
        font-size: 1.3rem;
        line-height: 1.8;
        margin-top: 25px;
        text-shadow: 1px 1px 5px #000;
    }

    /* Streamlit की इमेज के चारों तरफ चमकता हुआ बॉर्डर देने के लिए */
    .stImage img {
        border-radius: 20px;
        box-shadow: 0px 0px 25px #FFD700;
        border: 3px solid #FFD700;
    }
</style>
"""
st.markdown(custom_css, unsafe_allow_html=True)

# 3. स्क्रीन पर सबसे ऊपर "Happy Janmashtami" लिखना
st.markdown("<h1 class='main-title'>✨ Happy Janmashtami ✨</h1>", unsafe_allow_html=True)

# 4. कृष्ण जी की असली और सुंदर फोटो (Streamlit के ऑफिशियल फंक्शन से जो कभी ब्लॉक नहीं होती)
# इसमें कृष्ण जी की बहुत ही मनमोहक तस्वीर दिखाई देगी
krishna_photo_url = "https://unsplash.com"

st.image(krishna_photo_url, use_container_width=True)

# 5. नीचे का सुंदर मैसेज
st.markdown(
    "<p class='sub-title'>माखन चोर नन्द किशोर, बांधे जिसने प्रीत की डोर...<br>हरे कृष्णा! 🌸🪈</p>", 
    unsafe_allow_html=True
)

# 6. ऐप खुलते ही स्क्रीन पर गुब्बारे उड़ाना
st.balloons()
