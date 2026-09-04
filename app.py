import streamlit as st
import os

# 1. पेज की पूरी प्रीमियम VLVIP सेटिंग (मोबाइल स्क्रीन पर स्क्रॉल बार छिपाने के लिए)
st.set_page_config(page_title="Happy Janmashtami!", page_icon="🪈", layout="centered")

# 2. एडवांस CSS: फुल-स्क्रीन फिटिंग (No Scroll), प्रीमियम नियॉन गोल्ड और क्लासी टेक्स्ट डिजाइन
custom_css = """
<style>
    /* ऐप का प्रीमियम और गहरा रॉयल फेस्टिव बैकग्राउंड - स्क्रॉलिंग पूरी तरह बंद */
    .stApp {
        background: linear-gradient(135deg, #090014 0%, #15002a 50%, #26004d 100%) !important;
        color: #ffffff;
        overflow: hidden !important;
    }
    
    /* मुख्य कंटेनर को मोबाइल स्क्रीन की हाइट में फिट करने के लिए */
    .block-container {
        padding-top: 1rem !important;
        padding-bottom: 0rem !important;
        max-width: 450px !important;
    }
    
    /* मुख्य चमकती हुई हेडिंग */
    .main-title {
        font-family: 'Georgia', serif;
        color: #FFFFFF;
        text-align: center;
        font-size: 2.3rem;
        font-weight: bold;
        text-shadow: 0px 0px 10px #ff007f, 0px 0px 20px #ff007f;
        margin-top: 5px;
        margin-bottom: 2px;
        letter-spacing: 1px;
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
    
    /* इमेज के चारों तरफ का वीआईपी नियॉन ग्लो और 3D फ्लोटिंग - साइज मोबाइल के लिए फिक्स */
    .stImage img {
        display: block;
        margin-left: auto;
        margin-right: auto;
        max-height: 280px !important;
        width: auto !important;
        border-radius: 20px !important;
        box-shadow: 0px 0px 25px #ff007f, 0px 0px 10px #9900ff !important;
        border: 2px solid rgba(255, 0, 127, 0.3) !important;
        animation: superFloat 4s ease-in-out infinite !important;
    }

    /* नीचे का प्रीमियम और बिल्कुल साफ स्टैंडर्ड शुभकामनाएं (Best Wishes) बॉक्स */
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
    }
    
    .wish-highlight {
        color: #FFD700;
        font-weight: bold;
        text-shadow: 0px 0px 5px rgba(255, 215, 0, 0.4);
    }

    /* रिस्पॉन्सिव हाइट मोशन */
    @keyframes superFloat {
        0% { transform: translateY(0px); }
        50% { transform: translateY(-10px); }
        100% { transform: translateY(0px); }
    }
</style>
"""
st.markdown(custom_css, unsafe_allow_html=True)

# 3. जादुई नाम बदलने वाला कोड (URL Prompt Link)
query_params = st.query_params
sender = query_params.get("name", "")

# 4. स्क्रीन पर सबसे ऊपर "Happy Janmashtami" हेडिंग
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

# 6. तुम्हारी वही असली सुंदर फोटो 'images (52).jpeg' (अब बिल्कुल परफेक्ट हाइट में)
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
        <p class="wish-text" style="font-size: 0.95rem; color: #00ffcc; margin-bottom: 0;">May Lord Krishna fill your life with Love, Peace, and Happiness! 🌟</p>
    </div>
    """, 
    unsafe_allow_html=True
)

# 8. ऐप खुलते ही स्क्रीन पर गुब्बारे उड़ाना
st.balloons()
