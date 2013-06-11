# this is a test case for sample codes

from brml.potential import potential
from brml.variable import variable


p = potential(1,1)
print "var POTENTIAL.p created"
print "p.variable = ", p.variables
print "p.table = ", p.table

v = variable('butler',['hehe', 'heihei'])
# v = variable('butler',['murderer','not murderer'])
print "var VARIABLE.v created"
print "v.name = ", v.name
print "v.domain = ", v.domain