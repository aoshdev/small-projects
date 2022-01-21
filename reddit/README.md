# Reddit script

What it does:
* produce dataset for data exploration (one row per post)
* download photos
* filters by top posts
* customise based on:
    * subreddit name
    * duration ("all", "day", "hour", "month", "week", or "year")
    * limit number of posts

Setup:
* (WIP)

Other considerations:
* Dealing with posts with multiple urls
* Log of what was done and and errors

Learnings:
* using a basic yml configuration file
* access reddit's API using praw package
* os paths
* some Python style guide (2 tabs for arguments in new row)