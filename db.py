import psycopg2
from config import config
# connection = psycopg2.connect(
#     host = "localhost",
#     port="5432",
#     database="master",
#     user="postgres",
#     password = "password"
# )
def connect():
    connection = None
    