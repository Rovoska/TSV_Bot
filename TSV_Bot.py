import praw

user_agent = ("TSV Bot 0.1")
r = praw.reddit(user_agent = user_agent)
subreddit = praw.get_subreddit("svexhange")

for submission in subreddit.get_new(limit = 50):
	print ('Body: '), submission.selftext
	
