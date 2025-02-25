import time
import threading
import schedule
from flask import Flask
from tweet import tweet, reply

bot = Flask(__name__)

# Free-tier sends atmost of 17 requests a day, so plan
post_times = ["09:39"]
roast_times = ["09:42"]

@bot.route("/")
def home():
    return "CyberpsychAI is running!"

def run_scheduler():
    while True:
        schedule.run_pending()
        time.sleep(30)

def tweet_job():
    for post in post_times:
        schedule.every().day.at(post).do(tweet)
    for roast in roast_times:
        schedule.every().day.at(roast).do(reply)

@bot.before_first_request
def start_scheduler():
    tweet_job()
    task = threading.Thread(target=run_scheduler, daemon=True)
    task.start()

if __name__ == "__main__":
    bot.run(host="0.0.0.0", port=8000)