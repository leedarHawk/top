'''
Created by auto_sdk on 2018.11.10
'''
from top.api.base import RestApi
class TbkScOrderGetRequest(RestApi):
	def __init__(self,domain='gw.api.taobao.com',port=80):
		RestApi.__init__(self,domain, port)
		self.fields = None
		self.order_count_type = None
		self.order_query_type = None
		self.order_scene = None
		self.page_no = None
		self.page_size = None
		self.span = None
		self.start_time = None
		self.tk_status = None

	def getapiname(self):
		return 'taobao.tbk.sc.order.get'
