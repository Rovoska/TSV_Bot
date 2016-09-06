#!/usr/bin/python
import praw 

user_agent = ("TSV Bot 0.1")
r = praw.Reddit(user_agent=user_agent)
subreddit = r.get_subreddit("svexchange")
tsv = '1132'

# Get posts and filter if containing 1132
for submission in subreddit.get_new(limit=1):
    if re.search('1132', submission.selftext, re.IGNORECASE):
        print ('Title:'), submission.title
        print ('Body: '), submission.selftext
        print '---------------------------------\n'
        
    
