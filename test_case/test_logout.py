import unittest
import requests
from libs.wdms import WDMS
class Test_logout(unittest.TestCase):
	def setUp(self):
		s = requests.session()
		self.WDMS = WDMS(s)
	def test1_logout_successful(self):
		'''成功退出'''
		self.WDMS.login('admin','admin')
		r = self.WDMS.logout('admin','admin')
		self.assertEqual(r['message'],'Logout Successful')
		self.assertEqual(r['code'],200)
	def test2_logout_defeat(self):
		'''未登录,退出'''
		r = self.WDMS.logout('admin','admin')
		self.assertEqual(r['message'],'Login Required')
		self.assertEqual(r['code'],1001)