def readfileaslist (path):
	f = open (path , 'r')
	file = []
	for line in f:
		file.append(line.strip())
	return file

def removelastline (list):
	list.pop()
	return list
