from os.path import join, abspath, dirname

basedir = abspath(dirname(__file__))


class Configuration(object):
    DEBUG = True
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    # SQLALCHEMY_DATABASE_URI = 'mysql+mysqlconnector://root:root@localhost:3306/test'
    # SECRET_KEY = "veery gkjygtjygtjgjygsecret"

    # use SQLlite
    SQLALCHEMY_DATABASE_URI = "sqlite:///" + join(basedir, 'database.db')
    SQLALCHEMY__COMMIT_ON_TEARDOWN = True
    SECURITY_PASSWORD_SALT = 'Very difficult string for hack'
    SECURITY_PASSWORD_HASH = 'sha256_crypt'
    # simple example for keep password
    SECRET_KEY = "qwertyuiop["
