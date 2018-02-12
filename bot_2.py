import praw
import re
import os
import pdb

reddit = praw.Reddit('bot')
subreddit = reddit.subreddit('pythonforengineers')


if not os.path.isfile("comments_replied_to.txt"):
    comments_replied_to = []


else:
    with open('comments_replied_to.txt',"r") as f:
        comments_replied_to = f.read()
        comments_replied_to = comments_replied_to.split("\n")
        comments_replied_to = list(filter(None,comments_replied_to))



for comment in subreddit.stream.comments():
    if comment.id not in comments_replied_to:
        if re.search("sleepybot pls help",comment.body,re.IGNORECASE):
            comment.reply("Sleepy_Bot to the rescue!")
            comments_replied_to.append(comment.id)
            comment_file = open('comments_replied_to.txt','w')
            comment_file.write(comment.id+"\n")
            comment_file.close()
comment_file.close()

'''
with open("comments_replied_to.txt","w") as f:
    for comment_id in comments_replied_to:
'''
