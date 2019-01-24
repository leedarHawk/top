'''
Created by auto_sdk on 2018.11.01
'''
from top.api.base import RestApi
class ItemSkusGetRequest(RestApi):
	def __init__(self,domain='gw.api.taobao.com',port=80):
		RestApi.__init__(self,domain, port)
		self.fields = None
		self.num_iids = None

	def getapiname(self):
		return 'taobao.item.skus.get'
