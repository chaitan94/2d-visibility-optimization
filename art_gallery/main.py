import time
import pygame
from sys import argv
from shapes import *

def usage():
	print "Usage: [filename]"

def read_polygon_from_file(filename):
	f = open(filename, "r")
	p = []
	for line in f:
		u, v = line.strip().split()
		p.append(Point(u, v))
	return Polygon(p)

if __name__ == '__main__':
	if len(argv) != 2:
		usage()
		exit(1)
	p = read_polygon_from_file(argv[1])
	n = p.size()
	lights = p.artGallery()
	m = len(lights)
	print "We need %d light sources at the following positions:" % m
	for i in lights:
		print i

	size = width, height = 1000, 500
	screen = pygame.display.set_mode(size, pygame.NOFRAME)
	screen.fill((224, 224, 224))
	FPS = 60.0

	def handleInputs():
		events = pygame.event.get()
		for event in events:
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_ESCAPE:
					exit(0)

	while 1:
		handleInputs()
		for i in xrange(n):
			curr_point = p.points[i]
			next_point = p.points[(i+1)%n]
			pygame.draw.line(screen, (50, 50, 50), (40+curr_point.x, 40+curr_point.y), (40+next_point.x, 40+next_point.y), 2)
		for i in xrange(n):
			curr_point = p.points[i]
			next_point = p.points[(i+1)%n]
			pygame.draw.line(screen, (50, 50, 50), (540+curr_point.x, 40+curr_point.y), (540+next_point.x, 40+next_point.y), 2)
		for i in lights:
			pygame.draw.circle(screen, (50, 50, 200), (int(540+i.x), int(40+i.y)), 5)
		pygame.display.flip()
		time.sleep(1/FPS)
