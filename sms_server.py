# sms_server.py

from flask import Flask, request, jsonify
from twilio.rest import Client
from config import *
import re

app = Flask(__name__)

# Function to create Twilio client
def create_twilio_client():
    return Client(TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN)

client = create_twilio_client()

# Function to validate phone numbers
def is_valid_phone_number(number):
    return re.fullmatch(r'^\+\d{1,3}\d{1,14}$', number)

# Route for sending SMS
@app.route('/send_sms', methods=['POST'])
def send_sms():
    to = request.form['To']
    from_number = request.form['From']
    body = request.form['Body']

    # Validate phone numbers and message body
    if not (is_valid_phone_number(to) and is_valid_phone_number(from_number)):
        return jsonify({'error': 'Invalid phone number'}), 400
    if not (1 <= len(body) <= 1600):
        return jsonify({'error': 'Invalid message body'}), 400

    try:
        message = client.messages.create(
            body=body,
            from_=from_number,
            to=to
        )
        return jsonify({'message': 'SMS sent'}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(host=FLASK_SERVER_HOST, port=FLASK_SERVER_PORT)