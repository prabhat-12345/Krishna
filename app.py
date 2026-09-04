import streamlit as st
import os

# 1. पेज की पूरी प्रीमियम VLVIP सेटिंग (मोबाइल स्क्रीन पर स्क्रॉल बार छिपाने के लिए)
st.set_page_config(page_title="Happy Janmashtami!", page_icon="🪈", layout="centered")

# 2. एडवांस CSS: झिलमिलाते तारे (Stars) इफेक्ट, लाइव चमकता हुआ एनीमेशन और प्रीमियम टेक्स्ट डिज़ाइन
custom_css = """
<style>
    /* ऐप का प्रीमियम और गहरा रॉयल फेस्टिव बैकग्राउंड - स्क्रॉलिंग पूरी तरह बंद */
    .stApp {
        background: linear-gradient(135deg, #05000a 0%, #110022 50%, #1a0033 100%) !important;
        color: #ffffff;
        overflow: hidden !important;
        position: relative;
    }
    
    /* लाइव झिलमिलाते तारों (Stars) का बैकग्राउंड इफेक्ट जोड़ने के लिए */
    .stApp::before {
        content: "";
        position: absolute;
        top: 0; left: 0; width: 100%; height: 100%;
        background-image: 
            radial-gradient(white, rgba(255,255,255,.2) 2px, transparent 40px),
            radial-gradient(white, rgba(255,255,255,.15) 1px, transparent 30px),
            radial-gradient(white, rgba(255,255,255,.1) 2px, transparent 40px);
        background-size: 550px 550px, 350px 350px, 250px 250px;
        background-position: 0 0, 40px 60px, 130px 270px;
        animation: starTwinkle 10s linear infinite;
        opacity: 0.6;
        z-index: 0;
    }
    
    @keyframes starTwinkle {
        from { transform: translateY(0); }
        to { transform: translateY(-550px); }
    }
    
    /* मुख्य कंटेनर को मोबाइल स्क्रीन की हाइट में फिट करने के लिए */
    .block-container {
        padding-top: 1rem !important;
        padding-bottom: 0rem !important;
        max-width: 450px !important;
        position: relative;
        z-index: 1;
    }
    
    /* मुख्य चमकती और धीरे-धीरे रंग बदलने वाली एनिमेटेड हेडिंग */
    .main-title {
        font-family: 'Georgia', serif;
        text-align: center;
        font-size: 2.3rem;
        font-weight: bold;
        letter-spacing: 1px;
        margin-top: 5px;
        margin-bottom: 2px;
        animation: neonGlow 3s ease-in-out infinite alternate;
    }
    
    @keyframes neonGlow {
        0% {
            color: #ffffff;
            text-shadow: 0 0 10px #ff007f, 0 0 20px #ff007f, 0 0 30px #9900ff;
        }
        100% {
            color: #FFD700;
            text-shadow: 0 0 15px #ff6600, 0 0 25px #ff6600, 0 0 40px #ff007f;
        }
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
    
    /* इमेज के चारों तरफ का वीआईपी नियॉन ग्लो और 3D फ्लोटिंग */
    .stImage img {
        display: block;
        margin-left: auto;
        margin-right: auto;
        max-height: 280px !important;
        width: auto !important;
        border-radius: 20px !important;
        box-shadow: 0px 0px 30px #ff007f, 0px 0px 15px #9900ff !important;
        border: 2px solid rgba(255, 0, 127, 0.4) !important;
        animation: superFloat 4s ease-in-out infinite !important;
    }

    /* नीचे का प्रीमियम और बिल्कुल साफ स्टैंडर्ड शुभकामनाएं (Best Wishes) बॉक्स */
    .wishes-container {
        background: rgba(18, 0, 36, 0.6);
        border-radius: 15px;
        padding: 12px;
        margin-top: 15px;
        border: 1px solid rgba(255, 0, 127, 0.25);
        box-shadow: 0px 0px 20px rgba(255, 0, 127, 0.2);
        text-align: center;
        backdrop-filter: blur(5px);
    }

    .wish-text {
        font-family: 'Georgia', serif;
        color: #ffffff;
        font-size: 1.05rem;
        line-height: 1.6;
        margin-bottom: 8px;
    }
    
    .wish-highlight {
        color: #FFD700;
        font-weight: bold;
        text-shadow: 0px 0px 5px rgba(255, 215, 0, 0.6);
    }

    /* रिस्पॉन्सिव हाइट मोशन */
    @keyframes superFloat {
        0% { transform: translateY(0px) scale(1); }
        50% { transform: translateY(-12px) scale(1.01); }
        100% { transform: translateY(0px) scale(1); }
    }
</style>
"""
st.markdown(custom_css, unsafe_allow_html=True)

# 3. जादुई नाम बदलने वाला कोड (URL Prompt Link)
query_params = st.query_params
sender = query_params.get("name", "")

# 4. स्क्रीन पर सबसे ऊपर "Happy Janmashtami" हेडिंग (अब एनिमेटेड है)
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

# 6. तुम्हारी वही असली सुंदर फोटो 'images (52).jpeg'
image_path = "images (52).jpeg"

if os.path.exists(image_path):
    st.image(image_path, use_container_width=False)
else:
    st.warning("कृपया पेज को एक बार रिफ्रेश करें।")

# 7. नीचे का बिल्कुल नया, स्टैंडर्ड और प्रीमियम शुभकामनाएं (Best Wishes) बॉक्स
st.markdown(
    """
    <div class="wishes-container">
        <p class="wish-text">🌸 माखन चोर नन्द किशोर, बांधे जिसने प्रीत की डोर... <span class="wish-highlight">हरे कृष्णा! 🪈</span></p>
        <p class="wish-text">✨ श्री कृष्ण के कदम आपके घर आएं, आप खुशियों के दीप जलाएं! <span class="wish-highlight">शुभ जन्माष्टमी 🦚</span></p>
        <p class="wish-text" style="font-size: 0.95rem; color: #00ffcc; margin-bottom: 0; text-shadow: 0 0 5px #00ffcc;">May Lord Krishna fill your life with Love, Peace, and Happiness! 🌟</p>
    </div>
    """, 
    unsafe_allow_html=True
)

# 8. ऐप खुलते ही स्क्रीन पर गुब्बारे उड़ाना
st.balloons()
