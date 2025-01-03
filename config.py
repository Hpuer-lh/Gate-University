import os

class Config:
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:123456@localhost/hpu'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = os.urandom(24)