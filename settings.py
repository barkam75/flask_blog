import os

SECRET_KEY = 'you will never guess'
DEBUG = True
DB_USERNAME = 'flask_db'
DB_PASSWORD = 'flask_pwd'
BLOG_DATABASE_NAME = 'flask_blog'
DB_HOST = os.getenv('IP','0.0.0.0')
DB_URI = "mysql+pymysql://%s:%s@%s/%s" %(DB_USERNAME, DB_PASSWORD,DB_HOST,BLOG_DATABASE_NAME)
SQLALCHEMY_DATABASE_URI = DB_URI
SQLALCHEMY_TRACK_MODIFICATIONS = True
UPLOADED_IMAGES_DEST = '/home/bartek/PycharmProjects/flask_blog/static/images'
UPLOADED_IMAGES_URL = '/static/images/'
