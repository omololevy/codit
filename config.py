import os

class Config:
    '''
    General configuration parent class
    '''
  
    UPLOADED_PHOTOS_DEST = 'app/static/photos'
    SECRET_KEY = os.environ.get('SECRET_KEY')
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    
    
    #email configurations
    MAIL_SERVER = 'smtp.googlemail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = os.environ.get("MAIL_USERNAME")
    MAIL_PASSWORD = os.environ.get("MAIL_PASSWORD")


    # simple mde  configurations
    SIMPLEMDE_JS_IIFE = True
    SIMPLEMDE_USE_CDN = True

class ProdConfig(Config):
    '''
    Pruduction  configuration child class
    Args:
        Config: The parent configuration class with General configuration settings
    '''
    

class TestConfig(Config):
    '''
    For tests
    '''

class DevConfig(Config):
    '''
    Development  configuration child class
    Args:
        Config: The parent configuration class with General configuration settings
    '''
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = 'postgresql://levy:123456@localhost/codit'

    
config_options = {
'development': DevConfig,
'production': ProdConfig,
'test':TestConfig
}
