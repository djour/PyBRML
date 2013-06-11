# Python implementation of BRMLtoolbox
# Author: Jiuding Duan
# License: GNU license
def demoClouseau():
	"""
	DEMOCLOUSEAU inspector clouseau example
	"""
	print(__doc__)
	
	import numpy as np
	from brml.potential import potential
	from brml.variable import variable
	
	
	# Define number of variables(nodes)
	N = 3   
	butler=2; maid=1; knife=0 # Variable order is arbitary (3,2,1 for MATLAB)	
	# Define states, starting from 0. (from 1 for MATLAB)
	murderer=0; notmurderer=1
	used=0; notused=1

	""" 
	The following definitions of variable are not necessary for computation,
	but are useful for displaying table entries:
	"""
	# Create empty list for variable, len(variable) = N
	variable = [ variable(None, None) for i in range(N)] 
	
	variable[butler].name='butler'; variable[butler].domain = {'murderer','not murderer'}
	variable[maid].name='maid'; variable[maid].domain ={'murderer','not murderer'}
	variable[knife].name='knife'; variable[knife].domain={'used','not used'}

	"""
	Three potential since p(butler,maid,knife)=p(knife|butler,maid)p(butler)p(maid).
	potential numbering is arbitary
	"""
	# Create empty list for potential, len(variable) = N
	pot = [potential(None, None) for i in range(N)]
	
	pot[butler].variables=butler
	table = np.zeros((2))
	table[murderer] =0.4
	table[notmerderer] =0.6
	pot[butler].table = table

	pot[maid].variables=maid
	table = np.zeros((2))
	table[murderer] =0.2
	table[notmerderer] =0.8
	pot[maid].table = table

	pot[knife].variables=[knife,butler,maid] # define array below using this variable order
	table = np.zeros((2,2,2))
	table[used, notmurderer, notmurderer]=0.3
	table[used, notmurderer, murderer]   =0.2
	table[used, murderer,    notmurderer]=0.6
	table[used, murderer,    murderer]   =0.1
	pot[knife].table[notused][:][:]=1-pot[knife].table[used][:][:] # due to normalisation
	pot[knife].table = table

# jointpot = multpots(pot); % joint distribution

#drawNet(dag(pot),variable);
#disp('p(butler|knife=used):')
#disptable(condpot(setpot(jointpot,knife,used),butler),variable);
	
	