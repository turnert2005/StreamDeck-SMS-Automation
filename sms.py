import requests
import logging
import config
from twilio.rest import Client
import phonenumbers

# Function to create Twilio client
def create_twilio_client():
    return Client(config.TWILIO_ACCOUNT_SID, config.TWILIO_AUTH_TOKEN)

client = create_twilio_client()

# Function to validate phone numbers
def is_valid_phone_number(number):
    try:
        parsed_number = phonenumbers.parse(number, None)
        return phonenumbers.is_valid_number(parsed_number)
    except phonenumbers.NumberParseException:
        return False

# Send an SMS using Twilio API
def send_sms():
    payload = {
        'To': config.RECIPIENT_PHONE_NUMBER,
        'From': config.TWILIO_PHONE_NUMBER,
        'Body': config.MESSAGE_BODY
    }
    response = requests.post(
        f"https://api.twilio.com/2010-04-01/Accounts/{config.TWILIO_ACCOUNT_SID}/Messages.json",
        auth=(config.TWILIO_ACCOUNT_SID, config.TWILIO_AUTH_TOKEN),
        data=payload
    )
    logging.info(f"Twilio API response status code: {response.status_code} ({requests.status_codes._codes[response.status_code][0]})")
    logging.info(f"Twilio API response text: {response.text.replace('\n', '')}")
    return response
