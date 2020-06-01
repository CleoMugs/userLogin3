#tests.py
import os
import unittest
from flask import abort, url_for

from flask_testing import TestCase

from flaskapp import create_app, db
from flaskapp.models import User


class TestCase(TestCase):
	def create_app(self):
		config_name = 'testing'
		app = create_app(config_name)
		#app.config.update(SQLALCHEMY_DATABASE_URI = 'sqlite:///members_test.db')
		app.config.update(SQLALCHEMY_DATABASE_URI = 'mysql://cleo:123@localhost/members_test')

		return app

	def setUp(self):
		db.create_all()
		admin = User(username="admin", email="ausers;dmin@admin.com", password="admin123")
		user = User(username="Cleo", email="okinda@gmail.com", password="123")

		db.session.add(admin)
		db.session.add(user)
		db.session.commit()

	def tearDown(self):
		db.session.remove()
		db.drop_all()




class TestModels(TestCase):
	def test_user_model(self):
		self.assertEqual(User.query.count(), 2)
		#self.assertTrue("Cleo" in db.session)


class TestViews(TestCase):
	def test_homepage_view(self):
		"""
		Test that homepage is accessible without login
		"""
		response = self.client.get(url_for('main.home'))
		self.assertEqual(response.status_code, 200)

	def test_login_view(self):
		"""
		Test that login page is accessible without login
		"""
		response = self.client.get(url_for('users.login'))
		#self.assertEqual(response.status_code, 200)

	def test_logout_view(self):
		"""
		Test that logout link is inaccessible without login
		and redirects to login page then to logout
		"""
		target_url = url_for('users.logout')
		redirect_url = url_for('users.login', next=target_url)
		response = self.client.get(target_url)
		self.assertEqual(response.status_code, 302)
		#self.assertRedirects(response, redirect_url)


class TestErrorPages(TestCase):
	def test_404_not_found(self):
		response = self.client.get('/pagenotexist')
		self.assertEqual(response.status_code, 404)
		#self.assertTrue("404 Error" in response.data)


	def test_500_internal_server_error(self):
		@self.app.route('/500')
		def internal_server_error():
			abort(500)

		response = self.client.get('/500')
		self.assertEqual(response.status_code, 500)
		#self.assertTrue("500 Error" in response.data)

if __name__ == '__main__':
	unittest.main()