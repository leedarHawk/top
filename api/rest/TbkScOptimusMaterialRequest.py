'''
Created by auto_sdk on 2018.10.29
'''
from top.api.base import RestApi
class TbkScOptimusMaterialRequest(RestApi):
	def __init__(self,domain='gw.api.taobao.com',port=80):
		RestApi.__init__(self,domain, port)
		self.adzone_id = None
		self.content_id = None
		self.content_source = None
		self.device_encrypt = None
		self.device_type = None
		self.device_value = None
		self.material_id = None
		self.page_no = None
		self.page_size = None
		self.site_id = None

	def getapiname(self):
		return 'taobao.tbk.sc.optimus.material'
