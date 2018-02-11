import praw
import re
import os
import pdb

reddit = praw.Reddit('bot')
subreddit = reddit.subreddit('pythonforengineers')



for comment in subreddit.stream.comments():
    if re.search("sleepybot pls help",comment.body,re.IGNORECASE):
        comment.reply("Sleepy_Bot to the rescue!")
