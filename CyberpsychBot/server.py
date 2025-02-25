import time
import threading
import schedule
from flask import Flask
from tweet import tweet, reply

bot = Flask(__name__)

# Free-tier sends atmost of 17 requests a day, so plan
post_times = ["06:00","08:00","10:00","12:00","14:00","16:00"]  # Instance timezone is UTC
#roast_times = ["05:31"]

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
    '''
    for roast in roast_times:
        schedule.every().day.at(roast).do(reply)   
    '''

if __name__ == "__main__":
    tweet_job()
    task = threading.Thread(target=run_scheduler, daemon=True)
    task.start()
    bot.run(host="0.0.0.0", port=8000)