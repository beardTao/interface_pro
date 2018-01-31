import unittest
import HTMLTestRunner
from libs import func
def cases():
	case_dir = r'./test_case'
	discover = unittest.defaultTestLoader.discover(case_dir,pattern = 'test*.py',top_level_dir = None)
	return discover
if __name__ == '__main__':
	file_path = r'./report/result.html'
	with open(file_path,'wb') as fp:
		runner = HTMLTestRunner.HTMLTestRunner(stream = fp,title='test report',description = 'details')
		runner.run(cases())
		#发送邮件
		# func.send_mail()