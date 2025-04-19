# Email Automation Bot

## Overview
This project automates sending random emails to recipients at a scheduled time. The bot uses **Gmail SMTP** and can be run locally or deployed to the cloud.

## Steps to Set Up

### Step 1: Clone the Repository
Clone the repository to your local machine:

```bash
git clone https://github.com/rishivennu/email-automation.git
cd email-automation

✅ Here's How to Generate Your Gmail App Password:
🔐 Step 1: Enable 2-Step Verification
Go to Google My Account – Security

Under “Signing in to Google”, enable 2-Step Verification

🔑 Step 2: Generate an App Password
After enabling 2FA, go back to Security

Under “Signing in to Google” → click App passwords

Sign in again if asked

Under “Select app” → choose Mail

Under “Select device” → choose Other and name it email-bot or anything

Click Generate

✅ Copy the 16-character password (looks like this):
nginx
Copy
Edit
abcd efgh ijkl mnop
Use this in your Python code as APP_PASSWORD (without spaces).

✉️ Final Integration Example in Code:
python
Copy
Edit
EMAIL = "yourgmail@gmail.com"
APP_PASSWORD = "abcdefghijklmnop"  # <-- This is your generated app password
