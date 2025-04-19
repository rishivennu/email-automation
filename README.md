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
