SOCIS 2013 Proposal
======
Framework construction and application to real-world inference problem
-------

The goal of this project would be to implement an efficient and object-oriented framework for Python version of BRML toolbox. BRML toolbox is developed under MATLAB and offered various demos related to Bayesian Reasoning and Machine Learning. The toolbox is affiliated to a recent well-designed book by David Barber, Reader from Computer Science Department in University College London(UCL).

The significance for our PyBRML work can be emphasized in two ways:

 * Bayesian reasoning and probabilistic graphical model is a unified framework for building expert system in order to solve real-world problems.
 * Currently, no actively-developing toolbox for bayesian reasoning and probabilistic graphical model under Python exists. Our PyBRML would benefits both the book readers, engineers and researchers who prefer Python as well.

The BRML toolbox offered algorithms for various topics, such as Bayesian reasoning, machine learning, dynamic systems and approximate inference etc. The current framework in BRML is summarized below:

https://github.com/pythonroar/PyBRML/blob/master/proposal/datastructure.png

In SOCIS 2013, most importantly, we will focus on the Bayesian reasoning and probabilistic graphical model section since it provides probabilistic modeling which is fundamental for probabilistic machine learning and dynamical models and further approximate inference. 

Roadmap
-------
The First Step of this project is to create a framework for BRML toolbox in Python corresponding to MATLAB version. On the Bayesian reasoning and probabilistic graphical model part, there are about 10 standalone functions for graph theory, 30 for potential manipulation and 20 for inference. Thanks to the demos(ie. demoClouseau, demoBurglar, demoMRFclean, demoMostProbablePath, demoShortestPath, demoSumprod, demoMaxprod, demoBucketElim etc.) offered by BRMLtoolbox, we will conduct our implementation based on the demos one by one. Finally make the inference algorithms such as factor graph and junction tree accessible for solving problems.

Further Steps of the project would then consists two directions:

 * Develop visualization library for Bayesian reasoning and probabilistic graphical model based on matplotlib library, corresponding to miscellaneous functions in BRML toolbox.
 * Follow the AAAI’00 paper on Bayesian Fault Detection and Diagnosis in Dynamic System, make a throughout tutorial on solving real-world problems such as engine monitoring and diagnosis.
 
Basic Requirements:
-------
 
 * Basic background in machine learning and probabilistic graphical model.
 * Former experience with both MATLAB and Python.
 * Familiar with basic software engineering techniques such as version control and doctest.
  
References:
-------
 
 * The BRML Matlab package manual
	http://web4.cs.ucl.ac.uk/staff/D.Barber/textbook/brml_package.pdf
 * Engine Diagnosis paper
	U. Lerner, R. Parr, D. Koller, and G. Biswas. Bayesian Fault Detection and Diagnosis in Dynamic Systems. In Proceedings of the Seventeenth National Conference on Artificial Intelligence (AIII-00), pages 531-537, 2000.
 * NASA funding research on diagnostics
	http://ti.arc.nasa.gov/tech/dash/diagnostics-and-prognostics/


PyBRML Toolbox
======

PyBRML is a Python version of BRML toolbox for Bayesian Reasoning and Machine Learning

Thanks to Dr. David Barber's book Bayesian Reasoning and Machine Learning and his original design of the toolbox as an accompanying code for the book.


Book
-------
![Bayesian Reasoning and Machine Learning](http://web4.cs.ucl.ac.uk/staff/D.Barber/textbook/jacket.gif)

	@BOOK{barberBRML2012,
	author = {Barber, D.},
	title= {{Bayesian Reasoning and Machine Learning}},
	publisher = {{Cambridge University Press}},
	year = 2012}

website for the book:

http://www.cs.ucl.ac.uk/staff/d.barber/brml/
	
Motivation from David:

The BRMLtoolbox is provided to help readers see how mathematical models translate into actual MAT-
LAB code. There are a large number of demos that a lecturer may wish to use or adapt to help illustrate
the material. In addition many of the exercises make use of the code, helping the reader gain confidence
in the concepts and their application. Along with complete routines for many Machine Learning methods,
the philosophy is to provide low level routines whose composition intuitively follows the mathematical description
of the algorithm. In this way students may easily match the mathematics with the corresponding
algorithmic implementation.


History
-------

Former MATLAB implementation of BRML Toolbox include:

 * Object Oriented Version (OO)
 * Older (non-OO)

 Check these two version from Dr. David Barber's Homepage:
 
 http://web4.cs.ucl.ac.uk/staff/D.Barber/pmwiki/pmwiki.php?n=Brml.Software

Contribution
-------
The source code is hosted on GitHub and comments, suggestions and contributions are welcomed.
If you use BRML toolbox in your work, please cite the reference book.

License
-------
The Python version of BRML toolbox library is available under a GNU license.

Bundled dependencies
-------
 * Numpy
 * matplotlib

Documentation
-------
Under construction

Community
-------
Under construction

Reference
-------
	@BOOK{barberBRML2012,
	author = {Barber, D.},
	title= {{Bayesian Reasoning and Machine Learning}},
	publisher = {{Cambridge University Press}},
	year = 2012}

 
 

 

