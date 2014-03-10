
A4_PORTRAIT_IN_MM = (210,297)
A4_LANDSCAPE_IN_MM = (297,210)

class Metrics:
	def __init__(self, dpi):
		self.dpi = dpi
		
	def pt2px(self,pts):
		return 1/72*self.dpi*pts
		
	def mm2pt(self,mms):
		return round(mms/25*72*(self.dpi/72))
		
	def mm2px(self,mms):
		return round(1/25*self.dpi*mms);
		
	def mmpoint2px(self,mmpoint):
		return (self.mm2px(mmpoint[0]),self.mm2px(mmpoint[1]))