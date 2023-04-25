import time
import threading
import tkinter as tk
from tkinter import messagebox
import logging
import config
from server import start_server, is_server_running
from sms import send_sms, is_valid_phone_number

# Configure logging
logging.basicConfig(filename='sms.log', level=logging.INFO, format='%(asctime)s %(levelname)s: %(message)s')

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

    if is_valid_phone_number(config.RECIPIENT_PHONE_NUMBER):
        response = send_sms()

        if response.status_code == 201:
            status_messages += 'The SMS was sent successfully!\n'
        else:
            status_messages += 'Failed to send the SMS.\n'
    else:
        status_messages += 'The recipient phone number is not valid.\n'

    show_tkinter_message_box('SMS Status', status_messages)

if __name__ == '__main__':
    main()
