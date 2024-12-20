from flask import Flask, request
from twilio.twiml.messaging_response import MessagingResponse
from google.generativeai import GenerativeModel, GenerationConfig  # Ensure this import is correct
import google.generativeai as genai
app = Flask(__name__)

gemini_api_key = 'AIzaSyAiiK5e3IczRDfbb-wz59_m2x0XQ12Vnno'

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
        story = generate_story(incoming_msg)  # Call to the function for story generation
        msg.body(story)

    return str(resp)

def generate_story(article_text):

    genai.configure(api_key="AIzaSyAiiK5e3IczRDfbb-wz59_m2x0XQ12Vnno")
    model = genai.GenerativeModel("gemini-1.5-flash")
    article_text+=" In Only Indian Constitution."
    prompt = f"Create an Indian Constitutional story based on the article {article_text}. Keep the language simple and include a short summary at the end. create a intresting and attractive story to understand that indian article. Limit this to only indian constitution."

    try:
        response = model.generate_content([article_text])
        return response.text.strip() if response.text else "Failed to generate story."
    except Exception as e:
        return f"Error generating story: {e}"


if __name__ == "__main__":
    app.run(debug=True)
