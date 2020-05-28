'''

import os

class Config:
	#SECRET_KEY = '8f1eb85917a0cee05fecac007d23664f'
	#SQLALCHEMY_DATABASE_URI = 'sqlite:///members.db'
	MAIL_SERVER = 'smtp.gmail.com'
	MAIL_PORT = 587
	MAIL_USE_TLS = True

	MAIL_USERNAME = os.environ.get('EMAIL_USER')
	MAIL_PASSWORD = os.environ.get('EMAIL_PASS')

	['MAIL_USERNAME'] = 'cleophas.mugeni@gmail.com'
	['MAIL_PASSWORD'] = 'Kakosh@123'
	'''