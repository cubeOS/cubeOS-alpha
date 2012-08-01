#!/usr/bin/python

import sys, os, glob

def getlib(libs):
	contents = ""		#create a variable for the output
	if len(libs) == 0:
	  print "No arguments."
	  exit(1)

	for lib in libs:
		libraries += "; LIBRARY: " + lib + " ;\n"
		wd = os.path.join(os.path.pardir, "cubeOS-packages", lib)
		for f in glob.glob(os.path.join(wd, "*.package")):
			libraries += open(f, 'r').read() + "\n"
		libraries += "\n"

	return(libraries)
