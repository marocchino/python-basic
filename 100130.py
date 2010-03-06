# -*- coding: utf-8 -*-

# syntax, cond, function 
# 

print sum(xrange(1,11))

import datetime

sec = datetime.datetime.now().second
if sec & 1:
	print "%d ok"%(sec)
else :
	print "%d no"%(sec)

def hs2ad(num):
	"""docstring for hs2ad
	convert from heisei to AD
	"""
	if num > 1:
		return num + 1988
	else:
		return nil

print hs2ad('dsa')
