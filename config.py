__all__ = ['config']


class Config(object):
    DEBUG = True
    SECRET_KEY = 'xums'
    SQLALCHEMY_DATABASE_URI = 'sqlite:////tmp/test.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class DevConfig(Config):
    pass


class ProductConfig(Config):
    DEBUG = False


config = dict(dev=DevConfig, product=ProductConfig, default=Config)
