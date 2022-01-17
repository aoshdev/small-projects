import praw
import os
from dotenv import load_dotenv
import pandas as pd

# load reddit keys
load_dotenv()
client_id = os.environ.get('client_id')
secret = os.environ.get('secret')
user_agent = os.environ.get('user_agent')

# read-only instance
reddit = praw.Reddit(client_id=client_id,
 client_secret=secret,
 user_agent=user_agent)

subrredit = reddit.subreddit("shingekinokyojin")

print(subrredit.display_name)
print(subrredit.title)
print(subrredit.description)

for post in subrredit.hot(limit=5):
    print(post.title)
    print()

posts_dict = {"Title": [], "Post Text": [], "ID": [], "Score": [],
 "Total comments": [], "Post URL": []}

for posts in 