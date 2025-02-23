import os
import random
from dotenv import load_dotenv
from groq import Groq

load_dotenv()

os.environ["GROQ_API_KEY"]=os.getenv("GROQ_API_KEY")

llm = Groq(api_key=os.environ.get("GROQ_API_KEY"))  # LLM initialization

topics = ['Computers', 'Astronomy','Black Holes', 'Time Travel', 'Finance']

prompt = f"""
You are an expert on the topic{topics[random.randint(0,len(topics) - 1)]}, tell me an interesting uncommon fact about
it in less than 250 characters. Your response should be precise, avoid using any unnecessary words.
"""
model_name = "llama3-8b-8192"

def generate_tweet_text():
    tweet = llm.chat.completions.create(
        messages=[
            {
                'role':'system',
                'content': prompt
            }
        ],
        model=model_name,
    )
    return tweet.choices[0].message.content