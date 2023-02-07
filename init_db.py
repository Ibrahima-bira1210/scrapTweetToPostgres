import psycopg2

# Table creation
commands = (  # Table 1
    '''Create Table IF NOT EXISTS TwitterUser(User_Id BIGINT PRIMARY KEY, User_Name TEXT);''',
    # Table 2
    '''Create Table IF NOT EXISTS TwitterTweet(Tweet_Id BIGINT PRIMARY KEY,
                                         User_Id BIGINT,
                                         Tweet TEXT,
                                         sentiments TEXT,
                                         topics TEXT,
                                         Retweet_Count INT,
                                         CONSTRAINT fk_user
                                             FOREIGN KEY(User_Id)
                                                 REFERENCES TwitterUser(User_Id));''',
    # Table 3
    '''Create Table IF NOT EXISTS TwitterEntity(Id SERIAL PRIMARY KEY,
                                         Tweet_Id BIGINT,
                                         Hashtag TEXT,
                                         CONSTRAINT fk_user
                                             FOREIGN KEY(Tweet_Id)
                                                 REFERENCES TwitterTweet(Tweet_Id));''')


def initPostgres(db_host, db_name,db_port, db_user, db_passwd):
    # get request data

    # Connection to database server
    conn = psycopg2.connect(host=db_host, database=db_name, port=db_port, user=db_user,
                            password=db_passwd)
    # Create cursor to execute SQL commands
    cur = conn.cursor()
    # Execute SQL commands/
    for command in commands:
        # Create tables
        cur.execute(command)
    # Close communication with server
    conn.commit()
    cur.close()
    conn.close()