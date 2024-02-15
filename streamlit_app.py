import streamlit as st
from transformers import pipeline
from youtube_search import YoutubeSearch

# Initialize the Hugging Face pipeline for text generation, using GPT-2 for example
generator = pipeline('text-generation', model='gpt2')

# Function to generate response using Hugging Face pipeline
def generate_response(prompt):
    response = generator(prompt, max_length=150, num_return_sequences=1, truncation=True)
    return response[0]['generated_text'].strip()

# Function to perform YouTube search and retrieve video links
def search_videos(query, max_results=5):
    try:
        results = YoutubeSearch(query, max_results=max_results).to_dict()
        video_links = [f"https://www.youtube.com/watch?v={result['id']}" for result in results]
        return video_links
    except Exception as e:
        st.error("An error occurred while searching for videos: " + str(e))
        return []

# Streamlit App Layout
st.title("FitPal: Interactive Fitness Coach")

# Input fields
client_info = st.text_area("Talk with Fit", help="Enter your message here")
user_message = st.text_input("Client Info", help="Enter your height, age, weight, etc. for better personalized results")
video_query = st.text_input("Search for Video", help="Want to look up a video that explains more?")

# Button to generate response
if st.button("Submit"):
    if user_message:
        prompt = user_message + "\nClient Info: " + client_info
        chatbot_output = generate_response(prompt)
        st.write("Chatbot Response:")
        st.write(chatbot_output)

    if video_query:
        video_links = search_videos(video_query)
        if video_links:
            st.write("Video Links:")
            for link in video_links:
                st.markdown(f"[{link}]({link})", unsafe_allow_html=True)

