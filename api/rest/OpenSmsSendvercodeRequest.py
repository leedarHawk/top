'''
Created by auto_sdk on 2018.07.26
'''
from top.api.base import RestApi
class OpenSmsSendvercodeRequest(RestApi):
	def __init__(self,domain='gw.api.taobao.com',port=80):
		RestApi.__init__(self,domain, port)
		self.send_ver_code_request = None

	def getapiname(self):
		return 'taobao.open.sms.sendvercode'
