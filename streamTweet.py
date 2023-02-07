import time
import tweepy
from db_connect import dbConnect


# Extract hashtags

def read_hashtags(tag_list):
    hashtags = []
    for tag in tag_list:
        hashtags.append(tag['text'])
    return hashtags


class MyStreamListener(tweepy.StreamListener):

    def __init__(self, time_limit=300, db_user="", db_passwd="", db_name="", db_host="", db_port=""):
        self.db_user = db_user
        self.db_passwd = db_passwd
        self.db_name = db_name
        self.db_host = db_host
        self.db_port = db_port
        self.start_time = time.time()
        self.limit = time_limit
        super(MyStreamListener, self).__init__()

    def on_connect(self):
        print("Connected to Twitter API.")

    def on_status(self, status):
        print("using on_status function")
        # Tweet ID
        tweet_id = status.id
        # User ID
        user_id = status.user.id
        # Username
        username = status.user.name
        # Tweet
        if status.truncated:
            tweet = status.extended_tweet['full_text']
            hashtags = status.extended_tweet['entities']['hashtags']
        else:
            tweet = status.text
            hashtags = status.entities['hashtags']

        # Read hastags
        hashtags = read_hashtags(hashtags)

        # Retweet count
        retweet_count = status.retweet_count
        # Language
        lang = status.lang

        # If tweet is not a retweet and tweet is in English
        if not hasattr(status, "retweeted_status") and (lang == "en" or lang == "fr"):
            # Connect to database
            dbConnect(self.db_user, self.db_passwd, self.db_name, self.db_host, self.db_port, user_id, username,
                      tweet_id, tweet, retweet_count, hashtags)

        if float((time.time() - self.start_time)) > float(self.limit):
            print(time.time(), self.start_time, self.limit)
            return False

    def on_error(self, status_code):
        if status_code == 420:
            # Returning False in on_data disconnects the stream
            return False
