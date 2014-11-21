import unittest as ut
from shapes import *

class TestPolygon(ut.TestCase):
	def test_area(self):
		p = Polygon([Point(0, 0), Point(1, 0), Point(0, 1)])
		self.assertEqual(p.area(), 0.5)
		p = Polygon([Point(0, 0), Point(0, 1), Point(1, 0)])
		self.assertEqual(p.area(), -0.5)
		p = Polygon([Point(0, 0), Point(1, 0), Point(0.5, 0.5), Point(1, 1), Point(0, 1)])
		self.assertEqual(p.area(), 0.75)
		p = Polygon([Point(0, 0), Point(1, 0), Point(1, 1), Point(0, 1)])
		self.assertEqual(p.area(), 1)
		p = Polygon([Point(0, 0), Point(1, 0), Point(1, 1), Point(0, 1)])
		self.assertEqual(p.area(), 1)

	def test_convex_points(self):
		p = Polygon([Point(0, 0), Point(1, 0), Point(0.5, 0.5), Point(1, 1), Point(0, 1)])
		self.assertTrue(p.isConvexPoint(0))
		self.assertTrue(p.isConvexPoint(1))
		self.assertFalse(p.isConvexPoint(2))
		self.assertTrue(p.isConvexPoint(3))
		self.assertTrue(p.isConvexPoint(4))
		self.assertTrue(p.isConvexPoint(5)) # given i > n
		self.assertTrue(p.isConvexPoint(105)) # given i > n
		p = Polygon([Point(0, 40), Point(30, 30), Point(20, 70)])
		self.assertTrue(p.isConvexPoint(0))
		self.assertTrue(p.isConvexPoint(1))
		self.assertTrue(p.isConvexPoint(2))
		p = Polygon([Point(50, 0), Point(70, 40), Point(50, 50), Point(60, 60), Point(20, 70), Point(30, 30), Point(0, 40)])
		self.assertTrue(p.isConvexPoint(0))
		self.assertTrue(p.isConvexPoint(1))
		self.assertFalse(p.isConvexPoint(2))
		self.assertTrue(p.isConvexPoint(3))
		self.assertTrue(p.isConvexPoint(4))
		self.assertFalse(p.isConvexPoint(5))
		self.assertTrue(p.isConvexPoint(6))

	def test_convex_polygon(self):
		p = Polygon([Point(0, 0), Point(1, 0), Point(1.5, 0.5), Point(1, 1), Point(0, 1)])
		self.assertTrue(p.isConvex())
		p = Polygon([Point(0, 0), Point(1, 0), Point(0.5, 0.5), Point(1, 1), Point(0, 1)])
		self.assertFalse(p.isConvex())

	def test_triangle(self):
		p = Polygon([Point(0, 0), Point(1, 0)])
		self.assertFalse(p.isTriangle())
		p = Polygon([Point(0, 0), Point(1, 0), Point(0, 1)])
		self.assertTrue(p.isTriangle())
		p = Polygon([Point(0, 0), Point(1, 0), Point(1, 1), Point(0, 1)])
		self.assertFalse(p.isTriangle())

	def test_point_in_triangle(self):
		p = Polygon([Point(0, 0), Point(1, 0), Point(0, 1)])
		# On vertex
		self.assertTrue(p.isInTriangle(Point(0, 0)))
		# On edge
		self.assertTrue(p.isInTriangle(Point(0, 0.5)))
		# Interior
		self.assertTrue(p.isInTriangle(Point(0.1, 0.1)))
		# Outside
		self.assertFalse(p.isInTriangle(Point(1, 1)))

	def test_ears(self):
		p = Polygon([Point(0, 0), Point(1, 0), Point(0.3, 0.5), Point(1, 1), Point(0, 1)])
		self.assertFalse(p.isEar(0))
		self.assertTrue(p.isEar(1))
		self.assertFalse(p.isEar(2))
		self.assertTrue(p.isEar(3))
		self.assertFalse(p.isEar(4))
		p = Polygon([Point(50, 0), Point(70, 40), Point(50, 50), Point(60, 60), Point(20, 70), Point(30, 30), Point(0, 40)])
		self.assertFalse(p.isEar(0))
		self.assertTrue(p.isEar(1))
		self.assertFalse(p.isEar(2))
		self.assertTrue(p.isEar(3))
		self.assertFalse(p.isEar(4))
		self.assertFalse(p.isEar(5))
		self.assertTrue(p.isEar(6))

class TestGraph(ut.TestCase):
	def test_add_edge(self):
		g = Graph()
		self.assertEqual(g.size(), 0)
		g.add_edge((1, 2))
		self.assertEqual(g.size(), 2)
		g.add_edge((1, 3))
		self.assertEqual(g.size(), 3)
		g.add_edge((2, 3))
		self.assertEqual(g.size(), 3)
		g.add_edge((4, 5))
		self.assertEqual(g.size(), 5)

if __name__ == '__main__':
	ut.main()
