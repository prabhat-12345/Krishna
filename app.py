import streamlit as st
import os

# 1. पेज की पूरी प्रीमियम VLVIP सेटिंग (मोबाइल स्क्रीन पर स्क्रॉल बार छिपाने के लिए)
st.set_page_config(page_title="Happy Janmashtami!", page_icon="🪈", layout="centered")

# 2. एडवांस CSS: घूमता बॉर्डर, चमकता टेक्स्ट और लाइव तैरते हुए सितारे (Stars Particles)
custom_css = """
<style>
    /* ऐप का शानदार डार्क और मॉडर्न फेस्टिव बैकग्राउंड */
    .stApp {
        background: linear-gradient(135deg, #090014 0%, #15002a 50%, #26004d 100%) !important;
        color: #ffffff;
        overflow: hidden !important;
        position: relative;
    }
    
    /* मुख्य कंटेनर को मोबाइल स्क्रीन की हाइट में फिट करने के लिए */
    .block-container {
        padding-top: 0.8rem !important;
        padding-bottom: 0rem !important;
        max-width: 450px !important;
        position: relative;
        z-index: 10;
    }
    
    /* जादू: लाइव स्क्रीन पर धीरे-धीरे तैरने वाले सितारे (Pure CSS Floating Stars Particles) */
    .stars-particle-container {
        position: absolute;
        top: 0; left: 0; width: 100%; height: 100%;
        pointer-events: none;
        z-index: 1;
        overflow: hidden;
    }
    .particle-star {
        position: absolute;
        background: radial-gradient(circle, #FFD700 20%, transparent 70%);
        border-radius: 50%;
        opacity: 0.6;
        animation: floatUp linear infinite;
        box-shadow: 0 0 10px #FFD700, 0 0 20px #ff6600;
    }
    /* अलग-अलग तारों की पोजीशन, साइज और तैरने की स्पीड */
    .s1 { left: 15%; top: 90%; width: 4px; height: 4px; animation-duration: 7s; }
    .s2 { left: 40%; top: 85%; width: 6px; height: 6px; animation-duration: 9s; animation-delay: 2s; }
    .s3 { left: 70%; top: 95%; width: 5px; height: 5px; animation-duration: 6s; animation-delay: 1s; }
    .s4 { left: 85%; top: 80%; width: 7px; height: 7px; animation-duration: 10s; animation-delay: 3s; }
    .s5 { left: 25%; top: 75%; width: 5px; height: 5px; animation-duration: 8s; animation-delay: 0.5s; }
    .s6 { left: 60%; top: 88%; width: 4px; height: 4px; animation-duration: 7s; animation-delay: 1.5s; }

    @keyframes floatUp {
        0% { transform: translateY(100px) scale(0.5); opacity: 0; }
        30% { opacity: 0.8; }
        90% { opacity: 0.8; }
        100% { transform: translateY(-100vh) scale(1.2); opacity: 0; }
    }
    
    /* मुख्य हेडिंग जो धीरे-धीरे चमकते हुए अपना रंग बदलेगी */
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
    
    @keyframes textShine {
        0% { background-position: 0% center; }
        100% { background-position: 200% center; }
    }
    
    @keyframes headingGlow {
        0% { filter: drop-shadow(0 0 5px rgba(255, 0, 127, 0.6)); }
        100% { filter: drop-shadow(0 0 15px rgba(255, 215, 0, 0.8)); }
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
    
    /* जादुई फ्रेम: फोटो के चारों तरफ घूमने वाला नियॉन बॉर्डर और बैकग्राउंड पल्स ग्लो */
    .stImage {
        position: relative;
        padding: 6px;
        background: linear-gradient(0deg, #ff007f, #FFD700, #00ffcc, #ff007f);
        background-size: 400% 400%;
        border-radius: 25px;
        animation: borderRotate 6s linear infinite, superFloat 4s ease-in-out infinite;
        box-shadow: 0px 0px 35px rgba(255, 0, 127, 0.6), 0px 0px 15px rgba(255, 215, 0, 0.4) !important;
    }

    .stImage img {
        display: block;
        margin-left: auto;
        margin-right: auto;
        max-height: 275px !important;
        width: auto !important;
        border-radius: 20px !important;
        border: none !important;
        box-shadow: none !important;
    }

    /* नीचे का प्रीमियम शुभकामनाएं बॉक्स जिसके टेक्स्ट अब सोने की लहर की तरह लाइव चमकेंगे */
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

    @keyframes borderRotate {
        0% { background-position: 0% 50%; }
        50% { background-position: 100% 50%; }
        100% { background-position: 0% 50%; }
    }

    @keyframes superFloat {
        0% { transform: translateY(0px); }
        50% { transform: translateY(-12px); }
        100% { transform: translateY(0px); }
    }
</style>
"""
st.markdown(custom_css, unsafe_allow_html=True)

# 3. लाइव तैरने वाले सुनहरे तारों (Stars Particles) का ढांचा
st.markdown(
    """
    <div class="stars-particle-container">
        <div class="particle-star s1"></div>
        <div class="particle-star s2"></div>
        <div class="particle-star s3"></div>
        <div class="particle-star s4"></div>
        <div class="particle-star s5"></div>
        <div class="particle-star s6"></div>
    </div>
    """,
    unsafe_allow_html=True
)

# 4. जादुई नाम बदलने वाला कोड (URL Prompt Link)
query_params = st.query_params
sender = query_params.get("name", "")

# 5. स्क्रीन पर सबसे ऊपर "Happy Janmashtami" हेडिंग
st.markdown("<h1 class='main-title'>✨ Happy Janmashtami ✨</h1>", unsafe_allow_html=True)

# 6. अगर किसी ने अपना नाम लिंक में भेजा है तो वह यहाँ चमकेगा
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

# 7. आपकी वही असली सुंदर फोटो 'images (52).jpeg'
image_path = "images (52).jpeg"

if os.path.exists(image_path):
    st.image(image_path, use_container_width=False)
else:
    st.warning("कृपया पेज को एक बार रिफ्रेश करें।")

# 8. नीचे का पूरी तरह से शुभकामनाएं बॉक्स
st.markdown(
    """
    <div class="wishes-container">
        <p class="wish-text">🌸 माखन चोर नन्द किशोर, बांधे जिसने प्रीत की डोर... <span class="wish-highlight">हरे कृष्णा! 🪈</span></p>
        <p class="wish-text">✨ श्री कृष्ण के कदम आपके घर आएं, आप खुशियों के दीप जलाएं! <span class="wish-highlight">शुभ जन्माष्टमी 🦚</span></p>
        <p class="wish-text" style="font-size: 0.95rem; color: #00ffcc; margin-bottom: 0;">May Lord Krishna fill your life with Love, Peace, and Happiness! 🌟</p>
    </div>
    """, 
    unsafe_allow_html=True
)
