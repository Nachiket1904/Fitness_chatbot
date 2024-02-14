# FitPal: Interactive Fitness Coach
FitPal is an innovative chatbot designed to act as your personal fitness coach. Leveraging the power of advanced AI, FitPal offers workout advice, exercise recommendations, and video demonstrations, making it easier than ever to achieve your fitness goals.

## Features
### Engage with Your Personal Fitness Coach:
Chat with FitPal for personalized advice on your workout routines. Utilizing OpenAI's advanced text generation models, FitPal provides you with insights and guidance tailored to your fitness journey.

### Tailored Fitness Guidance:
Share details such as your height, age, weight, and fitness goals to receive custom workout recommendations designed just for you.

### Explore Video Demonstrations:
For visual learners or those seeking detailed exercise instructions, FitPal can search for and provide YouTube video links to ensure you have the best information at your fingertips.

## Installation

### Clone the Repository

Start by cloning the FitPal repository to your local machine:

```bash
git clone https://github.com/YourUsername/FitPal-Interactive-Fitness-Coach.git
cd FitPal-Interactive-Fitness-Coach
```

### Install Dependencies
Install all necessary libraries by running:

```bash
pip install -r requirements.txt
```

### Launch FitPal
Begin your fitness journey with FitPal:

```bash
streamlit run fitpal.py
```
## How to Use FitPal
- **Starting the Conversation**: Initiate your dialogue with FitPal by entering your query in the "Talk with Fit" section for instant fitness advice.
- **Personalizing Your Experience**: Provide your personal details in the "Client Info" section to receive workout recommendations that meet your specific needs.
- **Finding Instructional Videos**: Input your video request in the "Search for Video" section to have FitPal find relevant YouTube videos for you.
- **Viewing Responses and Videos**: Interact with FitPal's advice and the video links provided directly within the Streamlit app interface.

### Examples
FitPal comes with a variety of example prompts to help you get started. These examples cover common fitness queries to demonstrate how you can interact with the chatbot for insights and guidance.

### License
This project is made available under the MIT License. For more details, see the LICENSE file.

## Acknowledgments

FitPal is powered by the following technologies:

- **Hugging Face's Transformers**: Utilized for generating personalized fitness advice through the pretrained GPT-2 model.
- **Streamlit**: Employed to create an engaging web app interface for user interactions.
- **Youtube-Search-Python**: Integrated for seamless searching and retrieval of instructional fitness videos on YouTube.