'''
Created by auto_sdk on 2018.07.20
'''
from top.api.base import RestApi
class TbkScNewuserOrderSumRequest(RestApi):
	def __init__(self,domain='gw.api.taobao.com',port=80):
		RestApi.__init__(self,domain, port)
		self.activity_id = None
		self.adzone_id = None
		self.page_no = None
		self.page_size = None
		self.settle_month = None
		self.site_id = None

	def getapiname(self):
		return 'taobao.tbk.sc.newuser.order.sum'
