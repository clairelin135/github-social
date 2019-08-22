class BaseConfig(object): # Base Config Class
    DEBUG = True
    TESTING = False
class ProductionConfig(BaseConfig): # Production Specific Config
    DEBUG = False
class DevelopmentConfig(BaseConfig): # Development environment specific configuration
    DEBUG = True
    TESTING = True
