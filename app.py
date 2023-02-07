import time

import tweepy
from flask import Flask
from flask import request
import load_env as env
from flasgger import Swagger
from init_db import initPostgres
from streamTweet import MyStreamListener
from twitter_auth import auth_twitterV1
from flasgger import swag_from


app = Flask(__name__)

swagger = Swagger(app)

@app.route('/scrapToPostgres', methods=['POST'])
@swag_from('./scrap.yml')
def scrapToPostgres():
    # # get request data
    # data = request.get_json()
    GEOBOX_FRANCE = [6.295837, 43.201878, 8.535706, 50.349585]
    runtime = 1000

    # Connect to db and initialize a schema
    initPostgres(db_host=env.db_host, db_name=env.db_name, db_port=env.db_port, db_user=env.db_user,
                 db_passwd=env.db_passwd)
    print("init db")

    myStreamListener = MyStreamListener(300, env.db_user, env.db_passwd, env.db_name, env.db_host,
                                        env.db_port)
    myStream = tweepy.Stream(auth=auth_twitterV1(api_key=env.api_key, api_secret_key=env.api_secret_key,
                                                 access_token=env.access_token,
                                                 access_token_secret=env.access_token_secret).auth,
                             listener=myStreamListener, tweet_mode="extended")
    myStream.filter(locations=GEOBOX_FRANCE, languages=["en", "fr"])
    time.sleep(runtime)
    myStream.disconnect()

    return "Scrapping to Postgres in Action let's go", 200


if __name__ == '__main__':
    app.run()
