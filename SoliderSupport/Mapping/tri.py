import math

class getFun(object):
	"""docstring for getFun"""
	def __init__(self, r1, r2, r3, x1, x2, x3, y1, y2, y3):
		super(getFun, self).__init__()
		self.r1 = r1
		self.r2 = r2
		self.r3 = r3
		self.x1 = x1
		self.x2 = x2
		self.x3 = x3
		self.y1 = y1
		self.y2 = y2
		self.y3 = y3
		print(r1,r2,r3,x1,x2,x3,y1,y2,y3)
		
	def point(self, x):
 		return math.pow(((x[0]-self.x1)*(x[0]-self.x1)+(x[1]-self.y1)*(x[1]-self.y1)-self.r1*self.r1),2)+math.pow(((x[0]-self.x2)*(x[0]-self.x2)+(x[1]-self.y2)*(x[1]-self.y2)-self.r2*self.r2),2)+math.pow(((x[0]-self.x3)*(x[0]-self.x3)+(x[1]-self.y3)*(x[1]-self.y3)-self.r3*self.r3),2)
		pass