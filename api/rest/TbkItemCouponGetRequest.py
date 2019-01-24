'''
Created by auto_sdk on 2018.11.08
'''
from top.api.base import RestApi
class TbkItemCouponGetRequest(RestApi):
	def __init__(self,domain='gw.api.taobao.com',port=80):
		RestApi.__init__(self,domain, port)
		self.cat = None
		self.page_no = None
		self.page_size = None
		self.pid = None
		self.platform = None
		self.q = None

	def getapiname(self):
		return 'taobao.tbk.item.coupon.get'
