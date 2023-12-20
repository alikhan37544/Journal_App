import os

class Config:
    # Secret key for sessions (change this to something unique and secure)
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'your_secret_key'

    # MySQL configurations
    MYSQL_HOST = 'localhost'
    MYSQL_USER = 'new_user'
    MYSQL_PASSWORD = 'admin'
    MYSQL_DB = 'journal_app'
    MYSQL_CURSORCLASS = 'pymysql.cursors.DictCursor'
