'''
Created by auto_sdk on 2018.08.28
'''
from top.api.base import RestApi
class TbkScPublisherInfoGetRequest(RestApi):
	def __init__(self,domain='gw.api.taobao.com',port=80):
		RestApi.__init__(self,domain, port)
		self.info_type = None
		self.page_no = None
		self.page_size = None
		self.relation_app = None
		self.relation_id = None

	def getapiname(self):
		return 'taobao.tbk.sc.publisher.info.get'
