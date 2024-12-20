# WhatsApp-Bot-for-Indian-Constitutional-Articles

This is a Flask-based WhatsApp bot that generates information about articles from the Indian Constitution. The bot uses the Google Gemini API for article generation and is accessible via WhatsApp. Ngrok is used to expose the local server to the internet.

## Features
Generate information about Indian Constitution articles with simple and easy-to-understand language.
Provides a short summary for better comprehension.
Supports basic interactions like greetings and farewells.
Easy to set up locally with Ngrok for quick deployment.

## Prerequisites
Python 3.10+
Ngrok (for exposing local server to the internet)
Twilio account for WhatsApp messaging.
Google Gemini API key for story generation.

## Installation
### 1. Clone the Repository
git clone https://github.com/KoradaCharan/WhatsApp-Bot-for-Indian-Constitutional-Articles.git  
cd WhatsApp-Bot-for-Indian-Constitutional-Articles

### 2. Set Up Virtual Environment
#### Create a virtual environment:
python -m venv venv  

#### Activate the virtual environment:

Windows:
venv\Scripts\activate  

macOS/Linux:
source venv/bin/activate  

#### Install the required dependencies:
pip install -r requirements.txt  

## Configuration
### 1. Add API Key
Replace the placeholder gemini_api_key in the code with your Google Gemini API key.
gemini_api_key = 'YOUR_GOOGLE_API_KEY'

### 2. Set Up Twilio
Create a Twilio account.
Configure the Sandbox for WhatsApp messaging.
Copy your Ngrok URL and set it as the Webhook URL in the Twilio console under the WhatsApp sandbox configuration.

## Running the Project
### 1. Start the Flask Server
Run the Flask app to start the WhatsApp bot:
python app.py  

### 2. Start Ngrok
Expose your local Flask server using Ngrok:
ngrok http 5000  
Copy the Ngrok HTTPS URL and update it in the Twilio WhatsApp sandbox configuration as the webhook URL.

### Example Interactions
User: "Hi"
Bot: "Hello! Send me an article number or text from the Indian Constitution, and I'll create a story for you."
User: "Tell me about Article 21 please"
Bot: "Article 21 ensures the right to life and personal liberty. It protects individuals from any action that infringes on this right except under the procedure established by law."
User: "Bye"
Bot: "Goodbye! Feel free to message me anytime."

## Dependencies
Make sure the following dependencies are installed (defined in requirements.txt):

Flask
Twilio
Google Generative AI SDK
Install them using:
pip install -r requirements.txt 
 
## Deployment
The bot is deployed locally using Flask, and Ngrok is used to make it accessible over the internet. Follow the steps in the Running the Project section to deploy it successfully.

