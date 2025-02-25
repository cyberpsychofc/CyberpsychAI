import time
import threading
import schedule
from flask import Flask
from tweet import tweet, reply

bot = Flask(__name__)
flag = True
@bot.route("/")
def home():
    return "CyberpsychAI is running!"

def tweet_job():
    global flag
    if flag:
        schedule.every(2).minutes.do(tweet)
        flag = False
    schedule.every(480).minutes.do(reply)
    while True:
        schedule.run_pending() 
        time.sleep(30)

if __name__ == "__main__":
    task = threading.Thread(target=tweet_job, daemon=True)
    task.start()
    bot.run(host="0.0.0.0", port=8000)