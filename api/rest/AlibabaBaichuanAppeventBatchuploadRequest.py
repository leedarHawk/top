'''
Created by auto_sdk on 2018.07.26
'''
from top.api.base import RestApi
class AlibabaBaichuanAppeventBatchuploadRequest(RestApi):
	def __init__(self,domain='gw.api.taobao.com',port=80):
		RestApi.__init__(self,domain, port)
		self.appid = None
		self.bizid = None
		self.params = None

	def getapiname(self):
		return 'alibaba.baichuan.appevent.batchupload'
