import streamlit as st
import os

# 1. पेज की पूरी प्रीमियम VLVIP सेटिंग (मोबाइल स्क्रीन पर स्क्रॉल बार छिपाने के लिए)
st.set_page_config(page_title="Happy Janmashtami!", page_icon="🪈", layout="centered")

# 2. एडवांस CSS: हेडिंग, फोटो बॉर्डर और नीचे के कोट्स—सब कुछ 100% लाइव एनिमेटेड और नियॉन ग्लो
custom_css = """
<style>
    /* ऐप का शानदार डार्क और मॉडर्न फेस्टिव बैकग्राउंड */
    .stApp {
        background: linear-gradient(135deg, #090014 0%, #15002a 50%, #26004d 100%) !important;
        color: #ffffff;
        overflow: hidden !important;
    }
    
    /* मुख्य कंटेनर को मोबाइल स्क्रीन की हाइट में फिट करने के लिए */
    .block-container {
        padding-top: 0.8rem !important;
        padding-bottom: 0rem !important;
        max-width: 450px !important;
    }
    
    /* मुख्य हेडिंग जो धीरे-धीरे चमकते हुए अपना रंग बदलेगी (Animated Gradient Text) */
    .main-title {
        font-family: 'Georgia', serif;
        text-align: center;
        font-size: 2.5rem;
        font-weight: bold;
        letter-spacing: 1px;
        margin-top: 5px;
        margin-bottom: 5px;
        background: linear-gradient(to right, #ff007f, #FFD700, #00ffcc, #ff007f);
        background-size: 200% auto;
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        animation: textShine 4s linear infinite, headingGlow 2s ease-in-out infinite alternate;
    }

    /* जिसने भेजा है उसका नाम दिखाने के लिए VIP शाइनिंग स्टाइल */
    .sender-box {
        text-align: center;
        margin-bottom: 10px;
    }
    .sender-prefix {
        font-family: 'Georgia', serif;
        color: #00ffcc;
        font-size: 1rem;
        letter-spacing: 2px;
        text-transform: uppercase;
    }
    .sender-name {
        font-family: 'Georgia', serif;
        font-size: 1.6rem;
        font-weight: bold;
        text-transform: uppercase;
        background: linear-gradient(45deg, #FFD700, #ffaa00);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        text-shadow: 0px 0px 10px rgba(255, 170, 0, 0.5);
    }
    
    /* जादू 1: इमेज के चारों तरफ का वीआईपी नियॉन बॉर्डर जो लगातार अपनी चमक और रंग बदलेगा (Pulse & Rotate Glow) */
    .stImage img {
        display: block;
        margin-left: auto;
        margin-right: auto;
        max-height: 275px !important;
        width: auto !important;
        border-radius: 20px !important;
        border: 2px solid rgba(255, 0, 127, 0.4) !important;
        animation: superFloat 4s ease-in-out infinite, photoGlow 3s ease-in-out infinite alternate !important;
    }

    /* जादू 2: नीचे का प्रीमियम शुभकामनाएं बॉक्स जिसके टेक्स्ट अब सोने की लहर की तरह लाइव चमकेंगे (Shining Quotes) */
    .wishes-container {
        background: rgba(255, 255, 255, 0.04);
        border-radius: 15px;
        padding: 12px;
        margin-top: 15px;
        border: 1px solid rgba(255, 0, 127, 0.15);
        box-shadow: 0px 0px 15px rgba(153, 0, 255, 0.15);
        text-align: center;
    }

    .wish-text {
        font-family: 'Georgia', serif;
        color: #ffffff;
        font-size: 1.05rem;
        line-height: 1.6;
        margin-bottom: 8px;
        background: linear-gradient(to right, #ffffff, #FFD700, #00ffcc, #ffffff);
        background-size: 200% auto;
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        animation: textShine 5s linear infinite;
    }
    
    .wish-highlight {
        font-weight: bold;
        background: linear-gradient(to right, #FFD700, #ff6600, #FFD700);
        background-size: 200% auto;
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        animation: textShine 3s linear infinite;
    }

    /* सभी एनीमेशन के सीक्रेट रूल्स */
    @keyframes textShine {
        0% { background-position: 0% center; }
        100% { background-position: 200% center; }
    }
    
    @keyframes headingGlow {
        0% { filter: drop-shadow(0 0 5px rgba(255, 0, 127, 0.6)); }
        100% { filter: drop-shadow(0 0 15px rgba(255, 215, 0, 0.8)); }
    }

    @keyframes photoGlow {
        0% { box-shadow: 0px 0px 15px #ff007f, 0px 0px 5px #9900ff !important; }
        100% { box-shadow: 0px 0px 35px #FFD700, 0px 0px 15px #ff6600 !important; }
    }

    @keyframes superFloat {
        0% { transform: translateY(0px); }
        50% { transform: translateY(-12px); }
        100% { transform: translateY(0px); }
    }
</style>
"""
st.markdown(custom_css, unsafe_allow_html=True)

# 3. जादुई नाम बदलने वाला कोड (URL Prompt Link)
query_params = st.query_params
sender = query_params.get("name", "")

# 4. एनिमेटेड हेडिंग
st.markdown("<h1 class='main-title'>✨ Happy Janmashtami ✨</h1>", unsafe_allow_html=True)

# 5. अगर किसी ने अपना नाम लिंक में भेजा है तो वह यहाँ चमकेगा
if sender:
    st.markdown(
        f"""
        <div class="sender-box">
            <span class="sender-prefix">की तरफ से आपको</span><br>
            <span class="sender-name">🎉 {sender} 🎉</span>
        </div>
        """, 
        unsafe_allow_html=True
    )

# 6. तुम्हारी वही असली सुंदर फोटो 'images (52).jpeg' (अब डबल एनिमेटेड ग्लो के साथ)
image_path = "images (52).jpeg"

if os.path.exists(image_path):
    st.image(image_path, use_container_width=False)
else:
    st.warning("कृपया पेज को एक बार रिफ्रेश करें।")

# 7. नीचे का पूरी तरह से चमकता हुआ एनिमेटेड शुभकामनाएं बॉक्स
st.markdown(
    """
    <div class="wishes-container">
        <p class="wish-text">🌸 माखन चोर नन्द किशोर, बांधे जिसने प्रीत की डोर... <span class="wish-highlight">हरे कृष्णा! 🪈</span></p>
        <p class="wish-text">✨ श्री कृष्ण के कदम आपके घर आएं, आप खुशियों के दीप जलाएं! <span class="wish-highlight">शुभ जन्माष्टमी 🦚</span></p>
        <p class="wish-text" style="font-size: 0.95rem; margin-bottom: 0;">May Lord Krishna fill your life with Love, Peace, and Happiness! 🌟</p>
    </div>
    """, 
    unsafe_allow_html=True
)

# 8. ऐप खुलते ही स्क्रीन पर गुब्बारे उड़ाना
st.balloons()
