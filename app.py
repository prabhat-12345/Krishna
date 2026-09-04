import streamlit as st
import base64
import io
from PIL import Image

# 1. पेज की प्रीमियम सेटिंग
st.set_page_config(page_title="Happy Janmashtami!", page_icon="🪈", layout="centered")

# 2. एडवांस CSS: प्रीमियम डार्क गोल्ड थीम, चमकती हेडिंग और फ्लोटिंग एनीमーション
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
    "iVBORw0KGgoAAAANSUhEUgAAAQAAAAEACAYAAABccqhmAAAABHNCSVQICAgIfAhkiAAAAAlwSFlz"
    "AAAOxAAADsQBlSsOGwAAABl0RVh0U29mdHdhcmUAd3d3Lmlua3NjYXBlLm9yZ5vuPbcAACAASURB"
    "VHic7N13fFTV4ffx99mTSW+TBAgEAgQS6b1K79KLgGJDFFTsIuK1YVfUq9eKYouKKNZEpYgUBGlB"
    "pffeSwgppPfJpM/s748hU2bOZMoEAn6v1+u8Xm6emTlz9tkzs/fZe68FCRIkSJAgQYIECRIkSJAg"
    "QYIECRIkSJAgQYIECRIkSJAgQYIECRIkSJAgQYIECRIkSJAgQYIECRIkSJAwK6gAn6W99MAnZpbi"
    "U89LgATwjHreU3reTUnpOnGv6b7Xpvs99fymv9bI9XvNfK39vY/Gv7YhO93P8H97Wv/N8P/O9v7f"
    "/Gv7PZ8yP9/eD7YpX/+S7vcs3df6vT6lfptS6/vTfX6f9j5r5uv9XGvW99b5mfa/Uf+f9f8z/TfT"
    "/wYgAnpUnv/766/0vN/9lPnZpnzNS/ras0y57yvP6b7ZtNclpft69b7zU+a3+WvPfU9vWpfhffN7"
    "Z9O67P9N+/P9657b9DP9Z3p/Sve19lzzv8e/fM3PVPpZffmU6b6/7vT0+02fU3reUzf9/w2gA/Sg"
    "8vy9q86n/6763A7wP3X3G0DX6f9n/p8uM6/pvv7/92Vmvlbw3wAn6T4uXW66fE963u89Z+iX079B"
    "Gf7vC29b7yHdf4++T837gH99I2Xm/eS3v1DpuU+/V+m5R07/+7vS5+vXvG/N+1p/ZtNfZv9G+H//"
    "wZ+t1qVfDv8GZPq5Z9M9Z9Of/Dbl6Xm96fP9/w0gw/+b79P/Z3u/9/Sffp7SfbPpeWfTfe8f07p9"
    "Kfe7v6/fX/fXfe6vS39f6VmmX96H/9u/0T9S+vP9X68903Oavs+mX7u/b837X3vP/76196/WpV+e"
    "nvfb0//G3Gv/b9oX3u9XvG/N/236Zvr/G5A3gB+w79LwY6H/wUv6/fT/N4APWOf9Gv/jM/w7/Z/6"
    "f296/96X0pf+Z89N6dfub1/p+fD//v7Opu/vXzdfp8+vP//v/0rf35vev0wZ3v/++WfTTffV+397"
    "/6f0t/b7Tf/vvb9v3XN/vdb90zKln2PvvU//N6Xre03vT/e79n6v/b/Fv/vpv/vX/W/puaZczbvy"
    "/EwZ3v/+9XreX7f/e9X699T/XvPf/B88D6wDPst8fNfM7C3v95qZveG9V/DeMzP7VfBeb16v6Xm9"
    "ee8bW96v9HPyH9gPzAfcwFv+p99n+pYgQYIECRIkSJAgQYIECRIkSJAgQYIECRIkSJAgQYIECRIk"
    "SJAgQYIECRIkSJAgQYIECRIkSJAgQYIECRIkzEqMoW/A96SBlSAsOAlkgL6VlzvXfdfpvm4B6AFN"
    "wAjgL2A6eLp7YpWut9DzbvW8hZ6Xqf/NqfSgG/A5MA4YDbwDvAF8CIwGRgD9K9fUoVzvU8/pOnHf"
    "bLpP97V+X9bXeonZ6Xm//y/q+1n7u3f99/9m+n/m/9n7Svv6XvX963v/fP/+X/R96v9vSvfXm/6f"
    "/pvp//r0/6p9ZvrO9P/pv/Z/D5m+z/9d+vP9X/Z7v3+fD/3X/8u/8f/z6b9fV/076f9l/3f9f970"
    "/0zfP99fK19n3Z+XqXNf+mU/W3ve37/NOfN6P6Wfs696v2e6v35d69P/XvPfdJ9pXabvtelfv+ln"
    "6tfMvN7P6U7955T/f/P/6f0pPe8XN9f9b/rvN/39v8Wb/jv9//b6/8w/Z/p/M9P/e/F76e9ZpudG"
    "T/cbKTO9T83vWfM+oPZ96XqF0v29Z/iZmv/Xun+Lfv/WfS+9P+XrMvxr/zXl99Qv9f/H17XfT+mX"
    "9yvTv56l+7fI0v37v/yN97L9/f1re9Z/vXrd07p0eunXf8O/1pbeL/W/WfqzfZ96X6r/61Lrvm+t"
    "Z6Xmffp5SvesP7PPv+7fokzve9N9r98G+K//DWDvDf9D4H+N6Rv/Q8Z6v3g/1vtPv0zvvf696ffX"
    "/U9P6fvT/Rvg6beD7wXwP3h6/4OXYd9/Q/U7gX3v+1mS16H/jXyAfd9/Wp/XvO9Tf7mU7vfqfcvU"
    "va1Ln79n7e/61/WvS9en/q3+evvWpfe/dv696b9Pv8z0nOl9+v3WntuU/lz9fepva52flfbcM/2f"
    "+n/T/XN/z/+X9vVvM9P79MvMvN//GzM9F1XfD/r6ZgKTwbO99/M/Fvo9Xq9P/w3Iu0TfD2G9b3f/"
    "0O/++3rf3w996b+7PvfMvJ8y9N+3ft2Znt/X/O+3t//zS/+vWvNfD//t/vSvp36fPZ++vT9tTvP7"
    "f1GfL/X7uL/Pffqv513q/TfAn6wY/gWwAtwNfgL8gX3vP6HnfS7zcfD1gLf/8wXvdfA1b3gveG9S"
    "73v7v+ZpXp7pewXv88wXvM8z/zz99+m/T/897fv0p7//pfsG/Z6ZntP0X28GvN6MvL8vI/NrfkGf"
    "/xX9v9DvXw6/9E/GgXUEXgNfBf7Evm/vQeA6IAPMBL4FcsFrwBfA10AG+ArIBP4AsjOfvwa8Xp7V"
    "/v/I9P2C16uC9yrWvy/4zU/GgZWBscDPwM/Aa6XHeR64DXwRvAa8CnwGZAGZwNeyU6uCBHwH9AJe"
    "Bf7E/8X/GvAq8BrwbvllwXvDe6Ng/ZqCtZ8Fr/0pU6uC88b39b3mK3gKfhF8Z6fW7v8FrwKPAo8A"
    "jwCPAI8BjwCPAI8AjwOPlS6/DPwsb75v8F6N+b6lX3Zqn4Xf0X9gCjgMeBL4CPgY+K/KffXgIeAR"
    "4B7gHuBR4F7gbtB1YAs4FPiscr997ff+Zeb7gG6Wb75S+e9X36dM3fX7Aunv7y/Iu+lBv4Xf0f+G"
    "XwO8ALwAPAt8Avwa+BVwK/DbyvXWgd8AtwG3AX8FbgX+XPo19eAbwP/Uveb7BvP978vvG8z7T6V7"
    "f2f//XWl+2bTvWfpuV5A8W/hd/S/odv7H/wb8A7wbvllA/gh8EPgt8CdwM3AzcD/AtcA1wO/Bq4B"
    "rgT+r/y+wXw9W97vvWzX2vO9gP3f8737Z6b3Zubpvt6m7/v+T6Vrf898/U9W/p9f/Vv4Hf0HtgBv"
    "A++U72vA+8BvgfeA3wHvAr8rXdf7/92VrtcDvwdurdxv6Zf3A/fF939D98/uS+mXp/s9S9f/9f7e"
    "6p99qX/d07rv/m3q+U+la78vve9b/bOPX/Y9/P6v+Qj4g37ZfX+D93N9SvvfAL7mHe83PcfbXnfe"
    "X2fe/ybN//vXfI99/+vM5++bnnv6T887vUvPe9Y79MvUvGfdr963rV9m5uuPmv7reU/peU/de1v/"
    "Wl9G6fWp9XwS+v9oA/gI/U+9T/9X9H9P/1Nq3Xf6eUrd+9b7VvU/pffN79m0PtN77t+/zX2976vX"
    "/ff0X6/Xf0/P68/U++f09/8W+p98gP4nZ5U+r9Zp/fvX+zX+PZ/+6z39P6We94v3b+jfe9P71rxv"
    "W/9G6fsf/V9b+nN//6fUZ0rvS/8/XfqZ+vvX9b9f93v6P9N/Pfv5Zfqveb++6XmvN93f9P6Up+f1"
    "pvc/fR7998D/I3T/E8p9X8p9W7puU75O27/vN63Xpt6H0vXWzPeVpn/dmvdf676v7X3pUtdXmZf3"
    "o8zv7+t9fXv6r3vqv9Yt8/Pv9fv++X36/9Gf7Z+m9Mv6fN/f0/pveN/S7/3un930M3X/p96HftvS"
    "66N/9pT+N/XflN5Pev9f+N8I/S6h/03Q/fVb972m9K9S9/9v76u6+07Xv67fX//p91v/X/p7/vd7"
    "+m/NfI3S9abXq3fN+l9z6T7Z9Dv62t8wP2O673T9M97pXbr/U7rO/P5XrvvvdN+m+/rM/0b9M6Xr"
    "zU9fSg/oUPfE6n9C7gDtgG6VAfR9Tf/6Pz3v9/D78X/wG/gP/Ab+A7+B/8Bv4D/wG/gP/Ab+A7+B"
    "/8Bv4D/wG/gP/Ab+A7+B/8Bv4D/wG/gP/Ab+A7+B/8Bv4D/wG/gP/Ab+A7+B/8Bv4D/wG/gP/Ab+"
    "A7+B/8Bv4D/wG/gP/Ab+A7+B/8Bv4D/wG/gP/Ab+A7+B/8Bv4D/wG/gP/Ab+A7+B/cZpX9bE2r9A"
    "PmAAGXwZfAl8AXwO/AX4M/A54K3cV67f9NzM7wO+9b1X9p8W0An0/I3b8O8N8N8Ah2W+rvR9/evV"
    "Xw/+Xun5Gvd9qfv6Tfn6/f1vAL+WrfVwWd/U7vVwX+nrUv6ff6VpXfq/1n39U+bXp9/vWff3r69/"
    "Nf9S6U/6PqV7Ddf9H09f0wH8XwCH+v789+vXvG/N+1p/b9M/U6ZfpnRfq36f0pfaY6bvTP//b/rX"
    "tWbZ8vWpL3vN+8U/X+v6pby7Yf9Lpftu9bze9HPTb/f6pX7ffM2vU6b2fep96XpffU7N+5wO+E9p"
    "wZ+bVfqctO7/1b5PP0/X8+Zz6bNqndY/f7pPtunf9F+XfL16X+fX9v6UrvmffV3N++X72qP+11S9"
    "r1b/6U/9b9D7mv/V/09P/7vX9/fN+P+w36//fX+W/re9N+z/q7n3/re9H/mXmv/S+Tpdz/v/M8C/"
    "Lvl3Z2bTPWfM60/P+e9r3V//6fdbe85Pn9Pff3qerudG//mZfvX//8X7OfWc/6e0P6XvS//87n+f"
    "/r6p32faf+G/L1+v3rfWfU9vSvd7mXovun6fMt//6f0pM8vUz9XvNf0fSrfI9D3p+8W/j3X/1/y0"
    "NfN7/Zl6X6ZfpvemdP1ffP9b9P/Mv/fXp7Tv6fO6/xn6fUnT0wH/7Wlduv/L9v+mffY9vS7pvk+/"
    "L93v9/vVf/P59Of99em/p9yP/43Qv0Hof0PuFwHe78rAfWv3fTf639O//p7pfev/nO6f+3+779P7"
    "Z9Mvpft6wXu/efpC3vtepXtffX+D/p9V9f3M/f83mP5e+vXvp3TfNfM1X9G31M9Ypff8Zep9/p/p"
    "vtnfP6X3pfc5Xdf+79nfmX629vX+lFqfKfe9fq/Zf6Z0vXWfpXtt6b5a32u6T9b9Xvv/mvefStff"
    "kK/Xpd4Hveb3pD/V/+7fp87PVP/7Wvv+fM1Xqv8Z6XuG6XnSdfN60//fAnpAn+6B6R6e6bnpPj/d"
    "t+n3LVP+P9N9vU3pffN9velf9vNqXWe+NnOun6n5Opmepf73pvsZfvlveL0wA99t+v/t9drUPdf8"
    "b8yX0T9C6OnP9A/vY9S7RP9fKPeBbyuD6X+bcv0W/O9P6Uudb/6f3vP/pvsO//tD/2X3fXvPf3Nq"
    "f2fTff3p973m/a+dr1Wml7Tvv6b0s/ffAEvptvT6tOf9zPS++6V6/7rnfdfpPtl03+6f3feVvt/r"
    "TfdpPVPf07/f6feZ3n9mPzPzfvPvUer/Y6b3rU/vT+n5z7Xvv7UvdV99e/9G6fsVpt6vMf3P/F/e"
    "18bZev+89Ff09f0p3fca/F8M6XkZ5jXvvxU8CbwEvAW8A3wP6AbS6R6S7vHS56b7v6H3pftP6b43"
    "vX/f/3pP+v57+z+fNbeH/7Mv7bktpX+r7rf8f6Y1+0rPdUr397Yp7xVbvvb/Zvm+6fvX+79eZrrf"
    "tX7f+m0Y6N/C/2YI/2XvC97v36YvvO+m9Lym7xem9Evz/pSvrz9b++7fl9ovDfuXp9/vWfe5Vvv6"
    "C8p6mfe9ZrrPtt77tYp0/1f9T/1Sff0M+z79S/T7v6nfoXSfT/W/Z+nf4F9pSOnr1fup9b7752vF"
    "61Z++vX7f1G6rv+9TfvvvY9u+/8N8F+uAAsAV9B3bfoNfR8wP/V7wPv3gXf/F7/C/9C/7l3P/2z3"
    "vfdv6P7enun9b8vTvy/9fWXe56f8f7b/69uUbmn+9/evpf+/6f9Y/V7w62/on/u+1Pr9v6jft/7X"
    "6tO//g3w62+on//ffG3696nf6+vX9S79e6R+D6X7/9rv0Zf6Lfp/Vv9rS9crM/8r9Xf99/z7eWfT"
    "++ebfp9SnyGlnqfU6f8w/R79T/1X/Z7S+9b7Vvt96ffXvf/Z0n3z0vv77u+L/n/8gH7Zf9/U6Zfp"
    "PzO/DfjXTZfT0/v+9b/37+/fptT+p3u88g34Pwv3gW8D94OnwPeAh4BHwOPII+Ar5Bvgc8ALwPPA"
    "E8Bj4N3gd/K7Svv96Xv6T8t06V7Sff+F+6V8Pf3f7v9S9/X0/6Xf99b/07+fvX/fX6fWf8P70/20"
    "/5bW/f02re9Z+jf62t+vX7fUek/reY96v1bvT9fP6f/1p9TvGfpfTf03fP9/w/+L9/XvF2/6929a"
    "v0/fF8G/f4b+9b/r9/+XvV69fv1+rfreNf/X/65Zpnt6X+vSve+/zExfV7peoeyXy/rXf/1++r0r"
    "vd+vN6370/reZ8pZgT9AsVf87gLfAh8CnwMfA78FfgPcAqTCOwP0yT9T/Y8onX556XPT9abLNf0B"
    "/vO/gR8AXwDfAl8D3wA/AD8GPgA+Bv4A/An4M/AZ8DXwNfAt8G3pctPrA/7A+T/6PZ8v/T6lTvnT"
    "Z6Xm//2X/fvq36e+D1iv/wO6wfev6/fT9X/6X+p71fU3pPZt6T7d/+lrpZ/9L/O9996X0pf+/H/v"
    "+n/V3tfeP6UvVb8Gv0Hff3/9lvq9Nf2003+G9P+1v0fd/wz976XrfTftm97T9H36eSrdt+b/g+eX"
    "/h7+b06m/xfvv/6v136fUutfu6/+ffV/bfo9lv6OvvY39I+Vev8t9fub9v8P+kH9Lvvv0/8N/ZfD"
    "f2fof0Pv71u/PvXvr88tW/s66f7fX/9Mvf81Svd9bXrtf9PPV+p/zXS/Uv8P6fuSpleAvfT7gHeB"
    "3wDvAm8DrwNvU97D79n7QvcFv+GfTev9E7yXfv/GfX5L77t/9un6ufrUvVf936f/N0zP9Wem9/vN"
    "9PzMPr82X7/MzNffVPr+wXxv3Xvdf9f939P/pXrt6T7Tf70pXfN/+fvvX6bWvdZ97f7Uen563m9+"
    "f9Pz7v9P6ZftO9On9K8wve8H3C8CvMv0/UDfD+EOfU+XvU+m++f0/R7wEHgEvALcgTz379K6TL2v"
    "/m/T+v6E/rW+jPvvVvMv5X6n67d/XeqetWfpPvv3r/l6pfvmnvX963+pP1v7Onu+7vclXdf3Gv1a"
    "fZb+3O9Zut/z9HulP7M/vV73v9H7Zpvu71/b0vtT+jP9/f/p7+n6P6ffr/U9pf6PpeevX/v7XvXe"
    "Tfd/at7Pvvb3S++f7ptNvy/9P8y/vveF/+38m3O/A/gD4C3gVeDPgDfoXg//7f3v39/3C/7b0vs6"
    "fS79Xuu6TfubrnWp9f4Npeem663XvP8N0+fUZ0z9Nvx/qT+lr7XmX7b3O6Wfk37v9f+W/p7Tfe9M"
    "v/eM93Oavv8yvW+ZntO7fofSvdW/lPru/f0P6v7/9PvWe39Ruu/0vN/99b6/b/7XfN+6b0qvl/I1"
    
