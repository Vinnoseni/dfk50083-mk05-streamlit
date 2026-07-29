import streamlit as st

# ==========================================================
# PAGE SETTINGS
# ==========================================================
st.set_page_config(
    page_title="My Personal Profile",
    page_icon="👨‍🎓",
    layout="wide"
)

# ==========================================================
# SIDEBAR NAVIGATION
# ==========================================================
with st.sidebar:
    st.title(" Menu")

    page = st.radio(
        "Choose a section:",
        [" My Profile", " BMI Calculator", " My Mood"]
    )

    st.markdown("---")
    st.caption("DIT5E_SWG2")
    st.caption("Built using Python & Streamlit")


# ==========================================================
# PROFILE SECTION
# ==========================================================
if page == " My Profile":

    st.title("👨‍🎓 Welcome to My Profile Website")
    st.header("Personal Profile Using Streamlit")
    st.divider()

    col1, col2 = st.columns([1, 2])

    with col1:
        st.image(
            "vno.jpg",
            width=250,
            caption="My Profile Picture"
        )

    with col2:
        st.subheader("About Me")

        st.write("**Name:** Vinnoseni")
        st.write("**Matric Number:** 18DIT24F1156")
        st.write("**Course:** Diploma in Information Technology")
        st.write("**Class:** DIT5E_SWG2")
        st.write("**Hobby:** Coding, Gaming, Watching Movies")

        st.success(
            "I enjoy learning programming and creating web applications."
        )

    st.divider()

    st.subheader("💻 My Skills")

    skills = {
        "Python": 85,
        "HTML": 80,
        "CSS": 75,
        "Java": 70,
        "Database": 80
    }

    # Changed from st.bar_chart() to avoid Pandas DLL error
    for skill, level in skills.items():
        st.write(f"**{skill}**")
        st.progress(level / 100)


# ==========================================================
# BMI CALCULATOR SECTION
# ==========================================================
elif page == " BMI Calculator":

    st.title(" BMI Calculator")
    st.header("Check Your Body Mass Index")
    st.divider()

    col1, col2 = st.columns(2)

    with col1:
        name = st.text_input("Enter your name")

        weight = st.number_input(
            "Enter your weight (kg)",
            min_value=1.0,
            max_value=200.0,
            value=60.0
        )

    with col2:
        height = st.slider(
            "Enter your height (cm)",
            min_value=100,
            max_value=220,
            value=170
        )


    if st.button("Calculate BMI"):

        height_m = height / 100
        bmi = weight / (height_m ** 2)

        st.success(f"Hello {name}")
        st.success(f"Your BMI is {bmi:.2f}")


        if bmi < 18.5:
            st.warning("Category: Underweight ⚖️")

        elif bmi < 25:
            st.success("Category: Normal Weight ✅")

        elif bmi < 30:
            st.warning("Category: Overweight ⚠️")

        else:
            st.error("Category: Obese 🔴")

    else:
        st.info("Enter your details and click the button to calculate BMI.")


# ==========================================================
# MOOD SECTION
# ==========================================================
elif page == " My Mood":

    st.title(" My Mood Today")
    st.header("How are you feeling today?")
    st.divider()

    username = st.text_input(
        "Enter your name:"
    )

    mood = st.selectbox(
        "Choose your mood:",
        [
            "😀 Happy",
            "😢 Sad",
            "😡 Angry",
            "😴 Sleepy",
            "😎 Excited"
        ]
    )


    if st.button("Submit"):

        if username.strip() == "":
            st.error("Please enter your name first.")

        else:
            st.success(
                f"Hi {username}, your mood today is {mood}"
            )

            messages = {
                "😀 Happy": "Keep smiling and enjoy your day! 🌟",
                "😢 Sad": "Hope your day gets better. Take care 💙",
                "😡 Angry": "Stay calm and relax your mind 🌿",
                "😴 Sleepy": "Remember to get enough rest 🌙",
                "😎 Excited": "Use your energy to achieve your goals 🚀"
            }

            st.info(messages[mood])


# ==========================================================
# FOOTER
# ==========================================================
st.divider()
st.caption("© 2026 - Personal Profile Website built with Streamlit")