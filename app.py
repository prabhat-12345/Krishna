import streamlit as st
import os

# 1. पेज की पूरी प्रीमियम VLVIP सेटिंग
st.set_page_config(page_title="Happy Janmashtami!", page_icon="🪈", layout="centered")

# 2. एडवांस CSS: शाही डार्क गोल्ड और नियॉन मैजेंटा थीम
custom_css = """
<style>
    /* ऐप का प्रीमियम और गहरा रॉयल फेस्टिव बैकग्राउंड */
    .stApp {
        background: linear-gradient(135deg, #090014 0%, #15002a 50%, #26004d 100%) !important;
        color: #ffffff;
    }
    
    /* मुख्य चमकती हुई मॉडर्न हेडिंग */
    .main-title {
        font-family: 'Georgia', serif;
        color: #FFFFFF;
        text-align: center;
        font-size: 3.2rem;
        font-weight: bold;
        text-shadow: 0px 0px 10px #ff007f, 0px 0px 25px #ff007f, 0px 0px 40px #9900ff;
        margin-top: 15px;
        margin-bottom: 5px;
        letter-spacing: 2px;
    }

    /* जिसने भेजा है उसका नाम दिखाने के लिए VIP स्टाइल */
    .sender-name {
        font-family: 'Georgia', serif;
        color: #FFD700;
        text-align: center;
        font-size: 1.8rem;
        font-weight: bold;
        text-transform: uppercase;
        text-shadow: 0px 0px 15px #ff6600;
        margin-bottom: 25px;
        background: linear-gradient(45deg, #FFD700, #ff6600);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
    }
    
    /* नीचे का सुंदर और साफ बधाई संदेश बॉक्स */
    .wishes-container {
        background: rgba(255, 255, 255, 0.05);
        border-radius: 20px;
        padding: 20px;
        margin-top: 30px;
        border: 1px solid rgba(255, 0, 127, 0.2);
        box-shadow: 0px 0px 20px rgba(153, 0, 255, 0.2);
    }

    .wish-text {
        font-family: 'Georgia', serif;
        color: #00ffcc;
        text-align: center;
        font-size: 1.25rem;
        line-height: 1.8;
        text-shadow: 0px 0px 8px rgba(0, 255, 204, 0.3);
        margin-bottom: 15px;
    }

    .wish-highlight {
        color: #FFD700;
        font-weight: bold;
        text-shadow: 0px 0px 5px #ff6600;
    }

    /* इमेज के चारों तरफ का वीआईपी नियॉन ग्लो और 3D फ्लोटिंग */
    .stImage img {
        border-radius: 25px !important;
        box-shadow: 0px 0px 35px #ff007f, 0px 0px 15px #9900ff !important;
        border: 2px solid rgba(255, 0, 127, 0.3) !important;
        animation: superFloat 4s ease-in-out infinite !important;
    }

    /* और भी ज़्यादा स्मूथ ऊपर-नीचे तैरने का मोशन */
    @keyframes superFloat {
        0% { transform: translateY(0px) scale(1); }
        50% { transform: translateY(-15px) scale(1.01); }
        100% { transform: translateY(0px) scale(1); }
    }
</style>
"""
st.markdown(custom_css, unsafe_allow_html=True)

# 3. जादुई नाम बदलने वाला कोड (URL Prompt Link)
# अगर लिंक ऐसा होगा: https:// तो स्क्रीन पर Rahul का नाम दिखेगा
query_params = st.query_params
sender = query_params.get("name", "")

# 4. स्क्रीन पर सबसे ऊपर "Happy Janmashtami" हेडिंग
st.markdown("<h1 class='main-title'>✨ Happy Janmashtami ✨</h1>", unsafe_allow_html=True)

# अगर किसी ने अपना नाम लिंक में भेजा है तो वह यहाँ चमकेगा
if sender:
    st.markdown(f"<div class='sender-name'>👉 की तरफ से आपको 👈</div>", unsafe_allow_html=True)
    st.markdown(f"<div class='sender-name'>🎉 {sender} 🎉</div>", unsafe_allow_html=True)

# 5. तुम्हारी वही असली सुंदर फोटो 'images (52).jpeg'
image_path = "images (52).jpeg"

if os.path.exists(image_path):
    st.image(image_path, use_container_width=True)
else:
    st.warning("कृपया ऐप को लोड होने के लिए 5 सेकंड का समय दें या पेज को एक बार रिफ्रेश करें।")

# 6. नीचे का बिल्कुल नया और प्रीमियम शुभकामनाएं (Best Wishes) बॉक्स
st.markdown(
    """
    <div class="wishes-container">
        <p class="wish-text">🌸 माखन चोर नन्द किशोर, बांधे जिसने प्रीत की डोर...<br>हरे कृष्णा! 🪈</p>
        <p class="wish-text"><span class="wish-highlight">✨ श्री कृष्ण के कदम आपके घर आएं...</span><br>आप खुशियों के दीप जलाएं, परेशानी आपसे आंखें चुराए! 🦚</p>
        <p class="wish-text">💫 May Lord Krishna steal all your tensions and fill your life with <span class="wish-highlight">Love, Peace, and Happiness!</span> 🌟</p>
    </div>
    """, 
    unsafe_allow_html=True
)

# 7. ऐप खुलते ही स्क्रीन पर गुब्बारे उड़ाना
st.balloons()
