# Python implementation of BRMLtoolbox
# Author: Jiuding Duan
# License: GNU license
def demoClouseau():
	"""
	DEMOCLOUSEAU inspector clouseau example
	"""
	print(__doc__)
	
	
	from brml.potential import potential
	from brml.variable import variable
	
	# Variable order is arbitary (3,2,1 for MATLAB)
	butler=2; maid=1; knife=0; 
	# define states, starting from 0. (from 1 for MATLAB)
	murderer=0; notmurderer=1; used=0; notused=1; 

	""" 
	The following definitions of variable are not necessary for computation,
	but are useful for displaying table entries:
	"""
	variableList = [] # create empty list for variable
	
	variable(butler).name='butler'; variable(butler).domain = {'murderer','not murderer'};
	variable(maid).name='maid'; variable(maid).domain ={'murderer','not murderer'};
	variable(knife).name='knife'; variable(knife).domain={'used','not used'};

	"""
	Three potential since p(butler,maid,knife)=p(knife|butler,maid)p(butler)p(maid).
	potential numbering is arbitary
	"""
	pot[butler]=potential;
	pot{butler}.variables=butler;
	pot{butler}.table(murderer)=0.6;
	pot{butler}.table(notmurderer)=0.4;

	pot{maid}=array;
	pot{maid}.variables=maid;
	pot{maid}.table(murderer)=0.2;
	pot{maid}.table(notmurderer)=0.8;

	pot{knife}=array;
	pot{knife}.variables=[knife,butler,maid]; % define array below using this variable order
	pot{knife}.table(used, notmurderer, notmurderer)=0.3;  
	pot{knife}.table(used, notmurderer, murderer)   =0.2;
	pot{knife}.table(used, murderer,    notmurderer)=0.6;
	pot{knife}.table(used, murderer,    murderer)   =0.1;
	pot{knife}.table(notused,:,:)=1-pot{knife}.table(used,:,:); % due to normalisation

jointpot = multpots(pot); % joint distribution

drawNet(dag(pot),variable);
disp('p(butler|knife=used):')
disptable(condpot(setpot(jointpot,knife,used),butler),variable);
	
	