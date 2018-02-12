import praw
from urllib.parse import quote_plus
import os

questions = ['what is' , 'who is' , 'what are']
ready_template = '[let me google that for you](http://lmgtfy.com/?q={})'



if not os.path.isfile("posts_replied_to.txt"):
    posts_replied_to = []



else:
    with open("posts_replied_to.txt","r") as f:
        posts_replied_to = f.read()
        posts_replied_to = posts_replied_to.split("\n")
        posts_replied_to = list(filter(None, posts_replied_to))


def main():
    reddit = praw.Reddit('bot')

    subreddit = reddit.subreddit('pythonforengineers')

    for submission in subreddit.hot(limit = 10):
        process_submission(submission)



def process_submission(submission):
    if len(submission.title.split()) > 10:
        return

    norm_title = submission.title.lower();
    if submission.id not in posts_replied_to:
        for q in questions:
            if q in norm_title:
                url_title = quote_plus(submission.title)
                reply_text = ready_template.format(url_title)
                submission.reply(reply_text)
                posts_replied_to.append(submission.id)
                break
    else:
        print('copy')

    with open("posts_replied_to.txt","w") as f:
        for post_id in posts_replied_to:
            f.write(post_id + "\n")

if __name__ == "__main__":
    main()
