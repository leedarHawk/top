'''
Created by auto_sdk on 2019.01.22
'''
from top.api.base import RestApi
class TbkScActivitylinkToolgetRequest(RestApi):
	def __init__(self,domain='gw.api.taobao.com',port=80):
		RestApi.__init__(self,domain, port)
		self.activity_id = None
		self.adzone_id = None
		self.platform = None
		self.relation_id = None
		self.site_id = None
		self.union_id = None

	def getapiname(self):
		return 'taobao.tbk.sc.activitylink.toolget'
