


class Metrics:
	def __init__(self, dpi):
		self.dpi = dpi
		
	def pt2px(self,pts):
		return 1/72*self.dpi*pts
		
	def mm2px(self,mms):
		return 1/25*self.dpi*mms;
		
	def mmpoint2px(self,mmpoint):
		return (self.mm2px(mmpoint[0]),self.mm2px(mmpoint[1]))