import time
import threading
import schedule
from flask import Flask
from tweet import tweet, reply

bot = Flask(__name__)

@bot.route("/")
def home():
    return "CyberpsychAI is running!"

def tweet_job():
    schedule.every(120).minutes.do(tweet)
    schedule.every(480).minutes.do(reply)
    while True:
        schedule.run_pending() 
        time.sleep(30)

if __name__ == "__main__":
    task = threading.Thread(target=tweet_job, daemon=True)
    task.start()
    bot.run(host="0.0.0.0", port=8000)