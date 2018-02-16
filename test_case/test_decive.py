from libs.wdms import WDMS
import unittest
import requests
class Device(unittest.TestCase):
	def setUp(self):
		s = requests.session()
		self.WDMS = WDMS(s)
	
	def test_creat(self):
		'''区域部门不存在'''
		# self.WDMS.login('admin','admin')
		# r = self.WDMS.create_device()
		# self.assertEqual(r['message'],'Succeed')
		pass