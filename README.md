# Stream Deck SMS

Stream Deck SMS is a Python-based application that enables you to send SMS messages using your Elgato Stream Deck. The application uses the Twilio API to send SMS messages, and it allows you to configure the message recipient, message body, and Twilio account credentials directly from your Stream Deck.

## Installation

To use Stream Deck SMS, you must have Python 3.6 or later installed on your system. You can download the latest version of Python from the official website.

Once you have installed Python, you can install the required Python packages using pip, the Python package manager. Open a command prompt or terminal and run the following command:

```
pip install -r requirements.txt
```

This will install all the required Python packages for Stream Deck SMS.

## Configuration

Before you can use Stream Deck SMS, you must configure the Twilio API credentials and phone numbers for the sender and recipient. You can configure these settings in the `config.py` file.

```python
# Twilio API credentials
TWILIO_ACCOUNT_SID = 'your_account_sid_here'
TWILIO_AUTH_TOKEN = 'your_auth_token_here'

# Phone numbers
TWILIO_PHONE_NUMBER = 'your_twilio_phone_number_here'
RECIPIENT_PHONE_NUMBER = 'recipient_phone_number_here'

# Flask server configuration
FLASK_SERVER_HOST = '127.0.0.1'
FLASK_SERVER_PORT = 5000

# Miscellaneous configuration
WAIT_FOR_SERVER_TO_START = 5
```

Replace the placeholder values with your actual Twilio API credentials and phone numbers.

## Usage

To use Stream Deck SMS, simply run the `sms_server.py` file using Python:

```
python sms_server.py
```

This will start the Flask server and make it available at `http://127.0.0.1:5000`.

You can then create a new Stream Deck button that sends an HTTP POST request to the Flask server with the message body as the POST data. Here is an example of how to send a message using Python's `requests` library:

```python
import requests

url = 'http://127.0.0.1:5000/send-sms'
data = {
    'message': 'Hello, World!'
}
response = requests.post(url, data=data)
```

## Contributing

If you find a bug or have a feature request, please create a new issue on the GitHub repository. Pull requests are also welcome!

## License

Stream Deck SMS is licensed under the MIT License. See the `LICENSE` file for more information.