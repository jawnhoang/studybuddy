import os
basedir = os.path.abspath(os.path.dirname(__file__))
# directory where database is going to be placed
class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-will-never-guess'
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
    'sqlite:///' + os.path.join(basedir, 'app.db') # telling sql Alchemy where to put the db

    SQLALCHEMY_TRACK_MODIFICATIONS = False # a configuration that keeps track of all the changes we''re making