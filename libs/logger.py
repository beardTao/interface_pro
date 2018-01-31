import logging
import os
class Log():
	def __init__(self):
		#create logger
		self.logger = logging.getLogger()
		self.logger.setLevel(logging.DEBUG)
		#create handle
		self.fh = logging.FileHandler('./logs/log.txt','a',encoding = 'utf-8')
		#for test
		# self.fh = logging.FileHandler('./log.txt','a',encoding = 'utf-8')
		self.fh.setLevel(logging.DEBUG)
		#create formatter
		self.formatter = logging.Formatter('[%(asctime)s] - %(filename)s] - %(levelname)s: %(message)s')
		#handler bind formatter
		self.fh.setFormatter(self.formatter)
		#logger bind handler
		self.logger.addHandler(self.fh)
	
	def debug(self,message):
		self.logger.debug(message)

	def info(self,message):
		self.logger.info(message)

	def warning(self,message):
		self.logger.warning(message)

	def error(self,message):
		self.logger.error(message)	
	
	def critical(self,message):
		self.logger.critical(message)
if __name__ == '__main__':
	log = Log()
	log.info("---begin testing---")
	log.info("---test info---")
	log.info("---end testing ---")