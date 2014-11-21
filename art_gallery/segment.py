class Segment:
	def __init__(self, start, end):
		self.start = start
		self.end = end
	
	def length(self):
		dx = start.x - end.x
		dy = start.y - end.y
		return (dx*dx + dy*dy)**(0.5)
	
	def contains(self, p):
		pass
	
	def __str__(self):
		return "Segment [%s] [%s]" % (self.start, self.end)
