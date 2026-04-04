# Import necessary libraries
from flask import Flask, request, render_template, redirect #pip install flask
from groq import Groq #pip install groq
import json #built in


# Create Flask app instance
app = Flask(__name__)

# Initialize Groq client with your API key
client = Groq(api_key="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")

chat_history = [] # store chat history

# default message to display
chat_history.append({
    "role": "assistant",
    "content": "Hello! Welcome to our hotel chat. How can I assist you today?"
})

# Function to load hotel information from JSON file
def get_hotel_info():
    with open("hotel_info.json", "r") as f:
        hotel_data = json.load(f)  # Load JSON data as Python dictionary
    return hotel_data

# Load hotel data once when the app starts
hotel_data = get_hotel_info()

# Convert hotel dictionary to readable text for AI system prompt
info_text = "\n".join([f"{k}: {v}" for k, v in hotel_data.items()])

# Function to ask AI a question and get a response
def ask_ai(question):
  
    system_prompt = (
    "You are a hotel assistant chatbot.\n"
    "Your task is to answer user queries ONLY using the provided hotel information.\n\n"
    
    "Rules:\n"
    "1. Use only the given hotel data to answer.\n"
    "2. If exact information is not available, give a smart response based on related data.\n"
    "3. If no related information exists, politely say you are not sure and suggest contacting the hotel.\n"
    "4. Keep answers very short, clear, and helpful.\n"
    "5. Do NOT make up facts or add external information.\n"
    "6. Only respond to hotel-related queries.\n\n"
    
    "Response Style:\n"
    "- Be polite and professional.\n"
    "- If partial info is available, mention what is known and guide the user.\n"
    "- Example: 'We don’t have exact details, but based on our services...'\n\n"
    
    "Hotel Information:\n"
    f"{info_text}"
)
    try:
        # Send request to Groq AI chat model
        response = client.chat.completions.create(
            model="llama-3.1-8b-instant",
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": question}
            ]
        )
        # Return AI's answer
        return response.choices[0].message.content
    except Exception as e:
        # Return error message if something goes wrong
        return f"Error: {str(e)}"

# Define route for home page
@app.route('/', methods=['GET', 'POST'])
def home():
    """
    This function handles requests to the root URL '/'.
    - GET request: Display the chat page.
    - POST request: Get user input from form, ask AI, and show reply.
    """
    ai_reply = None  # Initialize AI reply
    user_message = None  # Initialize user message

    if request.method == 'POST':

        global chat_history
        # If form is submitted
        user_message = request.form['message']  # Get message from form input

        chat_history.append({"role": "user", "content": user_message})

        ai_reply = ask_ai(user_message)  # Get AI response
        
        chat_history.append({"role": "assistant", "content": ai_reply})

    # Render HTML template with user message and AI reply
    return render_template('index.html', chat_history = chat_history)


@app.route('/clear', methods=['POST'])
def clear():
    global chat_history
    chat_history.clear()

    # default message to display
    chat_history.append({
        "role": "assistant",
        "content": "Hello! Welcome to our hotel chat. How can I assist you today?"
    })  
    return redirect('/')

# Run the Flask app
if __name__ == '__main__':
    # Start development server on localhost:8000
    app.run(debug=True, host="127.0.0.1", port=8000)