import streamlit as st
import random

st.set_page_config(
    page_title="أثركِ | يوم المعلم",
    page_icon="🌷",
    layout="centered",
    initial_sidebar_state="collapsed"
)

messages = [
    """قد تنتهي الحصة، وينتهي العام الدراسي،
لكن أثركِ يبقى في ذاكرة طالباتكِ.

شكرًا لأنكِ لم تكوني مجرد معلمة،
بل كنتِ مصدر إلهام ودعم وأثر جميل.""",

    """وراء كل طالبة واثقة من نفسها،
هناك معلمة آمنت بها يومًا.

شكرًا لأنكِ كنتِ من أولئك الأشخاص
الذين يصنعون فرقًا دون أن يشعروا.""",

    """ربما لا تعرفين كم كلمة قلتِها
بقيت في ذاكرة طالبة،
وكم تشجيع منكِ غيّر يومًا كاملًا.

شكرًا لكل أثر جميل تركتِه.""",

    """المعلمة لا تزرع المعلومات فقط،
بل تزرع الثقة والطموح والأمل.

شكرًا لأنكِ تزرعين في طالباتكِ
شيئًا سيكبر معهن لسنوات."""
]

tech_messages = [
    ("📡 أنتِ مثل شبكة Wi-Fi", "تصلين طالباتكِ بالمعرفة مهما كان السؤال."),
    ("💡 أنتِ مثل فكرة مبتكرة", "تجعلين الأشياء الصعبة تبدو ممكنة."),
    ("💻 أنتِ مثل أفضل برنامج", "دائمًا لديكِ الحل عندما نحتاجه."),
    ("🔐 أنتِ مفتاح النجاح", "تفتحين أبوابًا لم نكن نعرف أنها موجودة.")
]

flowers = ["🌷", "🌸", "🌹", "🌺", "🌼", "💐"]

if "show_message" not in st.session_state:
    st.session_state.show_message = False

if "message" not in st.session_state:
    st.session_state.message = ""

if "tech_title" not in st.session_state:
    st.session_state.tech_title = ""

if "tech_text" not in st.session_state:
    st.session_state.tech_text = ""

if "gift_opened" not in st.session_state:
    st.session_state.gift_opened = False

st.title("🌷 أثركِ")
st.caption("رسالة صُنعت خصيصًا لكِ بمناسبة يوم المعلم")

st.divider()

st.subheader("✨ أهلاً بكِ يا معلمتنا")
st.write("هناك رسالة تقدير بانتظاركِ… اكتبي اسمكِ واكتشفيها.")

name = st.text_input(
    "اسم المعلمة",
    placeholder="مثال: نورة",
    max_chars=30
)

if st.button(
    "✨ اكتشفي رسالتكِ",
    use_container_width=True,
    type="primary"
):
    if name.strip():
        st.session_state.show_message = True
        st.session_state.gift_opened = False
        st.session_state.message = random.choice(messages)

        tech_title, tech_text = random.choice(tech_messages)
        st.session_state.tech_title = tech_title
        st.session_state.tech_text = tech_text

        flower_line = " ".join(
            random.choice(flowers) for _ in range(9)
        )
        st.success(f"{flower_line}\n\n✨ رسالتكِ جاهزة!")
    else:
        st.warning("🌷 اكتبي اسمكِ أولًا.")

if st.session_state.show_message:
    st.divider()

    st.success(
        f"💐 معلمتي {name.strip()}،\n\n"
        f"{st.session_state.message}"
    )

    st.info(
        f"{st.session_state.tech_title}\n\n"
        f"{st.session_state.tech_text}"
    )

    st.markdown("### 🤍 كل عام وأنتِ أثرٌ لا يُنسى")

    if not st.session_state.gift_opened:
        if st.button("🎁 اكتشفي هديتكِ", use_container_width=True):
            st.session_state.gift_opened = True
            st.rerun()
    else:
        st.success(
            "💌 هديتكِ اليوم:\n\n"
            "كلمة شكر صادقة من كل طالبة تعلمت منكِ شيئًا جميلًا."
        )

        flower_line = " ".join(
            random.choice(flowers) for _ in range(15)
        )
        st.write(f"### {flower_line}")

st.divider()

st.caption(
    "💻 فريق رواد التقنية\n\n"
    "صُمم بحب بمناسبة يوم المعلم 2026 🌷"
)

