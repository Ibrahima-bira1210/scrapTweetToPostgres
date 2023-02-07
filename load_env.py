from dotenv import load_dotenv

load_dotenv(dotenv_path='.env')
import os

api_key = os.getenv('API_KEY')
api_secret_key = os.getenv('API_SECRET_KEY')
access_token = os.getenv('ACCESS_TOKEN')
access_token_secret = os.getenv('ACCESS_TOKEN_SECRET')
bearer_token = os.getenv('BEARER_TOKEN')

db_host = os.getenv('DB_HOST')
db_name = os.getenv('DB_NAME')
db_port = os.getenv('DB_PORT')
db_user = os.getenv('DB_USER')
db_passwd = os.getenv('DB_PASSWD')
