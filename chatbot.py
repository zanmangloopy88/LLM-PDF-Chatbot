# An example LLM chatbot using Cohere API and Streamlit
# Adapted from the StreamLit OpenAI Chatbot example - https://github.com/streamlit/llm-examples/blob/main/Chatbot.py

import streamlit as st
import cohere
import fitz

# Converts a PDF to a list of 'document' chunks for processing by the Cohere LLM
# Each 'document' chunk is a dictionary with a 'title' and 'snippet' key
# Example return value: [{"title": "Page 1 Section 1", "snippet": "Text snippet..."}, ...]
def pdf_to_documents(pdf_path):
    doc = fitz.open(pdf_path)
    text = ""
    chunk_size = 1000
    documents = []
    for page_num in range(len(doc)):
        page = doc.load_page(page_num)
        text = page.get_text()
        part_num = 1
        for i in range(0, len(text), chunk_size):
            documents.append({"title": f"Page {page_num + 1} Part {part_num}", "snippet": text[i:i + chunk_size]})
            part_num += 1
    return documents

# Add a sidebar to the Streamlit app
with st.sidebar:
    if st.secrets["COHERE_API_KEY"]:
        cohere_api_key = st.secrets["COHERE_API_KEY"]
        st.write("API key found.")
    else:
        cohere_api_key = st.text_input("Cohere API Key", key="chatbot_api_key", type="password")
        st.markdown("[Get a Cohere API Key](https://dashboard.cohere.ai/api-keys)")
    
    document = st.selectbox("Select a document to talk to", ["AP CS Principles CED", "Tai Tam Bus Schedule", "Repulse Bay Bus Schedule"])
    if document == "AP CS Principles CED":
        my_documents = pdf_to_documents('apcsp-ced.pdf')
    elif document == "Tai Tam Bus Schedule":
        my_documents = pdf_to_documents('HKISTaiTamBusSchedule.pdf')
    elif document == "Repulse Bay Bus Schedule":    
        my_documents = pdf_to_documents('HKISRepulseBayBusSchedule.pdf')
    else:
        my_documents = pdf_to_documents('apcsp-ced.pdf')
    st.write(f"Selected document: {document}")

# Set the title of the Streamlit app
st.title("💬 Personal Assistant")

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

    # Send the user message and pdf text to the model and capture the response
    response = client.chat(chat_history=st.session_state.messages,
                           message=prompt,
                           documents=my_documents,
                           prompt_truncation='AUTO')
    
    # Add the user prompt to the chat history
    st.session_state.messages.append({"role": "user", "text": prompt})
    
    # Add the response to the chat history
    msg = response.text
    st.session_state.messages.append({"role": "assistant", "text": msg})

    # Write the response to the chat window
    st.chat_message("assistant").write(msg)