from flask import Flask, request
from twilio.twiml.messaging_response import MessagingResponse
from google.generativeai import GenerativeModel, GenerationConfig  
import google.generativeai as genai
app = Flask(__name__)

gemini_api_key = 'YOUR_GEMINI_API_KEY'

@app.route("/", methods=["GET"])
def index():
    return "Flask WhatsApp Bot is running!"

@app.route("/whatsapp", methods=["POST"])
def whatsapp():
    incoming_msg = request.values.get("Body", "").strip()
    resp = MessagingResponse()
    msg = resp.message()

    if incoming_msg.lower() == "hi" or incoming_msg.lower() == "hello":
        msg.body("Hello! Send me an article number or text from the Indian Constitution, and I'll explain it for you.")
    elif incoming_msg.lower() == "bye":
        msg.body("Goodbye! Feel free to message me anytime.")
    else:
        msg.body("Generating your Article. Please wait...")
        story = generate_article(incoming_msg)  # function call for article generation
        msg.body(story)

    return str(resp)

def generate_article(article_text):

    genai.configure(api_key="YOUR_GEMINI_API_KEY")
    model = genai.GenerativeModel("gemini-1.5-flash")
    article_text+=" In Only Indian Constitution."
    prompt = f"Explain the Indian Constitutional article {article_text}. Keep the language simple and include a short summary at the end. Limit this to only indian constitution."

    try:
        response = model.generate_content([article_text])
        return response.text.strip() if response.text else "Failed to generate article."
    except Exception as e:
        return f"Error generating article: {e}"


if __name__ == "__main__":
    app.run(debug=True)
