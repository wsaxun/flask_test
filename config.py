__all__ = ['config']


class Config(object):
    DEBUG = True



class DevConfig(Config):
    pass


class ProductConfig(Config):
    DEBUG = False


config = dict(dev=DevConfig, product=ProductConfig, default=Config)
