import streamlit as st
import ollama

st.set_page_config(page_title="Prashanth GPT", page_icon="✨", layout="centered")

# Custom CSS
st.markdown("""
    <style>
    .stApp {
        background-color: #ffffff;
        color: #1a1a1a;
    }
    h1 {
        text-align: center;
        background: linear-gradient(90deg, #4285F4, #9B72CB, #D96570);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        font-weight: 700;
    }
    /* User message bubble */
    [data-testid="stChatMessage"]:has([data-testid="chatAvatarIcon-user"]) {
        background-color: #f0f2f6;
        border-radius: 18px;
        padding: 12px 16px;
        margin: 6px 0;
        color: #1a1a1a;
    }
    /* Assistant message bubble */
    [data-testid="stChatMessage"]:has([data-testid="chatAvatarIcon-assistant"]) {
        background: linear-gradient(135deg, #f5f7fa, #e8ecf3);
        border: 1px solid #dde3ec;
        border-radius: 18px;
        padding: 14px 18px;
        margin: 6px 0;
        box-shadow: 0 2px 10px rgba(0,0,0,0.05);
        color: #1a1a1a;
    }
    </style>
""", unsafe_allow_html=True)

st.title("✨ Prashanth GPT")
st.caption("Powered by Qwen2.5 (Local via Ollama)")

if "messages" not in st.session_state:
    st.session_state.messages = []

if not st.session_state.messages:
    st.markdown(
        "<h3 style='text-align:center; color:#666;'>How can I help you today?</h3>",
        unsafe_allow_html=True
    )

for msg in st.session_state.messages:
    avatar = "🧑" if msg["role"] == "user" else "✨"
    with st.chat_message(msg["role"], avatar=avatar):
        st.markdown(msg["content"])

if prompt := st.chat_input("Message Prashanth GPT..."):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user", avatar="🧑"):
        st.markdown(prompt)

    with st.chat_message("assistant", avatar="✨"):
        with st.spinner("Thinking..."):
            response = ollama.chat(
                model="qwen2.5:3b",
                messages=st.session_state.messages
            )
            reply = response["message"]["content"]
        st.markdown(reply)

    st.session_state.messages.append({"role": "assistant", "content": reply})