from libs.wdms import WDMS
import requests
import unittest
# import json
class deparements(unittest.TestCase):
	def setUp(self):
		s = requests.session()
		self.WDMS = WDMS(s)
	
	#create zone
	def test_create_department1(self):
		'''在不存在的区域下创建部门'''
		self.WDMS.login('admin','admin')
		r = self.WDMS.create_department(1,'testDepartments',1)
		self.assertEqual(r['message'],"Zone Doesn't Exist")
		self.assertEqual(r['code'],4002)	

	def test_create_department2(self):
		'''在某区域下创建部门'''
		self.WDMS.login('admin','admin')
		self.WDMS.create_zone('999','testZone999')
		r = self.WDMS.create_department(1,'test2',999)
		self.assertEqual(r['message'],'Succeed')
		self.assertEqual(r['code'],200)

	#get the infomation of departments
	def test_get_all_department_info(self):
		'''获取所有部门信息'''
		self.WDMS.login('admin','admin')
		r = self.WDMS.get_department_info()
		self.assertEqual(r['code'],200)
		self.assertEqual(r['message'],'Succeed')

	def test_get_department_info1(self):
		'''获取非法区域编号下所有部门信息'''
		self.WDMS.login('admin','admin')
		data = {'zoneNumber':'sss'}
		r = self.WDMS.get_department_info(data = data)
		self.assertEqual(r['code'],3006)
		self.assertEqual(r['message']['zoneNumber'][0],'Enter a whole number.')
	
	def test_get_department_info2(self):
		'''获取某个不存在区域下所有部门信息'''
		self.WDMS.login('admin','admin')
		data = {'zoneNumber':123}
		r = self.WDMS.get_department_info(data = data)
		self.assertEqual(r['code'],3008)
		self.assertEqual(r['message'],'Zone 123 Not Found')
	
	def test_get_department_info3(self):
		'''正确获取某个区域下所有部门的信息'''
		self.WDMS.login('admin','admin')
		data = {'zoneNumber':999}
		r = self.WDMS.get_department_info(data = data)
		self.assertEqual(r['code'],200)
		self.assertEqual(r['message'],'Succeed')

	#delete departments
	def test_delete_departments(self):
		'''删除某区域下部门'''
		self.WDMS.login('admin','admin')
		r = self.WDMS.delete_department(1,999)
		self.assertEqual(r['code'],200)
		self.assertEqual(r['message'],'Succeed')