import yagmail
import random
import time

EMAIL = "your@gmail.com"  # Replace with your email
APP_PASSWORD = "your password"  # Replace with your app password

# Load recipients and messages
def load_data(file_path):
    with open(file_path, 'r') as file:
        return [line.strip() for line in file if line.strip()]

recipients = load_data('recipients.txt')
messages = load_data('messages.txt')

# Send a random email
def send_random_email():
    yag = yagmail.SMTP(EMAIL, APP_PASSWORD)
    for recipient in recipients:
        subject = "A little note for you ✨"
        body = random.choice(messages)
        yag.send(to=recipient, subject=subject, contents=body)
        print(f"[SENT] Email to {recipient}")
    print("✅ All emails sent!")

# Call the send_random_email() function once
send_random_email()
