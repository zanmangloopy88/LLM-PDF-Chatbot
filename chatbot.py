import streamlit as st
import cohere
import fitz

def extract_text_from_pdf(pdf_path):
    doc = fitz.open(pdf_path)
    text = ""
    for page_num in range(len(doc)):
        page = doc.load_page(page_num)
        text += page.get_text()
    return text

# Sample function to process the text and query LLM
def process_and_query_llm(text, llm):
    # Example: Split text into chunks and query each chunk
    chunks = [text[i:i + 1000] for i in range(0, len(text), 1000)]
    results = []
    for chunk in chunks:
        response = llm.query(chunk)
        results.append(response)
    return results

print("Hello")

pdf_path = 'apcsp-ced.pdf'
pdf_text = extract_text_from_pdf(pdf_path)

# # Process and query
# responses = process_and_query_llm(pdf_text, cohere_llm)

# # Output responses
# for i, response in enumerate(responses):
#     print(f"Response {i + 1}:\n{response}\n")


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
    response = client.chat(chat_history=st.session_state.messages,
                           message=prompt)
    
    # Add the user prompt to the chat history
    st.session_state.messages.append({"role": "user", "text": prompt})
    
    # Add the response to the chat history
    msg = response.text
    st.session_state.messages.append({"role": "assistant", "text": msg})

    # Write the response to the chat window
    st.chat_message("assistant").write(msg)