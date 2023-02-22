import os

basedir = os.path.abspath(os.path.dirname(__file__))
#main directory of the application

class Config(object):
    #will use hardcoded string if environment variable is not defined
    SECRET_KEY=os.environ.get('SECRET_KEY') or "you-will-never-guess"
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
        'sqlite:///' + os.path.join(basedir, 'app.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    MAIL_SERVER = os.environ.get('MAIL_SERVER')
    MAIL_PORT = int(os.environ.get('MAIL_PORT') or 25)
    MAIL_USE_TLS = os.environ.get('MAIL_USE_TLS') is not None
    MAIL_USERNAME = os.environ.get('MAIL_USERNAME')
    MAIL_PASSWORD = os.environ.get('MAIL_PASSWORD')
    ADMINS = ['ipcampbell12@gmail.com']
    POSTS_PER_PAGE = 3
    LANGUAGES = ['en', 'es']
    MS_TRANSLATOR_KEY = os.environ.get('MS_TRANSLATOR_KEY')


    #logging packages has ability to send logs by email