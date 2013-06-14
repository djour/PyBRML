"Basic Class: potential"
if __name__ == '__main__':
    print 'PotentialClass is running by itself'
else:
    print 'PotentialClass is imported as module'
	
import numpy as np
import copy

class potential: 
	def __init__(self, variables = [], table = []): 
		self.variables = variables 
		self.table = table 
	def __mul__(self, other):
            
                newpot = copy.copy(self)
#FIX ME: dimension consistency not checked
#FIX ME: only 1-D multiply considered
                print "NOT-SWAPED table: \n", newpot.table
		commonitem = np.intersect1d(np.int8(self.variables),np.int8(other.variables))
		commonindex = np.int8(np.in1d(self.variables,commonitem).nonzero())
		commonshape = np.array(self.table.shape)[commonindex]
		newpot.variables[0],newpot.variables[commonindex] = newpot.variables[commonindex],newpot.variables[0]
                print "current commonindex:", commonindex
                print "current commonitem:", commonitem
                print "current commonshape:", commonshape
		print "current variable index:", newpot.variables
		newpot.table=newpot.table.swapaxes(commonindex,0)
                print "SWAPED table: \n", newpot.table
		for i in range(commonshape):
		#FIX ME: only swap (1-D case) the axes1=commonindex and axes2=0
			newpot.table[i,...] = newpot.table[i,...] * other.table[i]
			#newpot.table[i,...] = table * other.table
		print "current table: \n", newpot.table
		return newpot
	def size(self)
                var =  
                table = np.array(self.table)
                dim = table.ndim
                if dim == 0:
                    print "ERRRRRRRRRRRRRRRRRR"
                elif dim == len():
                    
                
