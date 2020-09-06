# ordered dictionary example
# http://docs.python.org/dev/library/collections.html#collections.OrderedDict

import collections

d = {}
o = collections.OrderedDict()

# add to regular dictionary
d['a'] = 1
d['b'] = 2
d['c'] = 3

# add to ordered dictionary
o['a'] = 1
o['b'] = 2
o['c'] = 3

# print both. o returns pairs in order added 
print d
print o

# you can still reference by key
print d['a']
print o['a']
