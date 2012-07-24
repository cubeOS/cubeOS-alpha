#!/usr/bin/python2
# This is a platform-independent script to automate building, compiling,
# and assembling cubeOS. Windows users must have das and dcpu-16 binaries
# in the cubeOS directory, or in their system PATH location
from subprocess import call
import build	#Runs build.py
assembleStatus = call(["das","-o","cubeOS.bin","cubeOS.dasm16"])
if (assembleStatus==0):
	runStatus = call(["dcpu-16","cubeOS.bin"])
	print "dcpu-16 execution finished with status",runStatus
else:
	print "**ASSEMBLY FAILED WITH STATUS ",assembleStatus,"**"
