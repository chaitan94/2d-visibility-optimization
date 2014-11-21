class Point:
	def __init__(self, x, y):
		self.x = float(x)
		self.y = float(y)

	def collinear(self, p, q):
		if p.x - self.x  == 0 and q.x - self.x == 0:
			return True
		if p.x - self.x  == 0 or q.x - self.x == 0:
			return False
		m1 = (p.y-self.y)/(p.x-self.x)
		m2 = (q.y-self.y)/(q.x-self.x)
		return m1 == m2
	
	def __str__(self):
		return "Point [%f, %f]" % (self.x, self.y)
