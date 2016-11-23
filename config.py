import os
basedir = os.path.abspath(os.path.dirname(__file__))

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'hard to guess string'
    SQLALCHEMY_COMMIT_ON_TEARDOWN = True
    FLASK_MAIL_SUSBJECT_PREFIX = '[Flasky]'
    FLASKY_MAIL_SENDER = 'Flask Admin <916395242@qq.com>'
    FLASK_ADMIN = os.environ.get('FLASK-ADMIN')
    FLASK_POSTS_PER_PAGE = 10
    FLASKY_FOLLOWERS_PER_PAGE = 10
    FLASK_FOLLOWERS_PER_PAGE = 10
    FLASK_COMMENTS_PER_PAGE = 10
    @staticmethod
    def init_app(app):
        pass

class DevelopmentConfig(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = os.environ.get('DEV_DATABASE_URL') or \
        'sqlite:///' + os.path.join(basedir, 'data-dev.sqlite')


class TestingConfig(Config):
    TESTING = True
    SQLALCHEMY_DATABASE_URI = os.environ.get('TEST_DATABASE_URL') or \
        'sqlite:///' + os.path.join(basedir, 'data-test.sqlite')
    WTF_CSRF_ENABLED = False

config={
    'development':DevelopmentConfig,
    'testing':TestingConfig,
    'default':DevelopmentConfig
}