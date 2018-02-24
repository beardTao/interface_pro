from libs.wdms import WDMS
import requests
import unittest
# import json
class Zone(unittest.TestCase):
	def setUp(self):
		s = requests.session()
		self.WDMS = WDMS(s)
	
	#create zone
	def test1_create_zone(self):
		'''创建区域'''
		self.WDMS.login('admin','admin')
		r = self.WDMS.create_zone(122,'test')
		self.assertEqual(r['message'],'Succeed')
		self.assertEqual(r['code'],200)
	
	#update zone	
	def test2_update_zone(self):
		'''更新区域名称'''
		self.WDMS.login('admin','admin')
		r = self.WDMS.create_zone(122,'test2')
		self.assertEqual(r['message'],'Succeed')
		self.assertEqual(r['code'],200)
	
	def test3_zone_info(self):
		'''获取区域信息'''
		self.WDMS.login('admin','admin')
		r = self.WDMS.get_zone_info()
		self.assertEqual(r['code'],200)
		self.assertEqual(r['message'],'Succeed')
		#判断返回信息值是否正确
		result_zoneName = r['data'][0]['zoneName']
		result_zoneNum = r['data'][0]['zoneNumber']
		self.assertEqual(result_zoneNum,122)
		self.assertEqual(result_zoneName,'test2')
