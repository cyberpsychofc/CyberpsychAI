import time
import requests
import threading
import schedule
from flask import Flask
from tweet import tweet, reply

bot = Flask(__name__)

# Free-tier sends atmost of 17 requests a day, so plan
post_times = ["14:00","16:00","18:00","20:00","22:00","00:00"]  # Instance timezone is UTC
#roast_times = ["05:31"]

@bot.route("/", methods=['GET'])
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

def keep_scheduler_alive():
    while True:
        try:
            requests.get('http://localhost:8000/')
        except requests.exceptions.RequestException as e:
            print(f"Failed ping: {e}")
        time.sleep(100) 

if __name__ == "__main__":
    tweet_job()
    task = threading.Thread(target=run_scheduler)
    task.start()
    thread_support = threading.Thread(target=keep_scheduler_alive)
    thread_support.start()
    bot.run(host="0.0.0.0", port=8000)