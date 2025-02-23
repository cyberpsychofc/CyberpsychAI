from flask import Flask

bot = Flask(__name__)

@bot.route("/")
def home():
    return "CyberpsychAIBot is running!"

if __name__ == "__main__":
    bot.run(host="0.0.0.0", port=8000)