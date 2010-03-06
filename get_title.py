from sys import argv
def get_title_from_url(url):
	"""docstring for get_title_from_url"""
	try:
		from urllib2 import urlopen
		lines = urlopen(url).read().split("\n")
		for line in lines:
			if "<title>" in line:
				return line
		return "can't find title"
	except:
		return "can't open url"
if len(argv) > 1:
	print get_title_from_url(argv[1])
else
	print get_title_from_url("http://0.0.0.0:3000/articles")
