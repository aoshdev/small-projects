
import urllib.request
import praw
import os
from dotenv import load_dotenv
import pandas as pd
from pathlib import Path
from datetime import date
import re

# user inputs
subreddit_name = "shingekinokyojin"
time_filter = "month" # one of: "all", "day", "hour", "month", "week", or "year"
post_limit = 100

# other paths -- don't change
generic_pictures_path = Path.home() / "Pictures"
today = date.today().strftime("%Y_%m_%d")
output_path = f'{generic_pictures_path}\{subreddit_name}'

# create directory if it doesn't already exist
os.mkdir(output_path)

# load reddit keys
load_dotenv()
client_id = os.environ.get('client_id')
secret = os.environ.get('secret')
user_agent = os.environ.get('user_agent')

# read-only instance
reddit = praw.Reddit(client_id=client_id,
 client_secret=secret,
 user_agent=user_agent)

subreddit = reddit.subreddit(subreddit_name)

# save in dataframe and download images
posts = subreddit.top(time_filter=time_filter, limit=post_limit)

posts_dict = {
        "title": [], "score": [],"total_comments": [],
        "post_url": [], "is_jpg": []}

for post in posts:
    posts_dict["title"].append(post.title)
    posts_dict["score"].append(post.score)
    posts_dict["total_comments"].append(post.num_comments)
    posts_dict["post_url"].append(post.url)

    if post.url.endswith(".jpg"):
        posts_dict["is_jpg"].append(1)
        file_name = re.sub(r"[^a-zA-Z0-9]+", ' ', post.title)[:100]
        file_path = f'{output_path}\{file_name}.jpg'
        urllib.request.urlretrieve(post.url, file_path)
    else:
        posts_dict["is_jpg"].append(0)

top_posts = pd.DataFrame(posts_dict)
top_posts.to_csv(f"{output_path}\{subreddit_name}.csv", index=False)
