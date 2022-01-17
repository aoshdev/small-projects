import urllib.request
import praw
import os
from dotenv import load_dotenv
import pandas as pd
from pathlib import Path
import datetime
import re
import yaml

# read in yaml file (containing user inputs)
yml_path = f"{os.path.dirname(__file__)}/sample.yml"
with open(yml_path) as f:
    inputs = yaml.safe_load(f)

# paths
generic_pictures_path = Path.home() / "Pictures"
today = datetime.date.today().strftime("%Y_%m_%d")
output_path = f"{generic_pictures_path}\{inputs['subreddit_name']}"

# create directory if it doesn't already exist
if not os.path.isdir(output_path):
    os.mkdir(output_path)

# load reddit keys
load_dotenv()
client_id = os.environ.get('client_id')
secret = os.environ.get('secret')
user_agent = os.environ.get('user_agent')

# read-only instance
reddit = praw.Reddit(
        client_id=client_id,
        client_secret=secret,
        user_agent=user_agent)

subreddit = reddit.subreddit(inputs['subreddit_name'])

posts = subreddit.top(
        time_filter=inputs['time_filter'], 
        limit=inputs['post_limit'])

posts_dict = {
        "title": [], "score": [],"total_comments": [],
        "post_url": [], "datetime_utc": []}

for post in posts:
    posts_dict["title"].append(post.title)
    posts_dict["score"].append(post.score)
    posts_dict["total_comments"].append(post.num_comments)
    posts_dict["post_url"].append(post.url)

    datetime_utc = datetime.datetime.fromtimestamp(post.created)
    posts_dict["datetime_utc"].append(datetime_utc)

top_posts = pd.DataFrame(posts_dict)
top_posts.to_csv(f"{output_path}\{inputs['subreddit_name']}.csv", index=False)

print("Saved dataset.")

# save pictures
if inputs["download_pics"] == 'y':

    print("Starting to save pictures.")

    for i, k in enumerate(posts_dict['post_url']):
        
        post_url = posts_dict["post_url"][i]
        post_title = posts_dict["title"][i][:100] # truncate

        # # download if it's a picture
        if post_url.endswith(".jpg"):
            file_name = re.sub(r"[^a-zA-Z0-9]+", ' ', post_title)
            file_path = f'{output_path}\{file_name}.jpg'
            urllib.request.urlretrieve(post_url, file_path)

    print("Finished saving pictures.")
    print(f"Saved here: {output_path}")

print("All done.")