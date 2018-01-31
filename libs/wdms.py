import requests
import unittest
import json
class WDMS():
	def __init__(self,s):
		self.s = s
	
	def login(self,username,password):
		url = 'http://127.0.0.1:8081/api/accounts/login/'
		payload = {'username':username,'password':password}
		r = self.s.post(url,json = payload)
		return r.json()
	
	def logout(self,username,password):
		url = 'http://127.0.0.1:8081/api/accounts/logout/'
		payload = {'username':username,'password':password}
		r = self.s.post(url,json = payload)
		return r.json()
	
	'''zone'''
	#create zone;post,json
	def create_zone(self,index,name):
		url = r'http://127.0.0.1:8081/api/zones'
		#Data固定参数，注意大写
		payload = {'Data':[{'zoneNumber':index,'zoneName':name}]}
		r = self.s.post(url,json = payload)
		return r.json()
	
	#get zone info ; get
	def get_zone_info(self):
		url = r'http://127.0.0.1:8081/api/zones'
		r = self.s.get(url)
		return r.json()
	
	'''department'''
	#create department
	def create_department(self,code,name,zone_num):
		url = r'http://127.0.0.1:8081/api/departments?zoneNumber=1'
		payload = {'Data':[{'departmentCode':code,'departmentName':name,'zoneNumber':zone_num}]}
		r = self.s.post(url,json = payload)
		return r.json()

	#get the information of departments ; get
	def get_department_info(self,data = ''):
		url = r'http://127.0.0.1:8081/api/departments'
		r = self.s.get(url,params = data)
		return r.json()

	#delete parartment ; post , json
	def delete_department(self,code,zone_num):
		url = r'http://127.0.0.1:8081/api/delete/departments/'
		payload = {'departmentCode':code,'zoneNumber':zone_num}
		r = self.s.post(url,json = payload)
		return r.json()
		
	'''device'''
	#get the information of devices 
	def get_device_info(self):
		url = r'http://127.0.0.1:8081/api/devices?departmentCode=1'
	
	#create or update device;post、json
	def create_device(self):
		# url = r'http://127.0.0.1:8081/api/devices'
		url =r'http://127.0.0.1:8081/iclock/data/company/_new_/'
		payload = {'sn':'123456','zoneNumber':1,'departmentCode':"7","alias":'test'
		,'masterDevice':'Yes','facialDevice':'No'}
		r = self.s.post(url,json = payload)
		return r.json()

