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
	app = Flask(__name__, instance_relative_config=True)
	app.config.from_object(app_config[config_name])
	app.config.from_pyfile('config.py')

	db.init_app(app)
	bcrypt.init_app(app)
	login_manager.init_app(app)
	mail.init_app(app)

	migrate = Migrate(app, db)


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
