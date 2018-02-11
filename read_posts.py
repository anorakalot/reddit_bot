import praw
reddit = praw.Reddit('bot_1')
subreddit = reddit.subreddit("learnpython")


#print(reddit.user.me())

for submission in subreddit.hot(limit = 5):
    print ("Title: " , submission.title)
    #print ("Text: ", submission.selftext)
    print ("Score: " , submission.score)
    print("\n")
