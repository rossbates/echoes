"""
echoes.py
~~~~~~~~
This module contains the primary objects which power echoes
"""

import json
import pickle
import os.path
from bs4 import BeautifulSoup
import requests


class EchoAPI:
	url = 'https://pitangui.amazon.com'
	email = ''
	password = ''
	session = None
	logged_in = False
	cookie_file = 'echoes.cookie'

	def __init__(self, email, password):
		self.session = requests.session()
		self.email = email
		self.password = password


		# test a standard request using cookie
		if (
			os.path.isfile(self.cookie_file) and
			self.cookie_auth()
		):
			self.logged_in = True
		else:
			self.login()

	def login(self):
		login_page=self.get('')
		soup = BeautifulSoup(login_page.content)
		login_url = soup.find('form', id='ap_signin_form').get('action')
		hidden_elements = [
			'appActionToken', 'appAction', 'openid.ns', 'prevRID', 'pageId',
			'openid.identity', 'openid.claimed_id', 'openid.mode',
			'openid.assoc_handle', 'openid.return_to', 'create'
		]
		form_inputs = soup.findAll('input', {'name': hidden_elements})

		post_data = {
			'email': self.email,
			'password': self.password
		}

		for elem in form_inputs:
			value = elem.get('value')
			if value:
				post_data[elem.get('name')] = value
			else:
				pass
		r = self.session.post(login_url, data=post_data, headers=get_headers())

		try:
			captcha = BeautifulSoup(r.content).find('div', {'id': 'ap_captcha_img'})
			if captcha is not None:
				raise StandardError('Error: Login Blocked by Captcha')
			else:
				with open(self.cookie_file, 'w') as f:
					pickle.dump(requests.utils.dict_from_cookiejar(self.session.cookies), f)
				self.logged_in = True
		except:
			raise StandardError
		# TODO handle invalid password

	def cookie_auth(self):
		with open(self.cookie_file) as f:
			cookies = requests.utils.cookiejar_from_dict(pickle.load(f))
			self.session.cookies = cookies

		device = self.get('/api/devices/device')

		if device.status_code == 200:
			return True
		else:
			return False

	def cards(self, limit=1):
		params = {'limit': limit}
		cards = self.get('/api/cards',params)
		return json.loads(cards.text)['cards']

	def todos(self, task_type, limit):
		params = {'type': task_type, 'size':limit}
		tasks = self.get('/api/todos', params)
		return json.loads(tasks.text)['values']

	def get(self, url, data=None):
		headers = get_headers()
		return self.session.get(self.url + url, headers=headers, params=data)


def get_headers():
	headers = {
		'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
		'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/38.0.2125.111 Safari/537.36',
		'Charset': 'utf-8',
		'Origin': 'http://echo.amazon.com',
		'Referer': 'http://echo.amazon.com/spa/index.html'
	}
	return headers






