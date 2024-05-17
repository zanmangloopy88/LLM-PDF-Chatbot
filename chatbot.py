import streamlit as st
import cohere

# An example LLM chatbot using Cohere API and Streamlit
# Adapted from the StreamLit OpenAI Chatbot example - https://github.com/streamlit/llm-examples/blob/main/Chatbot.py

# Add a sidebar to the Streamlit app
with st.sidebar:
    cohere_api_key = st.text_input("Cohere API Key", key="chatbot_api_key", type="password")
    st.markdown("[Get a Cohere API Key](https://dashboard.cohere.ai/api-keys)")

# Set the title of the Streamlit app
st.title("💬 My First Chatbot")

# Initialize the chat history with a greeting message
if "messages" not in st.session_state:
    st.session_state["messages"] = [{"role": "assistant", "text": "How can I help you?"}]

# Display the chat messages
for msg in st.session_state.messages:
    st.chat_message(msg["role"]).write(msg["text"])

# Get user input
if prompt := st.chat_input():
    # Stop responding if the user has not added the Cohere API key
    if not cohere_api_key:
        st.info("Please add your Cohere API key to continue.")
        st.stop()

    # Create a connection to the Cohere API
    client = cohere.Client(api_key=cohere_api_key)
    
    # Display the user message in the chat window
    st.chat_message("user").write(prompt)

    # Send the user message to the model and capture the response
    response = client.chat(model="command-r", 
                           chat_history=st.session_state.messages,
                           message=prompt)
    
    # Add the user prompt to the chat history
    st.session_state.messages.append({"role": "user", "text": prompt})
    
    # Add the response to the chat history
    msg = response.text
    st.session_state.messages.append({"role": "assistant", "text": msg})

    # Write the response to the chat window
    st.chat_message("assistant").write(msg)