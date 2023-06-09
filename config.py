# config.py

# Import required libraries
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Twilio API credentials
TWILIO_ACCOUNT_SID = os.getenv('TWILIO_ACCOUNT_SID', 'test_account_sid')
TWILIO_AUTH_TOKEN = os.getenv('TWILIO_AUTH_TOKEN', 'test_auth_token')

# Phone numbers
TWILIO_PHONE_NUMBER = os.getenv('TWILIO_PHONE_NUMBER', '+1234567890')
RECIPIENT_PHONE_NUMBER = os.getenv('RECIPIENT_PHONE_NUMBER', '+1234567890')

# Flask server configuration
FLASK_SERVER_HOST = os.getenv('FLASK_SERVER_HOST', '127.0.0.1')
FLASK_SERVER_PORT = int(os.getenv('SERVER_PORT', 5000))

# Miscellaneous configuration
WAIT_FOR_SERVER_TO_START = int(os.getenv('WAIT_FOR_SERVER_TO_START', 5))

#SMS Message Body
MESSAGE_BODY = os.getenv('MESSAGE_BODY', 'I Love you Heather')
