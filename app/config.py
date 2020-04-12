import os

basedir = os.path.abspath(os.path.dirname(__file__))

class Config(object):
    """docstring for Config."""

    def __init__(self):
        self.SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URL") or \
        "sqlite:///" + os.path.join(basedir, "app.db")
        self.SQLALCHEMY_TRACK_MODIFICATIONS = False
        self.SECRET_KEY = os.environ.get("SECRET_KEY") or "this_is_the_key"
