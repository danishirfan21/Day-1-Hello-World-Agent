import streamlit as st
import os
import pytz
from groq import Groq
from datetime import datetime
from dotenv import load_dotenv

load_dotenv()

# --- 1. SETUP ---
st.set_page_config(page_title="AI Time Agent", page_icon="🤖")
st.title("🤖 My First AI Agent")
st.caption("Powered by Groq & Llama 3.1")

client = Groq(api_key=os.environ.get("GROQ_API_KEY"))

# --- 2. THE TOOL ---
def get_current_time(location=None):
    try:
        if location:
            # Simple mapping for common cities/locations if needed, 
            # but pytz handles many standard ones.
            tz = pytz.timezone(location)
            now = datetime.now(tz)
            return f"{now.strftime('%I:%M %p')} ({location})"
        else:
            # Default to UTC or a specific local time
            now = datetime.now()
            return f"{now.strftime('%I:%M %p')} (Local Server Time)"
    except Exception:
        # Fallback if timezone is not found
        now = datetime.now()
        return f"{now.strftime('%I:%M %p')} (Local Server Time)"

# --- 3. THE UI LOGIC ---
if "messages" not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

if prompt := st.chat_input("Ask me for the time... e.g., 'What time is it in London?'"):
    st.chat_message("user").markdown(prompt)
    st.session_state.messages.append({"role": "user", "content": prompt})

    with st.chat_message("assistant"):
        with st.status("Agent is thinking...", expanded=True) as status:
            response = client.chat.completions.create(
                model="llama-3.1-8b-instant",
                messages=[{"role": "user", "content": prompt}],
                tools=[{
                    "type": "function",
                    "function": {
                        "name": "get_current_time",
                        "description": "Get the current time for a specific location.",
                        "parameters": {
                            "type": "object",
                            "properties": {
                                "location": {
                                    "type": "string",
                                    "description": "The location or timezone (e.g., 'America/New_York', 'Europe/London', 'Asia/Karachi')."
                                }
                            }
                        }
                    }
                }]
            )
            
            response_message = response.choices[0].message
            
            if response_message.tool_calls:
                st.write("🕒 Checking the system clock...")
                # Extract arguments safely
                import json
                tool_call = response_message.tool_calls[0]
                args = json.loads(tool_call.function.arguments)
                location = args.get("location")
                
                time_now = get_current_time(location)
                status.update(label="Time retrieved!", state="complete", expanded=False)
                final_answer = f"The current time is {time_now}."
            else:
                status.update(label="Thinking complete", state="complete", expanded=False)
                final_answer = response_message.content
        
        st.markdown(final_answer)
        st.session_state.messages.append({"role": "assistant", "content": final_answer})

