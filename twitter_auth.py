import tweepy


def auth_twitterV1(api_key, api_secret_key, access_token, access_token_secret):
    # authorize the API Key
    authentication = tweepy.OAuthHandler(api_key, api_secret_key)
    # authorization to user's access token and access token secret
    authentication.set_access_token(access_token, access_token_secret)
    api = tweepy.API(authentication)
    return api


# def auth_twitterV2(bearer_token, access_token, access_token_secret, api_key, api_secret_key):
#     client = tweepy.Client(bearer_token=bearer_token, access_token=access_token,
#                            access_token_secret=access_token_secret, consumer_key=api_key,
#                            consumer_secret=api_secret_key)
#     return client
