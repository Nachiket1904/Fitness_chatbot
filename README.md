# FitPal: Interactive Fitness Coach

FitPal is an innovative chatbot designed to act as your personal fitness coach. Leveraging the power of advanced AI, FitPal offers workout advice, exercise recommendations, and video demonstrations, making it easier than ever to achieve your fitness goals.

## Features

### Engage with Your Personal Fitness Coach:
Chat with FitPal for personalized advice on your workout routines. Utilizing OpenAI's advanced text generation models, FitPal provides you with insights and guidance tailored to your fitness journey.

### Tailored Fitness Guidance:
Share details such as your height, age, weight, and fitness goals to receive custom workout recommendations designed just for you.

### Explore Video Demonstrations:
For visual learners or those seeking detailed exercise instructions, FitPal can search for and provide YouTube video links to ensure you have the best information at your fingertips.

## How It Works

FitPal is powered by advanced AI models using the Together API. Here's how it operates:

1. **Natural Language Understanding**: 
   - **Tag**: #NLU
   - Description: FitPal leverages Together's state-of-the-art language models to understand user inputs and generate contextually appropriate responses.

2. **Custom Prompt Design**:
   - **Tag**: #PromptEngineering
   - Description: A carefully crafted system prompt sets the tone for FitPal to focus on fitness and health guidance.

3. **YouTube Integration**:
   - **Tag**: #YouTubeSearch
   - Description: FitPal uses the `youtube-search` library to fetch relevant exercise and fitness videos from YouTube, providing users with additional learning resources.

4. **Streamlit for Interface**:
   - **Tag**: #UserInterface
   - Description: The chatbot interface is built using Streamlit, ensuring a user-friendly and interactive experience.

The Together API enables FitPal to dynamically generate fitness guidance based on user queries. By combining AI-powered text generation with YouTube video searches, FitPal ensures a holistic approach to fitness coaching.

## Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/fitpal.git
   cd fitpal
   ```

2. Create a virtual environment and activate it:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows, use venv\Scripts\activate
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Create a `.env` file in the root directory and add the following:
   ```plaintext
   TOGETHER_API_KEY=your_api_key_here
   ```

## Usage
Run the application with Streamlit:
```bash
streamlit run main.py
```

## Notes
- Make sure to replace `your_api_key_here` in the `.env` file with your actual Together API key.
- The `.env` file should not be shared or pushed to GitHub to keep your API key secure.

## License
This project is licensed under the MIT License.

