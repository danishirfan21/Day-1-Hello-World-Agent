# 🤖 Groq AI Assistant

A lightning-fast AI agent built with Python, powered by Groq's Llama 3.1 models. This agent demonstrates the core concepts of "Function Calling" (Tools) where the AI can interact with the real world—specifically checking current time and weather across the globe.

### 🌐 Live Demo
[Check out the live agent here!](https://danish-time-agent.streamlit.app/)


## 🚀 Features

- **Groq Powered**: Uses `llama-3.1-8b-instant` for near-instant responses.
- **Function Calling**: Real-time integration with Python functions to fetch data.
- **Environment Driven**: Secure configuration using `.env` files.
- **Interactive UI**: Built with Streamlit for a clean, chat-like experience.
- **Global Timezone Support**: Powered by `pytz` to accurately check time anywhere.
- **Weather Insights**: Dynamically fetches weather data using the `wttr.in` service.
- **Agentic Loop**: The AI thinks, calls tools, observes results, and responds naturally.



## 🛠️ Setup

1. **Clone the repository** (or navigate to the folder).
2. **Create a virtual environment**:
   ```powershell
   python -m venv .venv
   ```
3. **Install dependencies**:
   ```powershell
   & ".venv/Scripts/python.exe" -m pip install -r requirements.txt

   ```
4. **Configure API Key**:
   Create a `.env` file in the root directory and add your Groq API key:
   ```env
   GROQ_API_KEY=your_gsk_key_here
   ```

## 📖 Usage

Run the web app:
```powershell
& ".venv/Scripts/python.exe" -m streamlit run app.py
```

Or run the terminal-based agent:
```powershell
& ".venv/Scripts/python.exe" agent.py
```


## 📂 Project Structure

- `app.py`: The Streamlit web application interface.
- `agent.py`: The terminal-based agent logic.
- `requirements.txt`: List of Python dependencies.
- `.env`: (Ignored) Contains your sensitive API keys.
- `.gitignore`: Ensures sensitive and junk files aren't tracked.
- `.env.example`: A template for setting up your environment.


## 🧠 How it Works

1. **User asks a question**: "What's the weather in London and what time is it there?"
2. **AI Decides**: The model identifies the location and realizes it needs two tools.
3. **Tool Execution**: 
   - Calls `get_current_time` for the timezone.
   - Calls `get_weather` to fetch atmospheric data.
4. **Final Response**: The AI combines the data and responds: "It's 2:00 PM in London with light rain and a temperature of 15°C."

