# 🤖 Groq Time Agent

A lightning-fast AI agent built with Python, powered by Groq's Llama 3.1 models. This agent demonstrates the core concepts of "Function Calling" (Tools) where the AI can interact with the real world—in this case, checking the local system time.

## 🚀 Features

- **Groq Powered**: Uses `llama-3.1-8b-instant` for near-instant responses.
- **Function Calling**: Real-time integration with Python functions.
- **Environment Driven**: Secure configuration using `.env` files.
- **Agentic Loop**: The AI thinks, calls a tool, observes the result, and responds naturally.

## 🛠️ Setup

1. **Clone the repository** (or navigate to the folder).
2. **Create a virtual environment**:
   ```powershell
   python -m venv .venv
   ```
3. **Install dependencies**:
   ```powershell
   & ".venv/Scripts/python.exe" -m pip install openai python-dotenv
   ```
4. **Configure API Key**:
   Create a `.env` file in the root directory and add your Groq API key:
   ```env
   GROQ_API_KEY=your_gsk_key_here
   ```

## 📖 Usage

Run the agent with the following command:

```powershell
& ".venv/Scripts/python.exe" agent.py
```

## 📂 Project Structure

- `agent.py`: The main logic for the AI agent and tool definitions.
- `.env`: (Ignored) Contains your sensitive API keys.
- `.gitignore`: Ensures sensitive and junk files aren't tracked.
- `.env.example`: A template for setting up your environment.

## 🧠 How it Works

1. **User asks a question**: "What time is it?"
2. **AI Decides**: The model realizes it doesn't know the time but has a `get_current_time` tool.
3. **Tool Execution**: Python runs `datetime.now()` and returns the string to the AI.
4. **Final Response**: The AI incorporates the time into a friendly message.
