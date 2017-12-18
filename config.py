import os

DEBUG = True

SECRET_KEY = os.urandom(24)

DIALECT = 'mysql'
DRIVER = 'pymysql'
HOST = '127.0.0.1'
PORT = '3306'
USERNAME = 'root'
PASSWORD = 'root'
DATABASE = 'movie_demo3'

SQLALCHEMY_DATABASE_URI = '{}+{}://{}:{}@{}:{}/{}'.format(DIALECT, DRIVER, USERNAME, PASSWORD, HOST, PORT, DATABASE)
SQLALCHEMY_TRACK_MODIFICATIONS = False

