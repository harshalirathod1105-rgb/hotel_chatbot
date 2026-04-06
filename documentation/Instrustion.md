⚙️ Installation Guide
🤖 Hotel FAQ Chatbot

⸻

📌 Prerequisites

Make sure the following are installed:
• Python (3.8 or above)
• pip (Python package manager)
• Web Browser (Chrome/Edge)
• Git (optional)

⸻

📥 Step 1: Clone Repository

Clone the project using Git: https://github.com/harshalirathod1105-rgb/hotel_chatbot.git
OR
Download ZIP and extract the project folder

⸻

📁 Step 2: Open Project Folder

Navigate to the project directory: cd hotel_chatbot

⸻

🧪 Step 3: Create Virtual Environment
For Windows:
python -m venv env
env\Scripts\activate

⸻

📦 Step 4: Install Dependencies
pip install -r requirements.txt

⸻

🔑 Step 5: Configure API Key
Create a .env file in the root folder
Add your Groq API key:
GROQ_API_KEY=your_api_key_here

⚠️ Replace with your actual API key

⸻

📊 Step 6: Add Hotel Data

Ensure your JSON file (e.g., hotel_data.json) is present

Example:

{
  "name": "Hotel Sunshine",
  "services": ["WiFi", "Parking", "Room Service"]
}

⸻

▶️ Step 7: Run Project
python app.py

⸻

🌐 Access the Application

Open browser and go to:

http://127.0.0.1:8000/

⸻

🛠️ Troubleshooting

• Python not recognized → Install Python & add to PATH
• Module not found → Run pip install -r requirements.txt
• API error → Check API key
• No chatbot response → Verify JSON data & backend logs

⸻

✅ System Ready

Your chatbot should now be running successfully 🎉