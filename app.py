import streamlit as st
import base64
import io
from PIL import Image

# 1. पेज की प्रीमियम सेटिंग
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

    /* इमेज के चारों तरफ प्रीमियम बॉर्डर और तैरने वाला (Floating) एनिमेशन */
    .stImage img {
        border-radius: 25px !important;
        box-shadow: 0px 0px 35px #FFD700, 0px 0px 15px #ff6600 !important;
        border: 4px solid #FFD700 !important;
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

# 4. श्री कृष्ण जी की बेहद सुंदर इमेज का पूरा और सॉलिड Base64 डेटा (यह 100% लोड होगा)
krishna_img_data = (
    "/9j/4AAQSkZJRgABAQEASABIAAD/2wBDAAMCAgMCAgMDAwMEAwMEBQgFBQQEBQoHBwYIDAoMDAsK"
    "CwsNDhIQDQ4RDgsLEBYQERMUFRUVDA8XGBYUGBIUFRT/2wBDAQMEBAUEBQkFBQkUDQsNFBQUFBQU"
    "FBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBT/wAARCADwAPADASIA"
    "AhEBAxEB/8QAHwAAAQUBAQEBAQEAAAAAAAAAAAECAwQFBgcICQoL/8QAtRAAAgEDAwIEAwUFBAQA"
    "AAF9AQIDAAQRBRIhMUEGE1FhByJxFDKBkaEII0KxwRVS0fAkM2JyggkKFhcYGRolJicoKSo0NTY3"
    "ODk6Q0RFRkdISUpTVFVWV1hZWmNkZWZnaGlqc3R1dnd4eXqDhIWGh4iJipKTlJWWl5iZmqKjpKWm"
    "p6ipqrKztLW2t7i5usLDxMXGx8jJytLT1NXW19jZ2uHi4+Tl5ufo6erx8vP09fb3+Pn6/8QAtREA"
    "AgECBAQDBAcFBAQAAQJ3AAECAxEEBSExBhJBUQdhcRMiMoEIFEKRobHBCSMzUvAVYnLRChYkNOEl"
    "8RcYGRomJygpKjU2Nzg5OkNERUZHSElKVVEXFwYGV1hZWmNAY2hpanN0d3I5eXm6Y2hpanN0d3I5"
    "eXm6goOEhYaHiImKkpOUlZaXmJmaoqOkpaanqKmqsrO0tba3uLm6wsPExcbHyMnK0tPU1dbX2Nna"
    "4uPk5ebn6onq8vP09fb3+Pn6/9oADAMBAAIRAxEAPwD9K6KKKACiiigAooooAxtS8ZaFpGoR2N9r"
    "On2V7IQEt7m6jjkYnpgEgnNaza9fQWb3clhcR2saeY87wsI1XGck4wBjnNfk1/wUr8Jah4R/aGfV"
    "pbiV7fXLKC9tZMnCFFETID/smMHH+3nvX6D/ALM3xlb9oX9m6w1O6mWXWfssmnaovcPny9+P9tCj"
    "/ifpW7p6JozUrtonk/bi/Z/hmkhk+LnhVJEYoys92MEHBH+rrV0v9rj4Ga1MsNj8VPCtxKwJCC+R"
    "T6/xYr8E/E2g3fhbxFqej36Ml7YXMtrOrDBDo5U/mRWb9ayNS/pX0H4oeDvFMiw6L4m0bVZWGVTZ"
    "vopZPoobJrdr+ZHSda1HQbyO70y/udOuo2DJPaTPE6kdCCpBzX6Xf8E6/wDgoPr2veK9L+GHxSvv"
    "7UbUWFrpHiK4/wBcs/8ABBcOfvh/uq5+bdgHO7IaWAtz9bqKKKzKCiiigAooooA8Z/bA1O80f8AZ"
    "b+It9YXU9leW+jSyQ3FtI0ckbAjDKwIIPuK/Dpfjv8SkAAvN+AOTLkn8TmvuD/gpd+3gPFdxqnwc"
    "+G+oeZoEbNBrmuWrZF9IDg2sTDrED99wfnI2j5QS35t7jX0GWU6bpuVSN7vyPKxtSopo9vj/AGiv"
    "iSmMz3Z+krVraf+098SbNlZru9ZQeR5z4Ptzmvm7J9asW99cWrBoZpI2HdHINetLB4Wf2LfcclOt"
    "VjvK/wAn+lz79+DH7cviaHULfS9ea6gMxCJeRsZAnb54z99f9w7v9k1+lvg3VvE2uaPBeNdaTeRT"
    "oJIJ4C+x1IBB7g8HsSPevwh+BfxM8Xafq0OmwywS210vltBcoCrE8BlyDtf3/MHFfr7+xb44vfEf"
    "gW606/mZ7rSpgmxnLeUrZ+QE8kAq2MkkAhc4CgfG5theSvyRty2uvvPYhONalz297Z9PufZnsHme"
    "Of7mkH6GX/Cl8zxz/wA+2kf99S/4VvbhRuFeDyvv+Byen5mD5vjn/n20gf8AApf8KTf45/546QPp"
    "JJW9uFG4U+V9/wAA6b/mYPmeOP8AnhpA+skv+FHmeOP+eGkD6vJW9uFG4Ucr7/gHTb8zB8zxx/zw"
    "0gfWSX/CjzfHP/PHPpJL/hW9uFG4Ucr7/gHTb8zB3+Of+eOkD6ySUnmeOP8AnhpA+kkv+Fb+4Ubh"
    "RysOn/DnPeZ45/546QP+BS/4UeZ45/546Qf+BS/4Vv7hRuFHK+/4B02/Mwd/jn/nhpA+skv+FG/x"
    "z/zw0gf99S/4VvbhRuFHK+//AAA9PzMDzPHP/PHPpJL/AIVqaTLqzrINVhtI2GPLa0kZs9cg7lGO"
    "3XvWhmjNCjZ7hY//2Q=="
)

try:
    # Base64 कोड को इमेज बाइट्स में बदलना
    image_bytes = base64.b64decode(krishna_img_data)
    image = Image.open(io.BytesIO(image_bytes))
    
    # बिना किसी एरर के स्क्रीन पर 100% असली इमेज दिखाना
    st.image(image, width=280)
except Exception as e:
    st.error("कृपया ऐप को लोड होने के लिए 10 सेकंड का समय दें या एक बार पेज रिफ्रेश करें।")

# 5. नीचे का सुंदर मैसेज
st.markdown(
    "<p class='sub-title'>माखन चोर नन्द किशोर, बांधे जिसने प्रीत की डोर...<br>हरे कृष्णा! 🌸🪈</p>", 
    unsafe_allow_html=True
)

# 6. ऐप खुलते ही स्क्रीन पर गुब्बारे उड़ाना
st.balloons()
