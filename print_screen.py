import datetime
def dict_of_file(url):
	"""docstring for sum_of_file"""
	f = open(url)
	lines = f.readlines()
	dict = {}
	for iter in lines:
		if not iter.lstrip().startswith('#') or len(iter):
			a = iter.split(',')
			if len(a) == 2:
				dict[a[0]] = a[1]
	return dict
d = dict_of_file('data/data2.txt')
for k,v in sorted(d.items()):
	begin,end = map(int,k.split('-'))
	sec = datetime.datetime.now().second
	if  begin <= sec <= end:
		print "%s(now: %s)" % (v, sec)
		break
