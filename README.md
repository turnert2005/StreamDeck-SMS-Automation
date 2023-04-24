
# Stream Deck SMS

Stream Deck SMS is a Python-based application that enables you to send SMS messages using your Elgato Stream Deck. The application uses the Twilio API to send SMS messages, and it allows you to configure the message recipient, message body, and Twilio account credentials directly from your Stream Deck.

## Installation

To use Stream Deck SMS, you must have Python 3.6 or later installed on your system. You can download the latest version of Python from the official website.

Once you have installed Python, clone the repository and navigate to the project directory. Run the following command to install the required Python packages:

```
python dependencies.py
```

This will check for and install any missing required Python packages for Stream Deck SMS.

## Configuration

Before you can use Stream Deck SMS, you must configure the Twilio API credentials and phone numbers for the sender and recipient. You can configure these settings in the `.env` file. If you don't have an `.env` file, create one in the project directory and add the following content:

```
TWILIO_ACCOUNT_SID=your_account_sid_here
TWILIO_AUTH_TOKEN=your_auth_token_here
TWILIO_PHONE_NUMBER=your_twilio_phone_number_here
RECIPIENT_PHONE_NUMBER=recipient_phone_number_here
FLASK_SERVER_HOST=127.0.0.1
FLASK_SERVER_PORT=5000
WAIT_FOR_SERVER_TO_START=5
```

Replace the placeholder values with your actual Twilio API credentials and phone numbers.

## Usage

To use Stream Deck SMS, simply run the `send_sms_trigger.py` file using Python:

```
python send_sms_trigger.py
```

This will start the Flask server, send an SMS, and display the status of the SMS in a tkinter message box.

You can then create a new Stream Deck button that executes the `send_sms_trigger.py` script to send an SMS message.

## Contributing

If you find a bug or have a feature request, please create a new issue on the GitHub repository. Pull requests are also welcome!

## License

Stream Deck SMS is licensed under the MIT License. See the `LICENSE` file for more information.
```

This updated `README.md` reflects the changes made to the code organization, the new `.env` file for configuration, and the updated method of installing required packages.