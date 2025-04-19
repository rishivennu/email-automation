# Email Automation Bot

## Overview
This project automates sending random emails to recipients at a scheduled time. The bot uses **Gmail SMTP** and can be run locally or deployed to the cloud.

## Steps to Set Up

### Step 1: Clone the Repository
Clone the repository to your local machine:

```bash
git clone https://github.com/rishivennu/email-automation.git
cd email-automation
Step 2: Install Python and Dependencies
Before you begin, ensure Python is installed on your machine. If you don’t have it installed, you can download and install Python from here.

Next, install the required dependencies for this project:

Open a terminal and navigate to the project folder where the requirements.txt file is located.

Run the following command to install the necessary Python libraries:

bash
Copy
Edit
pip install -r requirements.txt
This will install all the necessary packages, including yagmail (for sending emails) and schedule (for scheduling tasks).

Step 3: Set Up Gmail App Password
In order to use Gmail for sending emails through your Python script, you need to generate an App Password because Gmail requires 2-Step Verification to access Gmail via external apps.

1. Enable 2-Step Verification:
Go to Google My Account.

Under the Security tab, enable 2-Step Verification by following the on-screen instructions.

2. Generate an App Password:
After enabling 2FA, go back to the Security section in your Google account.

Under Signing in to Google, click on App passwords.

Sign in to your Google account again if prompted.

Under Select app, choose Mail.

Under Select device, choose Other and enter a name like email-bot.

Click Generate.

Copy the generated 16-character app password (e.g., abcd efgh ijkl mnop).

3. Use the App Password in Your Code:
Open the auto_email_sender.py file in your project.

Replace the APP_PASSWORD variable with the generated app password from the previous step:

python
Copy
Edit
EMAIL = "yourgmail@gmail.com"
APP_PASSWORD = "abcdefghijklmnop"  # <-- This is your generated app password
Step 4: Configure the Input Files
You need to configure two text files:

1. recipients.txt:
This file should contain one recipient email address per line. For example:

txt
Copy
Edit
email1@example.com
email2@example.com
email3@example.com
2. messages.txt:
This file should contain one message per line. For example:

txt
Copy
Edit
Hey there! Hope you're doing well 🌟
Just checking in, have a great day!
Did you smile today? 😊
Stay positive and awesome!
Step 5: Run the Automation Script
Now that everything is set up, you can run the automation script:

Open a terminal in the project folder.

Run the following command to start the script:

bash
Copy
Edit
python auto_email_sender.py
The script will send random emails to all the recipients listed in recipients.txt using one of the messages from messages.txt.

By default, the emails will be sent at 10:00 AM every day.

Step 6: Optional - Deploying to the Cloud
If you want to deploy the automation to the cloud, you can choose a platform like Heroku, AWS, or any other service that supports running Python scripts.

1. Prepare for Deployment:
Make sure your auto_email_sender.py, recipients.txt, messages.txt, and requirements.txt are included in your project directory.

Create a Procfile for Heroku deployment:

bash
Copy
Edit
worker: python auto_email_sender.py
2. Deploy on Heroku:
Install the Heroku CLI.

Log in to your Heroku account:

bash
Copy
Edit
heroku login
Create a new Heroku app:

bash
Copy
Edit
heroku create
Push your code to Heroku:

bash
Copy
Edit
git push heroku main
Once the deployment is complete, Heroku will run the script at the scheduled time.

Conclusion
You have now set up the email automation bot to send random emails to your recipients at a scheduled time. Optionally, you can deploy it to the cloud for continuous operation.

pgsql
Copy
Edit







