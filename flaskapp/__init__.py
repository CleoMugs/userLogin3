import os
from flask import Flask, abort
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from flask_mail import Mail
from flask_migrate import Migrate
#from flaskapp.config import Config
from config import app_config
#from flaskapp import config


db = SQLAlchemy()


bcrypt = Bcrypt()
login_manager = LoginManager()
login_manager.login_view = 'users.login'
login_manager.login_message_category = 'info'

mail = Mail()

def create_app(config_name): 

	if os.environ.get('FLASK_ENV') == "production":
		app = Flask(__name__)
		app.config.update(SECRET_KEY=os.environ.get('SECRET_KEY'), SQLALCHEMY_DATABASE_URI=os.environ.get('SQLALCHEMY_DATABASE_URI'))
			

	else:
		app = Flask(__name__, instance_relative_config=True)
		app.config.from_object(app_config[config_name])
		app.config.from_pyfile('config.py')


	#app = Flask(__name__, instance_relative_config=True)
	#app.config.from_object(app_config[config_name])
	#app.config.from_pyfile('config.py')

	db.init_app(app)
	bcrypt.init_app(app)
	login_manager.init_app(app)
	mail.init_app(app)

	migrate = Migrate(app, db)
	
	from flaskapp import models


	from flaskapp.users.views import users
	from flaskapp.main.views import main
	from flaskapp.errors.handlers import errors

	app.register_blueprint(users)
	app.register_blueprint(main)
	app.register_blueprint(errors)

	'''
	#Demonstrate 500 Error
	@app.route('/500')
	def error():
		abort(500)
	'''

	return app


'''
mport os
import sys

path = '/home/Cleo/userLogin3'
if path not in sys.path:
    sys.path.append(path)

os.environ['FLASK_ENV'] = 'production'
os.environ['SECRET_KEY'] = '8f1eb85917a0cee05fecac007d23664f'
os.environ['SQLALCHEMY_DATABASE_URI'] = 'mysql://Cleo:kakosh123@Cleo.mysql.pythonanywhere-services.com/Cleo$members'
SQLALCHEMY_DATABASE_URI'='mysql://Cleo:kakosh123@Cleo.mysql.pythonanywhere-services.com/Cleo$members'

from run import app as application
'''