__all__ = ['config']


class Config(object):
    DEBUG = True
    SERVER_NAME = '0.0.0.0'

    @staticmethod
    def init_app(app):
        pass


class DevConfig(Config):
    pass


class ProductConfig(Config):
    DEBUG = False


config = dict(dev=DevConfig, product=ProductConfig, default=Config)
