import praw
import pdb
import re
import os
from time import sleep

reddit = praw.Reddit('bot_1')
subreddit = reddit.subreddit('pythonforengineers')



if not os.path.isfile("posts_replied_to.txt"):
    posts_replied_to = []



else:
    with open("posts_replied_to.txt","r") as f:
        posts_replied_to = f.read()
        posts_replied_to = posts_replied_to.split("\n")
        posts_replied_to = list(filter(None, posts_replied_to))


for submission in subreddit.hot(limit = 20):
    if submission.id not in posts_replied_to:
        if re.search("I love python" ,submission.title, re.IGNORECASE):
            submission.reply("Sleepy_Bot: GREETINGS FROM SLEEPSVILLE! ")
            print("Bot replying to : ", submission.title)
            posts_replied_to.append(submission.id)
            sleep(10)

with open("posts_replied_to.txt","w") as f:
    for post_id in posts_replied_to:
        f.write(post_id + "\n")
