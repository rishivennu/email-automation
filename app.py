from flask import Flask, render_template, request, redirect, url_for
import yagmail
import random
import os
import schedule
import time
import threading

app = Flask(__name__)

EMAIL = "youremail@gmail.com"
APP_PASSWORD = "your_app_password"

# Load recipients and messages
def load_data(file_path):
    with open(file_path, 'r') as file:
        return [line.strip() for line in file if line.strip()]

# Email sending logic
def send_random_email():
    yag = yagmail.SMTP(EMAIL, APP_PASSWORD)
    for recipient in recipients:
        subject = "Hello from the Bot 🤖"
        body = random.choice(messages)
        yag.send(to=recipient, subject=subject, contents=body)
        print(f"Email sent to {recipient}")

# Run the email sending task in the background
def run_email_sender():
    while True:
        schedule.run_pending()
        time.sleep(60)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload_files():
    if 'recipients_file' not in request.files or 'messages_file' not in request.files:
        return redirect(request.url)
    
    recipients_file = request.files['recipients_file']
    messages_file = request.files['messages_file']
    
    # Save files to disk
    recipients_file.save(os.path.join('recipients.txt'))
    messages_file.save(os.path.join('messages.txt'))
    
    # Reload recipients and messages after upload
    global recipients, messages
    recipients = load_data('recipients.txt')
    messages = load_data('messages.txt')
    
    return redirect(url_for('index'))

@app.route('/start-sending', methods=['POST'])
def start_sending():
    # Schedule email sending
    schedule.every().day.at("10:00").do(send_random_email)
    # Start background thread for email sending
    threading.Thread(target=run_email_sender, daemon=True).start()
    
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
