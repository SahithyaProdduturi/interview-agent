import streamlit as st
from utils import call_openai_chat, generate_feedback

# ------------------------- SESSION STATE INIT -------------------------
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

if "submitted_input" not in st.session_state:
    st.session_state.submitted_input = None

if "role" not in st.session_state:
    st.session_state.role = "Software Engineer"

if "difficulty" not in st.session_state:
    st.session_state.difficulty = "Junior"

if "persona" not in st.session_state:
    st.session_state.persona = "Calm"


# ------------------------- PAGE UI -------------------------
st.title("🤖 Interview Practice Partner")

st.sidebar.header("Settings")
st.session_state.role = st.sidebar.selectbox(
    "Role", ["Software Engineer", "Data Scientist", "AI Engineer"], key="role_select"
)

st.session_state.difficulty = st.sidebar.selectbox(
    "Difficulty", ["Junior", "Mid", "Senior"], key="difficulty_select"
)

st.session_state.persona = st.sidebar.selectbox(
    "Interviewer Personality", ["Calm", "Strict", "Friendly", "Efficient"], key="persona_select"
)

st.write("### Conversation")
st.write("Your AI interviewer will ask you questions and follow up based on your responses.")


# ------------------------- SEND CALLBACK -------------------------
def send_message():
    """Triggered when the user presses Enter. Stores input and clears box."""
    st.session_state.submitted_input = st.session_state.user_input
    st.session_state.user_input = ""  # SAFE — executed before rerender


# ------------------------- USER INPUT -------------------------
st.text_input(
    "Your answer:",
    key="user_input",
    placeholder="Type here and press Enter...",
    on_change=send_message
)


# ------------------------- PROCESSING USER INPUT -------------------------
if st.session_state.submitted_input:
    user_text = st.session_state.submitted_input.strip()

    if user_text:
        st.session_state.chat_history.append({"role": "user", "content": user_text})

        reply = call_openai_chat(
            role=st.session_state.role,
            difficulty=st.session_state.difficulty,
            persona=st.session_state.persona,
            history=st.session_state.chat_history
        )

        st.session_state.chat_history.append({"role": "assistant", "content": reply})

    st.session_state.submitted_input = None


# ------------------------- DISPLAY CHAT -------------------------
for message in st.session_state.chat_history:
    if message["role"] == "user":
        st.markdown(f"🧑 **You:** {message['content']}")
    else:
        st.markdown(f"🤖 **Bot:** {message['content']}")


# ------------------------- FEEDBACK BUTTON -------------------------
if st.button("🏁 End & Generate Feedback"):
    if len(st.session_state.chat_history) > 2:
        feedback = generate_feedback(
            role=st.session_state.role,
            difficulty=st.session_state.difficulty,
            history=st.session_state.chat_history
        )
        st.success("📄 Feedback Ready!")
        st.write(feedback)
    else:
        st.warning("⚠️ Please answer at least 3 questions before ending.")
