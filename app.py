import streamlit as st
import ollama
from streamlit_mic_recorder import speech_to_text
from gtts import gTTS
from pypdf import PdfReader
import base64
import io
import json
import datetime
import os
import requests

st.set_page_config(page_title="Prashanth GPT", page_icon="✨", layout="centered")

# Retrieve Groq API Key if configured
groq_api_key = None
try:
    groq_api_key = st.secrets.get("GROQ_API_KEY")
except Exception:
    pass

if not groq_api_key:
    groq_api_key = os.environ.get("GROQ_API_KEY")

# Initialize Ollama client (checks Streamlit secrets, environment, or defaults to localhost)
ollama_host = None
try:
    ollama_host = st.secrets.get("OLLAMA_HOST")
except Exception:
    pass

if not ollama_host:
    ollama_host = os.environ.get("OLLAMA_HOST")

if ollama_host:
    client = ollama.Client(host=ollama_host, headers={'Bypass-Tunnel-Reminder': 'true'})
else:
    client = ollama.Client()

# ══════════════════════════════════════════
# CUSTOM CSS
# ══════════════════════════════════════════
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&display=swap');
* { font-family: 'Inter', sans-serif; }

.stApp { background-color: #f7f8fc; color: #1a1a1a; }

h1 {
    text-align: center;
    background: linear-gradient(90deg, #4285F4, #9B72CB, #D96570);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    font-weight: 800; font-size: 2.1rem;
    padding: 10px 0 2px;
}

/* User bubble */
[data-testid="stChatMessage"]:has([data-testid="chatAvatarIcon-user"]) {
    background: #e8f0fe;
    border-radius: 18px; padding: 12px 16px; margin: 6px 0;
}

/* Assistant bubble */
[data-testid="stChatMessage"]:has([data-testid="chatAvatarIcon-assistant"]) {
    background: linear-gradient(135deg, #f5f7fa, #e8ecf3);
    border: 1px solid #dde3ec; border-radius: 18px;
    padding: 14px 18px; margin: 6px 0;
    box-shadow: 0 2px 10px rgba(0,0,0,0.05);
}

/* Padding so messages don't hide behind the input bar */
.main .block-container { padding-bottom: 120px !important; }

/* Sidebar section headers */
.sidebar-section {
    font-size: 13px; font-weight: 700; color: #6b7280;
    text-transform: uppercase; letter-spacing: 0.05em;
    margin: 12px 0 6px;
}

/* Welcome card */
.welcome-card {
    background: linear-gradient(135deg, #fff, #f0f4ff);
    border: 1px solid #c7d7fd; border-radius: 20px;
    padding: 28px 24px; text-align: center; margin: 40px 0;
}
.welcome-card h2 { color: #3b5bdb; font-size: 1.4rem; margin-bottom: 8px; }
.welcome-card p  { color: #6b7280; font-size: 14px; margin: 0; }

/* Suggestion chips */
.chip-row { display: flex; flex-wrap: wrap; gap: 8px; justify-content: center; margin-top: 16px; }
</style>
""", unsafe_allow_html=True)

# ══════════════════════════════════════════
# SESSION STATE
# ══════════════════════════════════════════
defaults = {
    "messages": [],
    "system_prompt": (
        "You are Prashanth GPT, a helpful, knowledgeable, and friendly AI assistant. "
        "Provide clear, accurate, and thoughtful responses. When relevant, use examples, "
        "bullet points, and code blocks to make answers easy to understand."
    ),
    "tokens_used": 0,
    "model": "llama-3.1-8b-instant" if groq_api_key else "qwen2.5:3b",
}
for k, v in defaults.items():
    if k not in st.session_state:
        st.session_state[k] = v

# ══════════════════════════════════════════
# HELPER FUNCTIONS
# ══════════════════════════════════════════
def check_ollama():
    """Check if Ollama is running and reachable (bypassed if Groq is active)."""
    if groq_api_key:
        return True
    try:
        client.list()
        return True
    except Exception:
        return False

def get_available_models():
    """Fetch locally available Ollama models or Groq cloud models."""
    if groq_api_key:
        return [
            "llama-3.3-70b-versatile",
            "llama-3.1-8b-instant",
            "llama-3.2-11b-vision-preview",
            "mixtral-8x7b-32768",
            "gemma2-9b-it"
        ]
    try:
        # New ollama library returns typed Model objects, access via .model attribute
        return [m.model for m in client.list().models]
    except Exception:
        return ["qwen2.5:3b", "llava:latest", "mistral", "llama3.2"]

def play_audio(text):
    """Convert text to speech and auto-play it."""
    try:
        tts = gTTS(text=text, lang='en', slow=False)
        fp = io.BytesIO()
        tts.write_to_fp(fp)
        fp.seek(0)
        b64 = base64.b64encode(fp.read()).decode()
        st.markdown(
            f'<audio autoplay><source src="data:audio/mp3;base64,{b64}" type="audio/mp3"></audio>',
            unsafe_allow_html=True
        )
    except Exception as e:
        st.warning(f"TTS error: {e}")

def export_json():
    """Export chat history as JSON."""
    return json.dumps({
        "app": "Prashanth GPT",
        "exported_at": datetime.datetime.now().isoformat(),
        "model": st.session_state.model,
        "system_prompt": st.session_state.system_prompt,
        "messages": st.session_state.messages,
    }, indent=2)

def export_txt():
    """Export chat history as plain text."""
    lines = [
        f"Prashanth GPT — Chat Export",
        f"Date: {datetime.datetime.now().strftime('%Y-%m-%d %H:%M')}",
        f"Model: {st.session_state.model}",
        "=" * 50,
    ]
    for msg in st.session_state.messages:
        role = "You" if msg["role"] == "user" else "Prashanth GPT"
        lines.append(f"\n[{role}]\n{msg['content']}")
    return "\n".join(lines)

def stream_reply(model, messages, temperature):
    """Stream a reply from Ollama or Groq, yielding content chunks."""
    if groq_api_key:
        try:
            url = "https://api.groq.com/openai/v1/chat/completions"
            headers = {
                "Authorization": f"Bearer {groq_api_key}",
                "Content-Type": "application/json"
            }
            clean_messages = []
            for m in messages:
                clean_messages.append({"role": m["role"], "content": m["content"]})
            data = {
                "model": model,
                "messages": clean_messages,
                "stream": True,
                "temperature": temperature
            }
            response = requests.post(url, headers=headers, json=data, stream=True)
            if response.status_code != 200:
                yield f"❌ Groq Error {response.status_code}: {response.text}"
                return
            for line in response.iter_lines():
                if line:
                    decoded = line.decode('utf-8')
                    if decoded.startswith("data: "):
                        content = decoded[6:]
                        if content == "[DONE]":
                            break
                        try:
                            chunk_json = json.loads(content)
                            delta = chunk_json['choices'][0]['delta']
                            if 'content' in delta:
                                yield delta['content']
                        except Exception:
                            pass
        except Exception as e:
            yield f"❌ Error: {e}"
    else:
        try:
            stream = client.chat(
                model=model,
                messages=messages,
                stream=True,
                options={"temperature": temperature}
            )
            for chunk in stream:
                yield chunk["message"]["content"]
        except Exception as e:
            yield f"❌ Error: {e}"

# ══════════════════════════════════════════
# OLLAMA HEALTH CHECK
# ══════════════════════════════════════════
if not check_ollama():
    st.error("⚠️ **Ollama is not running.** Please start it first:")
    st.code("ollama serve", language="bash")
    st.info("Then pull a model:  `ollama pull qwen2.5:3b`")
    st.stop()

# ══════════════════════════════════════════
# SIDEBAR
# ══════════════════════════════════════════
with st.sidebar:
    st.markdown("## ⚙️ Settings")

    # ── Model Selection ──
    st.markdown('<div class="sidebar-section">🤖 Model</div>', unsafe_allow_html=True)
    available_models = get_available_models()
    selected_model = st.selectbox(
        "Model",
        available_models,
        index=available_models.index(st.session_state.model)
              if st.session_state.model in available_models else 0,
        label_visibility="collapsed",
        help="Switch between locally downloaded Ollama models."
    )
    st.session_state.model = selected_model

    # ── Temperature ──
    st.markdown('<div class="sidebar-section">🌡️ Temperature</div>', unsafe_allow_html=True)
    temperature = st.slider(
        "Temperature",
        min_value=0.0, max_value=2.0, value=0.7, step=0.1,
        label_visibility="collapsed",
        help="0 = precise & focused | 1+ = creative & varied"
    )
    st.caption(f"{'🎯 Focused' if temperature < 0.4 else '⚖️ Balanced' if temperature < 1.0 else '🎨 Creative'} ({temperature})")

    # ── System Prompt ──
    st.markdown('<div class="sidebar-section">🧠 System Prompt</div>', unsafe_allow_html=True)
    with st.expander("Edit system prompt", expanded=False):
        st.session_state.system_prompt = st.text_area(
            "System Prompt",
            value=st.session_state.system_prompt,
            height=130,
            label_visibility="collapsed"
        )

    st.markdown("---")

    # ── Voice Input ──
    st.markdown('<div class="sidebar-section">🎙️ Voice Input</div>', unsafe_allow_html=True)
    voice_text = speech_to_text(
        language='en',
        start_prompt="🎙️ Start Recording",
        stop_prompt="🛑 Stop Recording",
        just_once=True,
        key="mic_input"
    )
    st.caption("Voice → AI replies spoken aloud  |  Text → silent")

    st.markdown("---")

    # ── File Attachments ──
    st.markdown('<div class="sidebar-section">📁 Attachments</div>', unsafe_allow_html=True)
    uploaded_file = st.file_uploader(
        "Upload PDF or Image",
        type=["pdf", "png", "jpg", "jpeg"],
        label_visibility="collapsed"
    )

    st.markdown("---")

    # ── Actions ──
    st.markdown('<div class="sidebar-section">🛠️ Actions</div>', unsafe_allow_html=True)

    if st.button("🗑️ Clear Chat", use_container_width=True):
        st.session_state.messages = []
        st.session_state.tokens_used = 0
        st.rerun()

    fname = datetime.datetime.now().strftime("%Y%m%d_%H%M")
    col_j, col_t = st.columns(2)
    with col_j:
        st.download_button(
            "⬇️ JSON",
            data=export_json(),
            file_name=f"chat_{fname}.json",
            mime="application/json",
            use_container_width=True,
            help="Export full conversation as JSON"
        )
    with col_t:
        st.download_button(
            "📄 TXT",
            data=export_txt(),
            file_name=f"chat_{fname}.txt",
            mime="text/plain",
            use_container_width=True,
            help="Export conversation as plain text"
        )

    if len(st.session_state.messages) >= 2:
        if st.button("🔄 Regenerate Last Reply", use_container_width=True):
            # Remove last assistant message and re-trigger
            if st.session_state.messages and st.session_state.messages[-1]["role"] == "assistant":
                st.session_state.messages.pop()
            st.session_state["_regenerate"] = True
            st.rerun()

    st.markdown("---")

    # ── Stats ──
    st.markdown('<div class="sidebar-section">📊 Stats</div>', unsafe_allow_html=True)
    total = len(st.session_state.messages)
    user_turns = sum(1 for m in st.session_state.messages if m["role"] == "user")
    col1, col2 = st.columns(2)
    col1.metric("Messages", total)
    col2.metric("Your turns", user_turns)
    if st.session_state.tokens_used > 0:
        st.caption(f"~{st.session_state.tokens_used:,} tokens used (est.)")

# ══════════════════════════════════════════
# FILE PROCESSING
# ══════════════════════════════════════════
file_context = ""
image_bytes = None

if uploaded_file:
    ext = uploaded_file.name.split(".")[-1].lower()
    if ext == "pdf":
        reader = PdfReader(io.BytesIO(uploaded_file.read()))
        file_context = "".join([p.extract_text() or "" for p in reader.pages])
        st.sidebar.success(f"📚 PDF ready! ({len(file_context):,} chars extracted)")
    elif ext in ["png", "jpg", "jpeg"]:
        image_bytes = uploaded_file.read()
        st.sidebar.image(image_bytes, caption="Image loaded", use_container_width=True)
        st.sidebar.success("🖼️ Image ready!")
        if "llava" not in selected_model.lower():
            st.sidebar.info("💡 Switch to `llava` model for image analysis.")

# ══════════════════════════════════════════
# MAIN AREA — TITLE
# ══════════════════════════════════════════
st.title("✨ Prashanth GPT")
st.caption(f"Advanced AI Assistant · `{selected_model}` · 🌡️ {temperature}")

# ── Welcome screen when no messages ──
if not st.session_state.messages:
    st.markdown("""
    <div class="welcome-card">
        <h2>👋 Welcome to Prashanth GPT</h2>
        <p>Ask anything — type below, use voice, or attach a PDF / image from the sidebar.</p>
    </div>
    """, unsafe_allow_html=True)

    # Suggested starter prompts
    st.markdown("**Try one of these:**")
    suggestions = [
        "Explain machine learning in simple terms",
        "Write a Python function to sort a list",
        "What are the latest trends in AI?",
        "Help me debug my code",
        "Summarise a topic for me",
        "Write a professional email",
    ]
    cols = st.columns(3)
    for i, s in enumerate(suggestions):
        if cols[i % 3].button(s, key=f"sug_{i}", use_container_width=True):
            st.session_state["_preset_prompt"] = s
            st.rerun()

# ══════════════════════════════════════════
# CHAT HISTORY
# ══════════════════════════════════════════
for msg in st.session_state.messages:
    avatar = "🧑" if msg["role"] == "user" else "✨"
    with st.chat_message(msg["role"], avatar=avatar):
        st.markdown(msg["content"])

# ══════════════════════════════════════════
# INPUT
# ══════════════════════════════════════════
typed_text = st.chat_input("Message Prashanth GPT...")

# Pick up preset prompt from suggestion chips
if "_preset_prompt" in st.session_state:
    typed_text = st.session_state.pop("_preset_prompt")

# ══════════════════════════════════════════
# PROCESS INPUT
# ══════════════════════════════════════════
user_input = voice_text or typed_text
is_voice = bool(voice_text)

# Handle regenerate
if st.session_state.get("_regenerate") and st.session_state.messages:
    user_input = st.session_state.messages[-1]["content"]  # last user message
    is_voice = False
    st.session_state["_regenerate"] = False

if user_input:
    # ── Show user message ──
    if not st.session_state.get("_regenerate"):
        st.session_state.messages.append({"role": "user", "content": user_input})
        with st.chat_message("user", avatar="🧑"):
            st.markdown(user_input)

    # ── Build message history for Ollama ──
    prompt = f"Context from uploaded file:\n{file_context}\n\nUser question: {user_input}" if file_context else user_input
    user_msg = {"role": "user", "content": prompt}
    if image_bytes:
        user_msg["images"] = [image_bytes]

    model_to_use = selected_model
    if image_bytes:
        if groq_api_key:
            model_to_use = "llama-3.2-11b-vision-preview"
        elif "llava" not in selected_model.lower():
            model_to_use = "llava:latest"

    history = [{"role": "system", "content": st.session_state.system_prompt}]
    history += st.session_state.messages[:-1] + [user_msg]

    # ── Stream response ──
    with st.chat_message("assistant", avatar="✨"):
        placeholder = st.empty()
        full_response = ""
        tokens_this_reply = 0

        try:
            if groq_api_key:
                url = "https://api.groq.com/openai/v1/chat/completions"
                headers = {
                    "Authorization": f"Bearer {groq_api_key}",
                    "Content-Type": "application/json"
                }
                
                # Build messages payload for Groq (handling base64 images)
                clean_history = []
                for m in history:
                    if m.get("images"):
                        b64_img = base64.b64encode(m["images"][0]).decode("utf-8")
                        clean_content = [
                            {"type": "text", "text": m["content"]},
                            {"type": "image_url", "image_url": {"url": f"data:image/jpeg;base64,{b64_img}"}}
                        ]
                        clean_history.append({"role": m["role"], "content": clean_content})
                    else:
                        clean_history.append({"role": m["role"], "content": m["content"]})

                data = {
                    "model": model_to_use,
                    "messages": clean_history,
                    "stream": True,
                    "temperature": temperature
                }
                
                response = requests.post(url, headers=headers, json=data, stream=True)
                if response.status_code != 200:
                    full_response = f"❌ Groq Error {response.status_code}: {response.text}"
                    placeholder.error(full_response)
                else:
                    for line in response.iter_lines():
                        if line:
                            decoded_line = line.decode('utf-8')
                            if decoded_line.startswith("data: "):
                                content = decoded_line[6:]
                                if content == "[DONE]":
                                    break
                                try:
                                    chunk_json = json.loads(content)
                                    delta = chunk_json['choices'][0]['delta']
                                    if 'content' in delta:
                                        full_response += delta['content']
                                        placeholder.markdown(full_response + "▌")
                                except Exception:
                                    pass
                    placeholder.markdown(full_response)
            else:
                stream = client.chat(
                    model=model_to_use,
                    messages=history,
                    stream=True,
                    options={"temperature": temperature}
                )
                for chunk in stream:
                    content = chunk.message.content or ""
                    full_response += content
                    placeholder.markdown(full_response + "▌")
                    if chunk.done and chunk.eval_count:
                        tokens_this_reply = chunk.eval_count
                placeholder.markdown(full_response)

            st.session_state.tokens_used += tokens_this_reply or max(1, len(full_response) // 4)

        except Exception as e:
            full_response = f"❌ Error: {e}"
            placeholder.error(full_response)

        # Speak reply only for voice input
        if is_voice and full_response and not full_response.startswith("❌"):
            play_audio(full_response)

    st.session_state.messages.append({"role": "assistant", "content": full_response})
