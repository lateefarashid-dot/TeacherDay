import streamlit as st
import random


st.set_page_config(
    page_title="أثركِ | يوم المعلم",
    page_icon="🌷",
    layout="centered"
)

# ---------- CSS ----------

st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Cairo:wght@400;600;700;800&display=swap');

html, body, [class*="css"] {
    font-family: 'Cairo', sans-serif;
}

.stApp {
    background:
        radial-gradient(circle at 10% 10%, rgba(255, 214, 232, .45), transparent 28%),
        radial-gradient(circle at 90% 20%, rgba(210, 232, 255, .45), transparent 28%),
        linear-gradient(135deg, #fff8fb 0%, #f8fbff 100%);
}

.main-title {
    text-align: center;
    font-size: 48px;
    font-weight: 800;
    margin-top: 10px;
    background: linear-gradient(90deg, #b84d7d, #7b6bd6);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
}

.subtitle {
    text-align: center;
    color: #777;
    font-size: 19px;
    margin-bottom: 25px;
}

.card {
    background: rgba(255,255,255,.82);
    border: 1px solid rgba(255,255,255,.95);
    border-radius: 28px;
    padding: 30px;
    box-shadow: 0 12px 35px rgba(90,70,100,.10);
    text-align: center;
    margin: 20px 0;
}

.message {
    font-size: 20px;
    line-height: 2;
    color: #4b4050;
}

.name {
    color: #b84d7d;
    font-weight: 800;
}

.tech-box {
    background: linear-gradient(135deg, #f5edff, #eef8ff);
    border-radius: 22px;
    padding: 20px;
    margin-top: 20px;
    font-size: 18px;
}

.footer {
    text-align: center;
    color: #888;
    margin-top: 35px;
    font-size: 15px;
}

div.stButton > button {
    width: 100%;
    border-radius: 18px;
    height: 3.2em;
    font-family: 'Cairo', sans-serif;
    font-size: 18px;
    font-weight: 700;
    border: none;
    display: flex;
    text-align: center;
    justify-content: center;
    margin: 20px auto;
    
}
</style>
""", unsafe_allow_html=True)

# ---------- Messages ----------
messages = [
    """قد تنتهي الحصة، وينتهي العام الدراسي،
    لكن أثركِ يبقى في ذاكرة طالباتكِ
    شكرًا لأنكِ لم تكوني مجرد معلمة،
   بل كنتِ مصدر إلهام ودعم وأثر جميل""",

    """وراء كل طالبة واثقة من نفسها،
    هناك معلمة آمنت بها يومًا
    شكرًا لأنكِ كنتِ من أولئك الأشخاص
    الذين يصنعون فرقًا دون أن يشعروا""",

    """ربما لا تعرفين كم كلمة قلتِها
    بقيت في ذاكرة طالبة،
    وكم تشجيع منكِ غيّر يومًا كاملًا
    شكرًا لكل أثر جميل تركتِه""",

    """المعلمة لا تزرع المعلومات فقط،
    بل تزرع الثقة والطموح والأمل
    شكرًا لأنكِ تزرعين في طالباتكِ
    شيئًا سيكبر معهن لسنوات"""
]

tech_messages = [
    ("📡 أنتِ مثل شبكة Wi-Fi", "تصلين طالباتكِ بالمعرفة مهما كان السؤال"),
    ("💡 أنتِ مثل فكرة مبتكرة", "تجعلين الأشياء الصعبة تبدو ممكنة"),
    ("💻 أنتِ مثل أفضل برنامج", "دائمًا لديكِ الحل عندما نحتاجه"),
    ("🔐 أنتِ كلمة المرور للنجاح", "تفتحين أبوابًا لم نكن نعرف أنها موجودة")
]

# ---------- Session state ----------
if "show_message" not in st.session_state:
    st.session_state.show_message = False
if "flowers" not in st.session_state:
    st.session_state.flowers = False

# ---------- Header ----------
st.markdown('<div class="main-title">🌷 أثركِ</div>', unsafe_allow_html=True)
st.markdown(
    '<div class="subtitle">💗رسالة صُنعت خصيصًا لكِ بمناسبة يوم المعلم </div>',
    unsafe_allow_html=True
)

# ---------- Input ----------
st.markdown("""
<div class="card">
<h2>✨ أهلاً بكِ يا معلمتنا</h2>
<p style="color:#777;font-size:17px;">
هناك رسالة تقدير بانتظاركِ ..اكتبي اسمك واكتشفيها
</p>
</div>
""", unsafe_allow_html=True)

name = st.text_input(
    "اكتبي اسمكِ",
    placeholder="مثال: نورة",
    label_visibility="collapsed"
)

if st.button("✨ اكتشفي رسالتك"):
    if name.strip():
        st.session_state.show_message = True
        st.session_state.message = random.choice(messages)
        st.session_state.tech = random.choice(tech_messages)
        st.session_state.flowers = True
    else:
        st.warning("🌷 اكتبي اسمكِ أولًا لنجهز رسالتكِ.")

# ---------- Flower effect ----------
if st.session_state.flowers:
    st.markdown("""
    <div class="flower-rain">
        <span>🌷</span><span>🌸</span><span>🌹</span><span>🌺</span>
        <span>🌼</span><span>🌷</span><span>🌸</span><span>💮</span>
        <span>🌹</span><span>🌺</span><span>🌷</span><span>🌸</span>
        <span>🌼</span><span>🌹</span><span>🌷</span><span>🌸</span>
        <span>🌺</span><span>🌷</span><span>🌼</span><span>🌸</span>
    </div>
    <style>
    .flower-rain {
        position: fixed;
        top: 0;
        left: 0;
        width: 100%;
        height: 100vh;
        pointer-events: none;
        z-index: 9999;
        overflow: hidden;
    }
    .flower-rain span {
        position: absolute;
        top: -60px;
        font-size: 28px;
        animation: flowerFall 4s linear forwards;
        opacity: 0;
    }
    .flower-rain span:nth-child(1) { left: 3%;  animation-delay: .0s; }
    .flower-rain span:nth-child(2) { left: 9%;  animation-delay: .3s; }
    .flower-rain span:nth-child(3) { left: 15%; animation-delay: .7s; }
    .flower-rain span:nth-child(4) { left: 22%; animation-delay: .2s; }
    .flower-rain span:nth-child(5) { left: 28%; animation-delay: .9s; }
    .flower-rain span:nth-child(6) { left: 35%; animation-delay: .4s; }
    .flower-rain span:nth-child(7) { left: 42%; animation-delay: .1s; }
    .flower-rain span:nth-child(8) { left: 48%; animation-delay: .8s; }
    .flower-rain span:nth-child(9) { left: 55%; animation-delay: .5s; }
    .flower-rain span:nth-child(10) { left: 61%; animation-delay: .2s; }
    .flower-rain span:nth-child(11) { left: 68%; animation-delay: .7s; }
    .flower-rain span:nth-child(12) { left: 74%; animation-delay: .3s; }
    .flower-rain span:nth-child(13) { left: 80%; animation-delay: .9s; }
    .flower-rain span:nth-child(14) { left: 86%; animation-delay: .4s; }
    .flower-rain span:nth-child(15) { left: 92%; animation-delay: .1s; }
    .flower-rain span:nth-child(16) { left: 97%; animation-delay: .6s; }
    .flower-rain span:nth-child(17) { left: 18%; animation-delay: 1.1s; }
    .flower-rain span:nth-child(18) { left: 58%; animation-delay: 1.0s; }
    .flower-rain span:nth-child(19) { left: 88%; animation-delay: 1.2s; }
    .flower-rain span:nth-child(20) { left: 32%; animation-delay: 1.3s; }

    @keyframes flowerFall {
        0% {
            transform: translateY(-70px) rotate(0deg);
            opacity: 0;
        }
        10% { opacity: 1; }
        100% {
            transform: translateY(110vh) rotate(360deg);
            opacity: 0;
        }
    }
    </style>
    """, unsafe_allow_html=True)
    st.session_state.flowers = False

# ---------- Result ----------
if st.session_state.show_message:
    tech_title, tech_text = st.session_state.tech

    st.markdown(
        f"""
        <div class="card">
            <div style="font-size:45px;">💐</div>
            <h2> إلى الأستاذة الغالية   <span class="name">{name}</span></h2>
            <div class="message">
                {st.session_state.message}
            </div>
<div class="tech_messages">
<strong>{tech_title}</strong><br>
               {tech_text}
</div>
  
  <strong> 🌷كل عام وأنتِ أثرٌ جميل لا يُنسى</strong>
   
      
        """,
        unsafe_allow_html=True
    )



st.markdown(
    '<div class="footer">💻 فريق رواد التقنية | يوم المعلم 2026|أ.لطيفة راشد</div>',
    unsafe_allow_html=True
)

