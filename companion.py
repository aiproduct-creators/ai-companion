import os
from dotenv import load_dotenv
import openai
import streamlit as st
from config import SYSTEM_PROMPT

# Load OpenAI API key from your .env file
load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

# Use CSS to add custom styles to your UI
with open("style.css") as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

# Side bar
if st.sidebar.button("New Chat", key="clear_chat"):
    st.session_state.messages = []
st.sidebar.title("AVA")
st.sidebar.markdown("It is your AI companion for Quality Assurance (QA)")
st.sidebar.markdown("It helps you debug the code")
st.sidebar.markdown("Provide your code or ask for help")

# Main content
st.title("AI Companion")
if "openai_model" not in st.session_state:
    st.session_state["openai_model"] = "gpt-3.5-turbo"

if "messages" not in st.session_state:
    st.session_state.messages = []
    st.session_state.messages.append({"role": "system", "content": SYSTEM_PROMPT})

for message in st.session_state.messages:
    if message["role"] != "system":
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

if prompt := st.chat_input("Ask a question"):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    with st.chat_message("assistant"):
        message_placeholder = st.empty()
        full_response = ""
        is_function_json = False
        # Optional loading icon while waiting for response
        with st.spinner("✨🤖✨"):
            for response in openai.ChatCompletion.create(
                model=st.session_state["openai_model"],
                messages=[
                    {"role": m["role"], "content": m["content"]}
                    for m in st.session_state.messages
                ],
                temperature=0,
                stream=True,
            ):
                stream_text = response.choices[0].delta

                full_response += stream_text.get("content", "")
                message_placeholder.markdown(full_response + "▌")
                message_placeholder.markdown(full_response)
    st.session_state.messages.append({"role": "assistant", "content": full_response})
