import os
import yagmail
import random
import time

EMAIL = os.environ.get("EMAIL")
APP_PASSWORD = os.environ.get("APP_PASSWORD")

yag = yagmail.SMTP(EMAIL, APP_PASSWORD)

def load_data(file_path):
    with open(file_path, "r") as file:
        return [line.strip() for line in file if line.strip()]

def send_random_email():
    recipients = load_data("recipients.txt")
    subjects = load_data("subjects.txt")
    messages = load_data("messages.txt")

    recipient = random.choice(recipients)
    subject = random.choice(subjects)
    body = random.choice(messages)

    yag.send(to=recipient, subject=subject, contents=body)
    print(f"Email sent to {recipient} with subject: {subject}")

send_random_email()
