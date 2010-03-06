# -*- coding: utf-8 -*-
import re

def common_word(str):
	"""docstring for common_word"""
	str = re.sub("[.,]","",str.lower())
	array = str.split()
	dic = {}
	for iter in array:
		try:
			dic[iter] += 1
		except:
			dic[iter] = 1
	return sorted(dic.iteritems(), key=lambda (k,v):v, reverse=True)[:3]

def remove_html_tag_from_str(str):
	"""docstring for remove_html_tag_from_str"""
	return re.sub('<[^>]+>',' ',str)


def common_word_from_url(url):
	"""docstring for common_word_from_url"""
	try:
		from urllib2 import urlopen
		data = urlopen(url).read()
		str = remove_html_tag_from_str(data)
		return common_word(str)
	except:
		return "can't open url"

print common_word_from_url('http://www.google.com/intl/en/corporate/')
