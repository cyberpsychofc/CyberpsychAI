import time
import threading
from flask import Flask
from tweet import tweet

bot = Flask(__name__)

@bot.route("/")
def home():
    return "CyberpsychAI is running!"

def background_task():
    while True:
        tweet()
        time.sleep(6000)
thread = threading.Thread(target=background_task, daemon=True)
thread.start()

if __name__ == "__main__":
    bot.run(host="0.0.0.0", port=8000) 