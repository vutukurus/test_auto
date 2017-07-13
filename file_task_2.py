import sys

f=open(sys.argv[1])
a = f.readlines()

for i in a:
	if i.find(sys.argv[2]) >= 0 or i.find(sys.argv[3]) >= 0:
		print i
