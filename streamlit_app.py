import streamlit as st
from youtube_search import YoutubeSearch
import together
import colorama
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Initialize colorama
colorama.init(autoreset=True)

# Set up your API key for Together API
together.api_key = os.getenv('TOGETHER_API_KEY')
model = "mistralai/Mixtral-8x7B-Instruct-v0.1"

# Default system prompt that defines the chatbot's health-focused orientation
default_system_prompt = (
    "I am HealthBot, your personal health assistant. My purpose is to provide accurate, reliable, and easy-to-understand "
    "information on health-related topics. I am not a substitute for professional medical advice, diagnosis, or treatment. "
    "Feel free to ask me anything about health, wellness, fitness, or nutrition, and I'll do my best to assist."
)

# Function to perform YouTube search and retrieve video links
def search_videos(query, max_results=5):
    try:
        results = YoutubeSearch(query, max_results=max_results).to_dict()
        video_links = [f"https://www.youtube.com/watch?v={result['id']}" for result in results]
        return video_links
    except Exception as e:
        return []

# Function to generate a response using Together's API
def generate_response_with_together(user_query):
    # Building the prompt with the default system prompt and user's query
    prompt = f"{default_system_prompt}\n\nUser's Health Query: {user_query}"
    output = together.Complete.create(
        prompt=prompt,
        model=model,
        max_tokens=512,
        temperature=0.7,
        top_k=50,
        top_p=0.7,
        repetition_penalty=1,
        stop=["</s>"]  # Specify any sequence you want to stop generating at.
    )
    model_out = output['output']['choices'][0]['text'].strip()
    return model_out

# Streamlit App Layout
st.title("HealthBot - Your Personal Health Assistant")

# Chatbot interface using Streamlit's chat_input
if 'messages' not in st.session_state:
    st.session_state['messages'] = []  # To store chat history

# Display previous chat messages
for message in st.session_state['messages']:
    with st.chat_message(message['role']):
        st.write(message['content'])

# User input
user_message = st.chat_input("Ask me anything about health, wellness, or nutrition...")

if user_message:
    # Add user's message to chat history
    st.session_state['messages'].append({'role': 'user', 'content': user_message})
    with st.chat_message('user'):
        st.write(user_message)

    # Generate response from HealthBot
    with st.chat_message('assistant'):
        chatbot_output = generate_response_with_together(user_message)
        st.write(chatbot_output)

    # Add HealthBot's response to chat history
    st.session_state['messages'].append({'role': 'assistant', 'content': chatbot_output})

    # Suggest videos based on the health query
    video_links = search_videos(user_message, max_results=3)
    if video_links:
        with st.chat_message('assistant'):
            st.write("Here are some related videos you might find useful:")
            for link in video_links:
                st.markdown(f"- [{link}]({link})", unsafe_allow_html=True)
