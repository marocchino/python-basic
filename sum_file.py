def to_i(str):
	"""docstring for to_i"""
	try:
		return int(str)
	except:
		return 0

def sum_of_file(url):
	"""docstring for sum_of_file"""
	f = open(url)
	lines = f.readlines()
	return sum(map(to_i, lines))

print sum_of_file('data.txt')
