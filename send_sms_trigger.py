# send_sms_trigger.py

import time
import threading
import tkinter as tk
from tkinter import messagebox

import requests
from flask import Flask

import config

app = Flask(__name__)

# A flag to keep track of the server status
server_started = False


# A function that runs the Flask server
def run_server():
    global server_started
    app.run(host=config.FLASK_SERVER_HOST, port=config.FLASK_SERVER_PORT)
    server_started = True


# Check if the Flask server is running
def is_server_running():
    return server_started


# Start the Flask server
def start_server():
    server_thread = threading.Thread(target=run_server)
    server_thread.daemon = True
    server_thread.start()


# Send an SMS using the Flask server
def send_sms():
    payload = {
        'To': config.RECIPIENT_PHONE_NUMBER,
        'From': config.TWILIO_PHONE_NUMBER,
        'Body': 'I Love you Heather'
    }
    response = requests.post(
        f"http://{config.FLASK_SERVER_HOST}:{config.FLASK_SERVER_PORT}/send_sms",
        auth=(config.TWILIO_ACCOUNT_SID, config.TWILIO_AUTH_TOKEN),
        data=payload
    )
    return response


# Display a message box with the given title and text
def show_tkinter_message_box(title, text):
    root = tk.Tk()
    root.withdraw()  # Hide the main window
    messagebox.showinfo(title, text)
    root.destroy()  # Close the hidden main window


def main():
    status_messages = 'Stream Deck button pressed. Trigger initiated.\n'
    if is_server_running():
        status_messages += 'Flask server is already running.\n'
    else:
        status_messages += 'Flask server is not running. Starting server...\n'
        start_server()
        time.sleep(config.WAIT_FOR_SERVER_TO_START)  # Wait for the server to start
        status_messages += 'Flask server started.\n'

    response = send_sms()

    if response.status_code == 200:
        status_messages += 'The SMS was sent successfully!\n'
    else:
        status_messages += 'Failed to send the SMS.\n'

    show_tkinter_message_box('SMS Status', status_messages)


if __name__ == '__main__':
    main()