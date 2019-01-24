'''
Created by auto_sdk on 2018.11.08
'''
from top.api.base import RestApi
class TbkCouponConvertRequest(RestApi):
	def __init__(self,domain='gw.api.taobao.com',port=80):
		RestApi.__init__(self,domain, port)
		self.adzone_id = None
		self.item_id = None
		self.me = None
		self.platform = None

	def getapiname(self):
		return 'taobao.tbk.coupon.convert'
