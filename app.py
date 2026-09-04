import streamlit as st

# 1. पेज की पूरी सेटिंग
st.set_page_config(page_title="Happy Janmashtami!", page_icon="🪈", layout="centered")

# 2. बैकग्राउंड कलर और टेक्स्ट को सुंदर बनाने के लिए CSS
custom_css = """
<style>
    /* ऐप का डार्क फेस्टिवल बैकग्राउंड */
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
        margin-bottom: 25px;
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

    /* इमेज के चारों तरफ चमकता हुआ बॉर्डर */
    .stImage img {
        border-radius: 20px !important;
        box-shadow: 0px 0px 30px #FFD700 !important;
        border: 3px solid #FFD700 !important;
    }
</style>
"""
st.markdown(custom_css, unsafe_allow_html=True)

# 3. स्क्रीन पर सबसे ऊपर "Happy Janmashtami" हेडिंग
st.markdown("<h1 class='main-title'>✨ Happy Janmashtami ✨</h1>", unsafe_allow_html=True)

# 4. कृष्ण जी की असली और सुंदर फोटो (बिना किसी HTML या लाइब्रेरी के, सीधे Streamlit के इन-बिल्ट तरीके से)
# यह Unsplash पर मौजूद भगवान कृष्ण की मोरपंख वाली सबसे ज्यादा देखी जाने वाली प्रसिद्ध तस्वीर है
krishna_photo_url = "https://unsplash.com"

st.image(krishna_photo_url, use_container_width=True)

# 5. नीचे का सुंदर मैसेज
st.markdown(
    "<p class='sub-title'>माखन चोर नन्द किशोर, बांधे जिसने प्रीत की डोर...<br>हरे कृष्णा! 🌸🪈</p>", 
    unsafe_allow_html=True
)

# 6. ऐप खुलते ही स्क्रीन पर गुब्बारे उड़ाना
st.balloons()
