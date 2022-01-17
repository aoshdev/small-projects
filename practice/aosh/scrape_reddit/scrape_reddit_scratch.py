"""
Source:
https://towardsdatascience.com/scraping-reddit-data-1c0af3040768
https://www.geeksforgeeks.org/scraping-reddit-using-python/
"""

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

subreddit = reddit.subreddit("shingekinokyojin")

print(subreddit.display_name)
print(subreddit.title)
print(subreddit.description)

for post in subreddit.hot(limit=5):
    print(post.title)
    print()


posts = subreddit.top("month")

posts_dict = {
        "Title": [], "Post Text": [], "ID": [],
        "Score": [],"Total comments": [], "Post URL": []}

for post in posts:
    posts_dict["Title"].append(post.title)
    posts_dict["Post Text"].append(post.selftext)
    posts_dict["ID"].append(post.id)
    posts_dict["Score"].append(post.score)
    posts_dict["Total comments"].append(post.num_comments)
    posts_dict["Post URL"].append(post.url)

top_posts = pd.DataFrame(posts_dict)
top_posts




