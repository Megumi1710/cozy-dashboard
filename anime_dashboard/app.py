import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import os
import random
import json
from datetime import datetime

# =====================================================
# PAGE CONFIG
# =====================================================

st.set_page_config(
    page_title="🌸 Cozy Anime Dashboard",
    page_icon="🌸",
    layout="wide"
)

# =====================================================
# ANIME AESTHETIC CSS
# =====================================================

page_style = """
<style>

/* Main Background */

[data-testid="stAppViewContainer"]{
background-image: url("https://images.unsplash.com/photo-1519125323398-675f0ddb6308?q=80&w=1920");
background-size: cover;
background-position: center;
background-repeat: no-repeat;
background-attachment: fixed;
}

/* Transparent Header */

[data-testid="stHeader"]{
background: rgba(0,0,0,0);
}

/* Sidebar */

[data-testid="stSidebar"]{
background: rgba(255,255,255,0.12);
backdrop-filter: blur(12px);
}

/* Text */

h1,h2,h3,h4,p,label,div{
color: white;
}

/* Buttons */

.stButton>button{
background: linear-gradient(to right,#ff9ecf,#cfa7ff);
color: white;
border: none;
border-radius: 20px;
padding: 10px 25px;
font-size: 16px;
transition: 0.3s;
}

.stButton>button:hover{
transform: scale(1.05);
box-shadow: 0px 0px 15px pink;
}

/* Input Boxes */

.stTextInput>div>div>input{
background-color: rgba(255,255,255,0.2);
color: white;
border-radius: 15px;
}

/* Cute Container */

.cute-box{
background: rgba(255,255,255,0.15);
padding: 20px;
border-radius: 20px;
backdrop-filter: blur(8px);
box-shadow: 0px 0px 15px rgba(255,255,255,0.3);
}

/* Floating Animation */

@keyframes float {
0% {transform: translateY(0px);}
50% {transform: translateY(-10px);}
100% {transform: translateY(0px);}
}

.float{
animation: float 3s ease-in-out infinite;
}

</style>
"""

st.markdown(page_style, unsafe_allow_html=True)

# =====================================================
# LOFI MUSIC
# =====================================================

st.markdown(
    """
    <audio autoplay loop controls>
    <source src="https://cdn.pixabay.com/download/audio/2022/03/15/audio_c8c8a73467.mp3?filename=lofi-study-112191.mp3" type="audio/mp3">
    </audio>
    """,
    unsafe_allow_html=True
)

# =====================================================
# FILES CREATION
# =====================================================

if not os.path.exists("users.csv"):
    pd.DataFrame(columns=["username", "password"]).to_csv("users.csv", index=False)

if not os.path.exists("userdata.csv"):
    pd.DataFrame(
        columns=[
            "username",
            "date",
            "mood",
            "study_hours",
            "sleep_hours",
            "energy"
        ]
    ).to_csv("userdata.csv", index=False)

# =====================================================
# SESSION STATE
# =====================================================

if "logged_in" not in st.session_state:
    st.session_state.logged_in = False

if "username" not in st.session_state:
    st.session_state.username = ""

# =====================================================
# SIDEBAR
# =====================================================

st.sidebar.title("🌸 Navigation")

menu = st.sidebar.radio(
    "Go To",
    [
        "🏠 Home",
        "🔐 Login",
        "✨ Signup",
        "📊 Dashboard",
        "🤖 Chatbot",
        "🆘 Help"
    ]
)

# =====================================================
# HOME
# =====================================================

if menu == "🏠 Home":

    st.title("🌸 Cozy Anime Dashboard")

    st.markdown(
        """
        <div class="cute-box float">
        <h2>✨ Welcome ✨</h2>

        <p>
        A cozy anime themed productivity app made using
        Streamlit + Pandas + NumPy + Matplotlib.
        </p>

        <p>
        Features:
        <br>
        🌸 Login System
        <br>
        🌙 Persistent Saved Data
        <br>
        📊 Charts & Analytics
        <br>
        🤖 Funny Chatbot
        <br>
        🎧 Lofi Music
        <br>
        ✨ Aesthetic Anime UI
        </p>

        </div>
        """,
        unsafe_allow_html=True
    )

# =====================================================
# SIGNUP
# =====================================================

elif menu == "✨ Signup":

    st.title("✨ Create Account")

    new_user = st.text_input("Create Username")
    new_pass = st.text_input("Create Password", type="password")

    if st.button("Create Account 🌸"):

        users = pd.read_csv("users.csv")

        # remove spaces
        new_user = new_user.strip()
        new_pass = new_pass.strip()

        if new_user == "" or new_pass == "":
            st.warning("Please fill all fields")

        elif new_user in users["username"].astype(str).values:
            st.error("Username already exists 💀")

        else:

            new_data = pd.DataFrame({
                "username": [new_user],
                "password": [new_pass]
            })

            users = pd.concat([users, new_data], ignore_index=True)

            users.to_csv("users.csv", index=False)

            st.success("Account Created Successfully ✨")
            st.write("Now go to Login page 🌸")

# =====================================================
# LOGIN
# =====================================================

elif menu == "🔐 Login":

    st.title("🌙 Login")

    username = st.text_input("Username")
    password = st.text_input("Password", type="password")

    if st.button("Login ✨"):

        users = pd.read_csv("users.csv")

        # remove spaces
        username = username.strip()
        password = password.strip()

        # convert columns to string
        users["username"] = users["username"].astype(str)
        users["password"] = users["password"].astype(str)

        # check login
        user = users[
            (users["username"] == username) &
            (users["password"] == password)
        ]

        if not user.empty:

            st.session_state.logged_in = True
            st.session_state.username = username

            st.success(f"Welcome back {username} 🌸")

        else:
            st.error("Wrong username or password 😭")
# =====================================================
# DASHBOARD
# =====================================================

elif menu == "📊 Dashboard":

    if st.session_state.logged_in:

        st.title("📊 Cozy Dashboard")

        st.write(f"Logged in as: {st.session_state.username}")

        mood = st.selectbox(
            "Current Mood",
            [
                "Happy 🌸",
                "Sleepy 🌙",
                "Motivated ✨",
                "Dead Inside 💀",
                "Anime Training Arc ⚔️"
            ]
        )

        study_hours = st.slider(
            "Study Hours",
            0,
            15,
            2
        )

        sleep_hours = st.slider(
            "Sleep Hours",
            0,
            12,
            6
        )

        energy = st.slider(
            "Energy Level",
            0,
            100,
            50
        )

        if st.button("Save Today's Data 💾"):

            data = pd.read_csv("userdata.csv")

            data.loc[len(data)] = [
                st.session_state.username,
                datetime.now().strftime("%Y-%m-%d"),
                mood,
                study_hours,
                sleep_hours,
                energy
            ]

            data.to_csv("userdata.csv", index=False)

            st.success("Data Saved Successfully ✨")

        # =====================================================
        # LOAD USER DATA
        # =====================================================

        data = pd.read_csv("userdata.csv")

        user_data = data[
            data["username"] == st.session_state.username
        ]

        if not user_data.empty:

            st.subheader("📈 Your Analytics")

            avg_study = np.mean(user_data["study_hours"])
            avg_sleep = np.mean(user_data["sleep_hours"])
            avg_energy = np.mean(user_data["energy"])

            col1, col2, col3 = st.columns(3)

            with col1:
                st.metric("Average Study", f"{avg_study:.1f} hrs")

            with col2:
                st.metric("Average Sleep", f"{avg_sleep:.1f} hrs")

            with col3:
                st.metric("Average Energy", f"{avg_energy:.0f}%")

            # =====================================================
            # CHART 1
            # =====================================================

            st.subheader("📚 Study Progress")

            fig, ax = plt.subplots(figsize=(8,4))

            ax.plot(
                user_data["study_hours"],
                marker='o'
            )

            ax.set_xlabel("Entries")
            ax.set_ylabel("Study Hours")
            ax.set_title("Study Growth")

            st.pyplot(fig)

            # =====================================================
            # CHART 2
            # =====================================================

            st.subheader("😴 Sleep Analysis")

            fig2, ax2 = plt.subplots(figsize=(8,4))

            ax2.bar(
                user_data.index,
                user_data["sleep_hours"]
            )

            ax2.set_xlabel("Entries")
            ax2.set_ylabel("Sleep Hours")
            ax2.set_title("Sleep Chart")

            st.pyplot(fig2)

            # =====================================================
            # CHART 3
            # =====================================================

            st.subheader("⚡ Energy Analysis")

            fig3, ax3 = plt.subplots(figsize=(8,4))

            ax3.plot(
                user_data["energy"],
                marker='o'
            )

            ax3.set_title("Energy Levels")

            st.pyplot(fig3)

        else:
            st.info("No data available yet 🌸")

    else:
        st.warning("Please login first ✨")

# =====================================================
# CHATBOT
# =====================================================

elif menu == "🤖 Chatbot":

    st.title("🤖 Chibi AI Assistant")

    user_message = st.text_input("Talk with your anime assistant")

    responses = [

        "Go study before your exams become the final boss 💀",

        "You have two choices: productivity or another anime episode 🌸",

        "Hydration check! Drink water right now ✨",

        "Your brain currently has 97 tabs open 😭",

        "Sleep schedule left the chat 🌙",

        "You unlocked emotional damage achievement 🥲",

        "Touch grass after finishing one more episode ⚔️",

        "Congratulations! Your procrastination skill reached level 99 💀",

        "Even anime protagonists study harder during training arcs 📚"
    ]

    if st.button("Send 🌸"):

        if user_message != "":

            st.markdown(
                f"""
                <div class="cute-box">
                🤖 {random.choice(responses)}
                </div>
                """,
                unsafe_allow_html=True
            )

# =====================================================
# HELP TAB
# =====================================================

elif menu == "🆘 Help":

    st.title("🆘 Help Section")

    st.markdown(
        """
        <div class="cute-box">

        <h3>🌸 Beginner Guide</h3>

        <p>

        <b>1.</b> Create account from Signup page.
        <br><br>

        <b>2.</b> Login using your account.
        <br><br>

        <b>3.</b> Open Dashboard tab.
        <br><br>

        <b>4.</b> Save daily study and sleep data.
        <br><br>

        <b>5.</b> View charts and analytics.
        <br><br>

        <b>6.</b> Talk with funny chatbot assistant.
        <br><br>

        </p>

        <h3>✨ Technologies Used</h3>

        <p>

        🌸 Streamlit
        <br>
        📊 Pandas
        <br>
        🔢 NumPy
        <br>
        📈 Matplotlib

        </p>

        <h3>🌙 Future Upgrade Ideas</h3>

        <p>

        - AI chatbot
        <br>
        - Dark mode
        <br>
        - Pomodoro timer
        <br>
        - Anime quotes API
        <br>
        - Achievement system
        <br>
        - Journal feature
        <br>
        - Study streaks

        </p>

        </div>
        """,
        unsafe_allow_html=True
    )

# =====================================================
# FOOTER
# =====================================================

st.markdown("---")

st.caption("🌸 Made with Streamlit + Pandas + NumPy + Matplotlib")
