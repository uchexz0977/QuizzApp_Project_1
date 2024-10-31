import os
from datetime import timedelta

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY', b'\x97\x0f%#\xdep\x97\xf9o\x00\xee\xb5w\x0b\xc3\x07\x02?\x87h@8\x07Q' )
    SQLALCHEMY_DATABASE_URI = 'sqlite:///app.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    DEBUG = True
    REMEMBER_COOKIE_DURATION = timedelta(days=14)  # Set remember me cookie to expire after 14 days




