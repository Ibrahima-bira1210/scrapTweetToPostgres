import psycopg2


# Insert Tweet data into database
def dbConnect(db_user, db_passwd, db_name, db_host, db_port, user_id, user_name, tweet_id, tweet, retweet_count,
              hashtags):
    print("using dbConnect function")

    conn = psycopg2.connect(host=db_host, database=db_name, port=db_port, user=db_user, password=db_passwd)
    cur = conn.cursor()
    # insert user information
    command = '''INSERT INTO TwitterUser (user_id, user_name) VALUES (%s,%s) ON CONFLICT
                 (User_Id) DO NOTHING;'''
    cur.execute(command, (user_id, user_name))

    # insert tweet information
    command = '''INSERT INTO TwitterTweet (tweet_id, user_id, tweet, retweet_count) VALUES (%s,%s,%s,%s);'''
    cur.execute(command, (tweet_id, user_id, tweet, retweet_count))

    # insert entity information
    for i in range(len(hashtags)):
        hashtag = hashtags[i]
        command = '''INSERT INTO TwitterEntity (tweet_id, hashtag) VALUES (%s,%s);'''
        cur.execute(command, (tweet_id, hashtag))

    # Commit changes
    conn.commit()

    # Disconnect
    cur.close()
    conn.close()

