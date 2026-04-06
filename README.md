🏨 Hotel FAQ Chatbot
A smart AI-powered chatbot designed to answer hotel-related queries instantly using structured data and natural language processing.

______________

📌 Project Overview
The Hotel FAQ Chatbot is a web-based application that allows users to interact with a chatbot to get information about a hotel. The chatbot intelligently responds to user queries by analyzing hotel data stored in a JSON file and generating smart responses using AI.

___________

🔄 Project Flow
User opens the chatbot interface
User asks queries related to the hotel (services, features, etc.)
Backend processes the query using AI
AI analyzes hotel data from a JSON file
Smart response is generated and sent back
User sees the response on the screen

___________

🛠️ Tech Stack
Python – Backend logic
Flask – Web framework
Groq API – AI model integration
LLaMA 3.1 (8B Instant) – AI model for generating responses
JSON – Data storage for hotel information

____________

✨ Features
🚫 No login or signup required
🏨 Handles only hotel-related queries
🤖 AI-powered smart responses
📂 Uses JSON-based data for accurate answers
💬 Chat history support for better conversations
🧹 Option to clear chat
⏰ 24/7 availability

_____________

📁 Project Structure

hotel-faq-chatbot/
│
├── app.py                 # Main Flask application and logic
├── templates/            # HTML files
├── static/               # CSS, JS files
├── hotel_data.json       # Hotel information
├── requirements.txt      # Dependencies
└── README.md             # Project documentation

_______________

⚙️ Installation & Setup

1. Clone the repository: https : //github.com/harshalirathod1105-rgb/hotel_chatbot.git
2. Create virtual environment : python -m venv env
3. Activate virtual environment : env\Scripts\activate
4. Install dependencies : pip install -r requirements.txt
5. Add your Groq API key
Create a .env file and add: GROQ_API_KEY=your_api_key_here
6. Run the application:
python app.py
7. Open in browser: 127.0.0.1:8000

_______________

💡 Usage
Ask questions like:
"What services does the hotel offer?"
"Do you have free Wi-Fi?"
"What are check-in and check-out times?"
The chatbot will respond based on hotel data and AI understanding.

_________________

🔒 Limitations
Only answers hotel-related queries
Depends on accuracy of JSON data
Requires internet for AI API

________________

🚀 Future Improvements
Add multi-language support
Voice-based interaction
Admin panel to update hotel data
Integration with booking system

__________________

👩‍💻 Author

Harshali Rathod and supporting team

_________________


📄 License

This project is created for educational purposes only.
Permission is granted to use, copy, modify, and distribute this project for learning and academic use.

However:
❌ Commercial use is not allowed
❌ This project should not be used for production or business purposes
❌ Proper credit must be given to the original author



