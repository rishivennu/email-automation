from flask import Flask, render_template_string
import yagmail
import random

app = Flask(__name__)

EMAIL = "your@gmail.com"
APP_PASSWORD = "your_app_password"

recipients = ["example1@gmail.com", "example2@gmail.com"]
subjects = ["Good morning", "Hello!", "Just checking in"]
messages = [
    "Hope you have a great day!",
    "Don't forget to smile 😊",
    "Stay awesome!"
]

def send_random_email():
    recipient = random.choice(recipients)
    subject = random.choice(subjects)
    body = random.choice(messages)

    yag = yagmail.SMTP(EMAIL, APP_PASSWORD)
    yag.send(to=recipient, subject=subject, contents=body)
    return f"Email sent to {recipient} with subject: {subject}"

@app.route("/")
def home():
    return render_template_string("""
        <h2>📬 Email Sender Dashboard</h2>
        <a href='/send'><button>Send Random Email</button></a>
    """)

@app.route("/send")
def send():
    result = send_random_email()
    return f"<p>{result}</p><a href='/'>Go back</a>"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
