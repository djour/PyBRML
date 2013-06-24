#!/usr/bin/env python

"Basic Class: variable"
if __name__ == '__main__':
    print 'VariableClass is running by itself'
else:
    print 'VariableClass is imported as module'
	
class variable: 
	def __init__(self, name = [], domain= []): 
		self.name = name 
		self.domain = domain 