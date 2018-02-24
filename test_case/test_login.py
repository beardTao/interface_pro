import unittest
import requests
from libs.wdms import WDMS
class Login(unittest.TestCase):
	def setUp(self):
		s = requests.session()
		self.WDMS = WDMS(s)
	
	def test_login_success(self):
		'''账号密码正确，登录成功'''
		r = self.WDMS.login('admin','admin')
		self.assertEqual(r['message'],'Login Successful')
		self.assertEqual(r['code'],200)
	
	def test_username_error(self):
		'''账号错误，密码正确'''
		r = self.WDMS.login('admin','admin2')
		self.assertEqual(r['message'],'Username Or Password Is Incorrect')
		self.assertEqual(r['code'],1002)	

	def test_password_error(self):
		'''账号正确，密码错误'''
		r = self.WDMS.login('admin2','admin')
		self.assertEqual(r['message'],'Username Or Password Is Incorrect')
		self.assertEqual(r['code'],1002)