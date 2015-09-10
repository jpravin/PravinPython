import fileutil

class Node:
	def __init__(self, name):
		self.name = name
		self.connects = []

	def __repr__(self):
		return "%s:%s" % (self.name, self.connects)

	def addEdge(self, edge):
		self.connects.append(edge)

class Edge:
	def __init__(self, node, distance):
		self.node = node
		self.distance = distance
	def __repr__(self):
		return "%s:%s" % (self.node, self.distance)

def addtomapifnotpresent(map , key, value):
	if key not in map:
		map[key] = value
	return map

file = fileutil.readfileaslist('places.txt')
file = fileutil.removelastline(file)
placesmap = {}
for line in file:
	l = line.split(' ')
	placesmap = addtomapifnotpresent(placesmap, l[0], Node(l[0]))
	placesmap = addtomapifnotpresent(placesmap, l[1], Node(l[1]))
	p1 = placesmap[l[0]]
	p2 = placesmap[l[1]]
	p1.addEdge(Edge(p2, l[2]))
	p2.addEdge(Edge(p1, l[2]))
#	print p1
#	print p2
	
#print placesmap
print placesmap['Birmingham']
print placesmap['London']
