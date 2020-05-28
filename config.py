import os

class Config(object):
	
    """
    Common configurations
    """

    # Put any configurations here that are common across all environments


class DevelopmentConfig(Config):
	"""
	Development configurations
	"""
	DEBUG = True
	SQLALCHEMY_ECHO = False
	SQLALCHEMY_TRACK_MODIFICATIONS = True

	MAIL_SERVER = os.environ.get('MAIL_SERVER')
	MAIL_PORT = os.environ.get('MAIL_PORT')
	MAIL_USE_TLS = os.environ.get('MAIL_USE_TLS')


	MAIL_USERNAME = os.environ.get('EMAIL_USER')
	MAIL_PASSWORD = os.environ.get('EMAIL_PASS')

	SECRET_KEY = os.environ.get('SECRET_KEY')
	SQLALCHEMY_DATABASE_URI = os.environ.get('SQLALCHEMY_DATABASE_URI')
	
	

class ProductionConfig(Config):
	"""
	Production configurations
	"""

	DEBUG = False

class TestingConfig(Config):
	"""
	Production configurations
	"""

	#TESTING = True
	


app_config = {
    'development': DevelopmentConfig,
    'production': ProductionConfig,
    'testing': TestingConfig
}


