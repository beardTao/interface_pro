#python发送邮件包
import smtplib
#python构造邮件包
from email.mime.text import MIMEText
#python邮件附件包
from email.mime.multipart import MIMEMultipart
def send_mail():
	#定义邮件发送参数
	msg = MIMEMultipart()
	sender = 'beardtao@163.com'
	password = ''
	receiver = ['beardtao@163.com']
	# receiver = '383789543@qq.com'
	smtp_server = 'smtp.163.com'
	port = 25
	subject = '接口测试报告'
	body_info = 'WDMS接口测试报告'
	#构造邮件基本信息，收发信件人员
	msg['From'] = sender
	msg['To'] = ';'.join(receiver)
	#构建邮件标题及正文内容
	msg['subject'] = subject
	body = MIMEText(body_info,'html','utf-8')
	msg.attach(body)
	#添加附件
	report_path = r'report/result.html'
	#本文件测试时使用的报告地址
	# report_path = r'G:\interface\project\WMDS\report\result.html'
	with open(report_path,'rb') as f:
		att_body = f.read()
	att = MIMEText(att_body,'base64','utf-8')
	#附件头信息，附件命名为report.html
	att["content-Disposition"] = 'attachment;filename = "report.html"'
	msg.attach(att)
	#准备发送邮件，兼容qq邮件和163邮箱
	try:
		server = smtplib.SMTP_SSL(smtp_server,port)
	except :
		server = smtplib.SMTP(smtp_server,port)
	server.login(sender,password)
	server.sendmail(sender,receiver,msg.as_string())
	server.quit()