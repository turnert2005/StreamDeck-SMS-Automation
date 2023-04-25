from flask import Flask
from config import SERVER_HOST, SERVER_PORT

app = Flask(__name__)

# A flag to keep track of the server status
server_started = False

# A function that runs the Flask server
def run_server():
    global server_started
    app.run(host=SERVER_HOST, port=SERVER_PORT)
    server_started = True

# Check if the Flask server is running
def is_server_running():
    return server_started

# Start the Flask server
def start_server():
    server_thread = threading.Thread(target=run_server)
    server_thread.daemon = True
    server_thread.start()
