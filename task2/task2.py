import sys

lines = [str(i) for i in open(sys.argv[1])]
a, b = map(float, lines[0].split())
r = float(lines[1])
#print(a, b, r)
for line in open(sys.argv[2]):
	x, y = map(float, line.split())
	res = (x - a)**2 + (y - b)**2
	if res == r*r:
		print(0)
	elif res < r*r:
		print(1)
	else:
		print(2)