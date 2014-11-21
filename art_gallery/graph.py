class Graph:
	def __init__(self):
		self.neighbours = {}
	
	def size(self):
		return len(self.neighbours)
	
	def add_vertex(self, v):
		if v in self.neighbours: return
		self.neighbours[v] = set([])
	
	def add_edge(self, e):
		u, v = e
		if u not in self.neighbours: self.add_vertex(u)
		if v not in self.neighbours: self.add_vertex(v)
		if u not in self.neighbours[v]:
			self.neighbours[v].add(u)
		if v not in self.neighbours[u]:
			self.neighbours[u].add(v)
	
	def threeColourize(self):
		n = self.size()
		colors = [0]*n
		colors[0] = 1
		colors[1] = 2
		while True:
			if all(colors): break
			for i in xrange(n):
				if colors[i]: continue
				c = set([])
				for j in self.neighbours[i]:
					if colors[j]: c.add(colors[j])
				if len(c) > 1:
					colors[i] = 6 - sum(c)
		return colors
	
	def __str__(self):
		s = ""
		for i in self.neighbours:
			s += "%d ->" % i
			for j in self.neighbours[i]:
				s += " %d" % j
			s += '\n'
		return s
