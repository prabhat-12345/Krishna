import streamlit as st
import os

# 1. पेज की पूरी प्रीमियम VLVIP सेटिंग (मोबाइल स्क्रीन पर स्क्रॉल बार छिपाने के लिए)
st.set_page_config(page_title="Happy Janmashtami!", page_icon="🪈", layout="centered")

# 2. एडवांस CSS: फुल-स्क्रीन शाही बॉर्डर, गिरती हुई सुनहरी पत्तियाँ और नियॉन लाइट एनीमेशन
custom_css = """
<style>
    /* ऐप का शानदार डार्क और मॉडर्न फेस्टिव बैकग्राउंड */
    .stApp {
        background: linear-gradient(135deg, #090014 0%, #17002e 50%, #26004d 100%) !important;
        color: #ffffff;
        overflow: hidden !important;
        position: relative;
    }
    
    /* मुख्य कंटेनर को मोबाइल स्क्रीन की हाइट में फिट करने के लिए */
    .block-container {
        padding-top: 0.6rem !important;
        padding-bottom: 0rem !important;
        max-width: 450px !important;
        position: relative;
        z-index: 2;
    }

    /* जादू 1: स्क्रीन के चारों तरफ शाही कोनों का बॉर्डर डिज़ाइन (Royal Festive Corner Decoration) */
    .stApp::before {
        content: "";
        position: absolute;
        top: 10px; left: 10px; right: 10px; bottom: 10px;
        border: 2px solid rgba(255, 215, 0, 0.25);
        border-radius: 20px;
        pointer-events: none;
        z-index: 5;
    }
    
    /* कोनों की कोडिंग डिज़ाइन */
    .corner-decor {
        position: absolute;
        width: 40px;
        height: 40px;
        border: 4px solid #FFD700;
        pointer-events: none;
        z-index: 6;
        filter: drop-shadow(0 0 8px #ff6600);
    }
    .top-left { top: 10px; left: 10px; border-right: none; border-bottom: none; border-top-left-radius: 15px; }
    .top-right { top: 10px; right: 10px; border-left: none; border-bottom: none; border-top-right-radius: 15px; }
    .bottom-left { bottom: 10px; left: 10px; border-right: none; border-top: none; border-bottom-left-radius: 15px; }
    .bottom-right { bottom: 10px; right: 10px; border-left: none; border-top: none; border-bottom-right-radius: 15px; }

    /* जादू 2: आसमान से धीरे-धीरे गिरने वाली सुनहरी पत्तियाँ (Premium Falling Gold Leaves Animation) */
    .petals-container {
        position: absolute;
        top: 0; left: 0; width: 100%; height: 100%;
        pointer-events: none;
        z-index: 1;
        overflow: hidden;
    }
    .petal {
        position: absolute;
        background: linear-gradient(135deg, #FFD700, #ffaa00);
        border-radius: 0 100% 0 100%;
        opacity: 0.7;
        animation: fall linear infinite;
        box-shadow: 0 0 5px rgba(255, 215, 0, 0.5);
    }
    /* अलग-अलग पत्तियों की पोजीशन और स्पीड */
    .p1 { left: 10%; width: 10px; height: 16px; animation-duration: 6s; animation-delay: 0s; }
    .p2 { left: 30%; width: 14px; height: 22px; animation-duration: 8s; animation-delay: 1.5s; }
    .p3 { left: 55%; width: 8px; height: 14px; animation-duration: 5s; animation-delay: 0.5s; }
    .p4 { left: 75%; width: 12px; height: 18px; animation-duration: 7s; animation-delay: 2s; }
    .p5 { left: 90%; width: 15px; height: 24px; animation-duration: 9s; animation-delay: 1s; }

    @keyframes fall {
        0% { transform: translateY(-20px) rotate(0deg); opacity: 0; }
        10% { opacity: 0.8; }
        90% { opacity: 0.8; }
        100% { transform: translateY(100vh) rotate(360deg); opacity: 0; }
    }
    
    /* मुख्य हेडिंग जो धीरे-धीरे चमकते हुए अपना रंग बदलेगी (Animated Gradient Text) */
    .main-title {
        font-family: 'Georgia', serif;
        text-align: center;
        font-size: 2.5rem;
        font-weight: bold;
        letter-spacing: 1px;
        margin-top: 15px;
        margin-bottom: 5px;
        background: linear-gradient(to right, #ff007f, #FFD700, #00ffcc, #ff007f);
        background-size: 200% auto;
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        animation: textShine 4s linear infinite, headingGlow 2s ease-in-out infinite alternate;
    }

    /* जिसने भेजा है उसका नाम दिखाने के लिए VIP स्टाइल */
    .sender-box {
        text-align: center;
        margin-bottom: 12px;
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
    
    /* जादू 3: इमेज के चारों तरफ घूमने वाला नियॉन बॉर्डर और बैकग्राउंड पल्स ग्लो */
    .stImage {
        position: relative;
        padding: 5px;
        background: linear-gradient(0deg, #ff007f, #FFD700, #00ffcc, #ff007f);
        background-size: 400% 400%;
        border-radius: 25px;
        animation: borderRotate 6s linear infinite, superFloat 4s ease-in-out infinite;
        box-shadow: 0px 0px 30px rgba(255, 0, 127, 0.6), 0px 0px 15px rgba(255, 215, 0, 0.4) !important;
    }

    .stImage img {
        display: block;
        margin-left: auto;
        margin-right: auto;
        max-height: 265px !important;
        width: auto !important;
        border-radius: 20px !important;
        border: none !important;
        box-shadow: none !important;
    }

    /* नीचे का प्रीमियम शुभकामनाएं बॉक्स जिसके टेक्स्ट अब सोने की लहर की तरह लाइव चमकेंगे */
    .wishes-container {
        background: rgba(9, 0, 20, 0.7);
        border-radius: 15px;
        padding: 12px;
        margin-top: 15px;
        border: 1px solid rgba(255, 215, 0, 0.2);
        box-shadow: 0px 0px 15px rgba(255, 215, 0, 0.15);
        text-align: center;
        backdrop-filter: blur(5px);
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

    /* एनीमेशन टाइमिंग्स */
    @keyframes borderRotate {
        0% { background-position: 0% 50%; }
        50% { background-position: 100% 50%; }
        100% { background-position: 0% 50%; }
    }
    @keyframes textShine {
        0% { background-position: 0% center; }
        100% { background-position: 200% center; }
    }
    @keyframes headingGlow {
        0% { filter: drop-shadow(0 0 5px rgba(255, 0, 127, 0.6)); }
        100% { filter: drop-shadow(0 0 15px rgba(255, 215, 0, 0.8)); }
    }
    @keyframes superFloat {
        0% { transform: translateY(0px); }
        50% { transform: translateY(-10px); }
        100% { transform: translateY(0px); }
    }
</style>
"""
st.markdown(custom_css, unsafe_allow_html=True)

# 3. HTML कोड के जरिए स्क्रीन पर कोनों का डिज़ाइन और सुनहरी पत्तियों का गिरना लाइव करना
html_effects = """
<div class="corner-decor top-left"></div>
<div class="corner-decor top-right"></div>
<div class="corner-decor bottom-left"></div>
<div class="corner-decor bottom-right"></div>

<div class="petals-container">
    <div class="petal p1"></div>
    <div class="petal p2"></div>
    <div class="petal p3"></div>
    <div class="petal p4"></div>
    <div class="petal p5"></div>
</div>
"""
# इसे CSS के साथ जोड़ने के लिए एक खाली डैशबोर्ड हैक
st.components.v1.html(f"<style>{custom_css}</style>{html_effects}", height=0)

# 4. जादुई नाम बदलने वाला कोड (URL Prompt Link)
query_params = st.query_params
sender = query_params.get("name", "")

# 5. एनिमेटेड हेडिंग
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

# 7. आपकी वही असली सुंदर फोटो 'images (52).jpeg' (अब घूमते हुए नियॉन लाइट फ्रेम में बंद है)
image_path = "images (52).jpeg"

if os.path.exists(image_path):
    st.image(image_path, use_container_width=False)
else:
    st.warning("कृपया पेज को एक बार रिफ्रेश करें।")

# 8. नीचे का पूरी तरह से चमकता हुआ एनिमेटेड शुभकामनाएं बॉक्स
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
