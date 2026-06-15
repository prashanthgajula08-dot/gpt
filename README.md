# ✨ Prashanth GPT

Prashanth GPT is a highly interactive, features-rich, and visually polished Streamlit-based AI assistant. Powered by locally-run LLMs via **Ollama**, this application supports rich conversational features, text-to-speech feedback, voice recordings, document context loading (PDFs), and image analysis (multimodal).

---

## 🚀 Key Features

- **🤖 Local LLM Support**: Integrates directly with Ollama. Dynamically switches between local models (e.g., `qwen2.5:3b`, `llava:latest`, `llama3.2`, etc.) and lets you adjust temperature values.
- **🎙️ Voice Input & TTS Output**: Record voice messages directly using the mic in the sidebar. When voice is used, the AI's reply is spoken aloud automatically (using Text-to-Speech).
- **📚 PDF Document Reading**: Upload any PDF to automatically extract text and provide it as context to your questions.
- **🖼️ Multimodal Image Analysis**: Attach images (PNG, JPG, JPEG) to analyze them visually (automatically triggers/recommends the `llava` model).
- **💾 Conversation Export**: Export your chat session history anytime to either structured **JSON** or clean plain text **TXT** format.
- **🛠️ Chat Management**: Easily clear conversation history, regenerate the last AI response, and edit the System Prompt directly in the UI.
- **📊 Real-time Stats**: View token usage estimations and message/turn metrics directly in the sidebar.
- **🎨 Premium Interface**: Leverages beautiful CSS styles including custom-curated font pairings (Inter), gradient background details, clean chat bubble designs, and custom cards.

---

## 🛠️ Prerequisites & Installation

Before running the application, make sure you have python and Ollama installed.

### 1. Install Ollama & Pull Models
1. Download and install Ollama from [ollama.com](https://ollama.com).
2. Start the Ollama service:
   ```bash
   ollama serve
   ```
3. Pull your preferred models (e.g., `qwen2.5:3b` and `llava` for image inputs):
   ```bash
   ollama pull qwen2.5:3b
   ollama pull llava:latest
   ```

### 2. Setup Project Dependencies
Clone this repository and install the required Python packages:
```bash
pip install -r requirements.txt
```

---

## 🏃 Running the Application

Launch the Streamlit app locally with the following command:
```bash
streamlit run app.py
```
This will open the application in your default web browser (typically at `http://localhost:8501`).

---

## 🌐 Deployment Options

Since Prashanth GPT relies on a local installation of Ollama, hosting the application in the cloud requires making sure Ollama is reachable. Here are three ways to deploy:

### Option A: Local Expose via Ngrok (Easiest for sharing)
If you want to quickly share your running local application with others:
1. Download and install [Ngrok](https://ngrok.com/).
2. Run your Streamlit app locally (port 8501).
3. Expose the port through Ngrok:
   ```bash
   ngrok http 8501
   ```
4. Share the generated public URL.

### Option B: Cloud VM (AWS, GCP, DigitalOcean)
To deploy on a dedicated cloud server:
1. Spin up an Linux VM instance (ideally with GPU support for fast inference).
2. Install Ollama, pull the models, and run the Ollama service in the background.
3. Install Python dependencies and run Streamlit.
4. Open the VM's firewalls for Streamlit's port (`8501`) to access it publicly.

### Option C: Streamlit Community Cloud + Remote Ollama
1. Commit this codebase and push it to a public GitHub repository.
2. Sign in to [Streamlit Community Cloud](https://share.streamlit.io/) and link it to your repository.
3. Deploy the application.
4. **Note**: Since Ollama won't run natively inside Streamlit Cloud's container, you must configure a public URL/environment variable for Ollama. By default, the `ollama` Python client respects the `OLLAMA_HOST` environment variable. You can specify this in Streamlit secrets pointing to a remote Ollama endpoint:
   ```toml
   # Streamlit secrets config
   OLLAMA_HOST = "http://your-public-ollama-host:11434"
   ```
