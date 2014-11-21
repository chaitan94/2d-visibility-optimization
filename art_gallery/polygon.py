from graph import Graph

class Polygon:
	def __init__(self, points):
		self.points = points
	
	def area(self):
		""" Calculating area via Shoelace Algorithm """
		ans = 0
		n = len(self.points)
		for i in xrange(n):
			curr_point = self.points[i]
			next_point = self.points[(i+1)%n]
			ans += (curr_point.x * next_point.y)
			ans -= (curr_point.y * next_point.x)
		ans /= 2
		return ans
	
	def size(self):
		return len(self.points)
	
	def isConvex(self):
		return all([self.isConvexPoint(i) for i in xrange(self.size())])
	
	def isVertex(self, p):
		return p in self.points
	
	def isConvexPoint(self, i):
		n = self.size()
		i %= n
		prev_point = self.points[(i-1)%n]
		curr_point = self.points[i]
		next_point = self.points[(i+1)%n]
		p = Polygon([prev_point, curr_point, next_point])
		return p.area() > 0
	
	def isEar(self, i):
		n = self.size()
		i %= n
		prev_point = self.points[(i-1)%n]
		curr_point = self.points[i]
		next_point = self.points[(i+1)%n]
		p = Polygon([prev_point, curr_point, next_point])
		f = p.area() > 0
		for v in xrange(n):
			if v == i or v == (i+1)%n or v == (i-1)%n:
				continue
			f = f and (not p.isInTriangle(self.points[v]))
		return f
	
	def isTriangle(self):
		return self.size() == 3
	
	def isInTriangle(self, p):
		if not self.isTriangle(): return False
		d1 = Polygon([p, self.points[0], self.points[1]]).area() < 0
		d2 = Polygon([p, self.points[1], self.points[2]]).area() < 0
		d3 = Polygon([p, self.points[2], self.points[0]]).area() < 0
		return (d1 == d2) and (d2 == d3)
	
	def triangulatedGraph(self):
		if self.size() < 3: return False
		g = Graph()
		org_idx = {}
		poly = Polygon(self.points[:])
		for i in xrange(poly.size()):
			org_idx[poly.points[i]] = i
		while poly.size() >= 3:
			for i in xrange(poly.size()):
				if not poly.isEar(i): continue
				n = poly.size()
				# pprev_point = poly.points[(i-2)%n]
				prev_point = poly.points[(i-1)%n]
				curr_point = poly.points[i]
				next_point = poly.points[(i+1)%n]
				# nnext_point = poly.points[(i+2)%n]
				g.add_edge((org_idx[prev_point], org_idx[curr_point]))
				g.add_edge((org_idx[curr_point], org_idx[next_point]))
				g.add_edge((org_idx[next_point], org_idx[prev_point]))
				poly.points.remove(curr_point)
				# if prev_point.collinear(pprev_point, next_point):
				# 	poly.points.remove(prev_point)
				# if next_point.collinear(nnext_point, prev_point):
				# 	poly.points.remove(next_point)
				break
		return g
	
	def artGallery(self):
		g = self.triangulatedGraph()
		c = g.threeColourize()
		cs = dict([(i, c.count(i)) for i in set(c)])
		color = min(cs, key=cs.get)
		p = []
		for i in xrange(self.size()):
			if c[i] == color:
				p.append(self.points[i])
		return p
	
	def __str__(self):
		s = "Polygon["
		n = self.size()
		for i in xrange(n-1):
			s += "%s, " % self.points[i]
		if n: s += "%s]" % self.points[n-1] 
		return s
