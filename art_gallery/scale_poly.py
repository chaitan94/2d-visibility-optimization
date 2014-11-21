from sys import argv
if len(argv) != 3:
	exit(1)
s = float(argv[2])
f = open("polygons/" + argv[1], "r")
for i in f:
	a = i.strip().split()
	print int(a[0]*s), int(a[1]*s)

