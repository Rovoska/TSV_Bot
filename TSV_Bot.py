#!/usr/bin/python
import praw

user_agent = ("TSV Bot 0.1")
r = praw.Reddit(user_agent=user_agent)
subreddit = r.get_subreddit("svexchange")
tsv = '1132'

for submission in subreddit.get_new(limit=1):
    op_text = submission.selftext
    tsv_match = any(string in op_text for string in tsv)
    if submission and tsv_match:
        print ('Title:'), submission.title
        print ('Body: '), submission.selftext
        print '---------------------------------\n'
        print ('WHY U NO WORK')
    
