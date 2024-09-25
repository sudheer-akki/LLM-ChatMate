import os
import streamlit as st
from LLM_Model import local_llm
import logging

# Configure logging
logging.basicConfig(level=logging.INFO)

st.title("💬ChatMate")
st.write("A LLM powered Streamlit app")


# Hugging Face Credentials
with st.sidebar:
    st.header('Hugging Face Login')
    hf_email = st.text_input('Enter E-mail:', type='password')
    hf_pass = st.text_input('Enter password:', type='password')

#clear chat history tab
def clear_chat_history():
    st.session_state.messages = [{"role": "assistant", "content": "How may I assist you today?"}]
st.sidebar.button('Clear Chat History', on_click=clear_chat_history)

if "messages" not in st.session_state:
    st.session_state["messages"] = [{"role": "assistant", "content": "How may I assist you today?"}]

# Display existing chat messages
for msg in st.session_state.messages:
    st.chat_message(msg["role"]).write(msg["content"])

if prompt := st.chat_input():
    st.session_state.messages.append({"role": "user", "content": prompt})
    st.chat_message("user").write(prompt)
    # Generate a new response if last message is not from assistant
    if st.session_state.messages[-1]["role"] != "assistant":
        with st.chat_message("assistant"):
            with st.spinner("Thinking..."):
                response = local_llm(prompt)
                placeholder = st.empty()
                full_response = ''
                for item in response:
                    full_response += item
                    placeholder.markdown(full_response)
                placeholder.markdown(full_response)
        message = {"role": "assistant", "content": full_response}
        st.session_state.messages.append(message)