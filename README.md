# AI Chatbot with Streamlit and Together AI

A simple chatbot application built with Streamlit that uses Together AI's API to provide intelligent responses.

## Features

- Clean and intuitive chat interface
- Real-time conversation with AI
- Chat history management
- Clear chat functionality
- Responsive design

## Setup

1. **Clone the repository**
   ```bash
   git clone <your-repo-url>
   cd deployagenticai
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Set up environment variables**
   - Copy `.env.example` to `.env`
   - Add your Together AI API key:
   ```bash
   TOGETHER_API_KEY=your_actual_api_key_here
   ```
   
   Or set it as a system environment variable:
   ```bash
   # Windows PowerShell
   $env:TOGETHER_API_KEY="your_actual_api_key_here"
   
   # Windows Command Prompt
   set TOGETHER_API_KEY=your_actual_api_key_here
   ```

4. **Run the application**
   ```bash
   streamlit run app.py
   ```

## Usage

1. Open your browser and navigate to the URL shown in the terminal (usually `http://localhost:8501`)
2. Type your message in the chat input at the bottom
3. Press Enter to send your message and receive an AI response
4. Use the "Clear Chat History" button in the sidebar to start a new conversation

## API Key Setup

To get your Together AI API key:

1. Visit [Together AI](https://together.ai/)
2. Sign up for an account
3. Navigate to your API settings
4. Generate a new API key
5. Add it to your environment variables

## Model Information

This chatbot uses the `google/gemma-2-9b-it` model from Together AI, which provides:
- High-quality conversational responses
- Good performance for general chat applications
- Reasonable response times

## Deployment

This application can be deployed on various platforms:

- **Streamlit Cloud**: Push to GitHub and deploy directly
- **Heroku**: Use the included requirements.txt
- **Docker**: Create a Dockerfile for containerized deployment
- **Local**: Run locally for development and testing

## Contributing

Feel free to submit issues and enhancement requests!

## License

This project is open source and available under the [MIT License](LICENSE).