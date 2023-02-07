# import tweepy
# from tweepy import StreamingClient, StreamRule
# import os
# from dotenv import load_dotenv
#
# load_dotenv()
#
# bearer_token = os.getenv('BEARER_TOKEN')
#
#
# class TweetPrinterV2(tweepy.StreamingClient):
#
#     def on_tweet(self, tweet):
#         print(f"{tweet.id} {tweet.created_at} ({tweet.author_id}): {tweet.text} :{tweet.context_annotations}")
#         print("-" * 50)
#
#
# printer = TweetPrinterV2(bearer_token)
#
# # add new rules
# rule = StreamRule(value="sncf")
# printer.add_rules(rule)
#
# printer.filter()
#
#






# import requests
# import tweepy
#
# import load_env as l_env
# from twitter_auth import auth_twitterV1
#
# client = tweepy.Client(bearer_token=l_env.bearer_token, access_token=l_env.access_token,
#                        access_token_secret=l_env.access_token_secret, consumer_key=l_env.api_key,
#                        consumer_secret=l_env.api_secret_key)
# # Define query
# query = 'sncf'
#
# # get max. 100 tweets
# tweets = client.search_recent_tweets(query=query,
#                                      tweet_fields=['author_id', 'created_at'],
#                                      max_results=100)
#
# for tweet in tweets.data:
#     print('\n**Tweet Text**\n',tweet.context_annotations)


# import pandas as pd
#
# # Save data as dictionary
# tweets_dict = tweets.json()
#
# # Extract "data" value from dictionary
# tweets_data = tweets_dict['data']
#
# # Transform to pandas Dataframe
# df = pd.json_normalize(tweets_data)
# print(df.head())
