from flask import render_template, request, Blueprint
from flaskapp.models import User
main = Blueprint('main', __name__)

@main.route('/')
@main.route('/home')
def home():
	page = request.args.get('page', 1, type=int)
	users = User.query.order_by(User.date_created.desc()).paginate(page=page, per_page=3)
	return render_template('home.html', users=users)

@main.route('/about')
def about():
	return  render_template('about.html', title='About')

