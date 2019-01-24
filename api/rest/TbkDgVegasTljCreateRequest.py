'''
Created by auto_sdk on 2018.11.10
'''
from top.api.base import RestApi
class TbkDgVegasTljCreateRequest(RestApi):
	def __init__(self,domain='gw.api.taobao.com',port=80):
		RestApi.__init__(self,domain, port)
		self.adzone_id = None
		self.campaign_type = None
		self.item_id = None
		self.name = None
		self.per_face = None
		self.security_switch = None
		self.send_start_time = None
		self.total_num = None
		self.user_total_win_num_limit = None

	def getapiname(self):
		return 'taobao.tbk.dg.vegas.tlj.create'
