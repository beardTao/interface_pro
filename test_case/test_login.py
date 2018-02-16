import unittest
import requests
from libs.wdms import WDMS
class Test_login(unittest.TestCase):
	def setUp(self):
		s = requests.session()
		self.WDMS = WDMS(s)
	
	def test_login_successful(self):
		'''账号正确，登录成功'''
		r = self.WDMS.login('admin','admin')
		self.assertEqual(r['message'],'Login Successful')
		self.assertEqual(r['code'],200)
	
	def test_login_defeat(self):
		'''账号正确，密码错误'''
		r = self.WDMS.login('admin','admin2')
		self.assertEqual(r['message'],'Username Or Password Is Incorrect')
		self.assertEqual(r['code'],1002)