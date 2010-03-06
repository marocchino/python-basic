def dict_of_file(url):
	"""docstring for sum_of_file"""
	f = open(url)
	lines = f.readlines()
	dict = {}
	for iter in lines:
		if not iter.lstrip().startswith('#'):
			a = iter.split(',')
			if len(a) == 2:
				dict[a[0]] = int(a[1])
	return dict

def avg_age_of_contain(str,dict):
	"""docstring for age_of_contain"""
	sum = 0
	num = 0
	for k,v in dict.items():
		if str in k:
			sum += v
			num += 1
	return sum/num

print avg_age_of_contain('a',dict_of_file('data/data3.txt'))
