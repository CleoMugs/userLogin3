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


	#MAIL_USERNAME = os.environ.get('MAIL_USER')
	#MAIL_PASSWORD = os.environ.get('MAIL_PASS')

	

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


