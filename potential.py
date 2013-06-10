"Basic Class: PotentialClass"
if __name__ == '__main__':
    print 'PotentialClass is being run by itself'
else:
    print 'PotentialClass is being imported from another module'
	
class PotentialClass: 
	def __init__(self, variables, table): 
		self.variables = variables 
		self.table = table 