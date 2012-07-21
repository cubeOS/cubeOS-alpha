#!/usr/bin/python
# This is a script to automate building, compiling, and assembling on 
# Linux. A platform-independent version will be made available soon. You 
# may have to change the line `dcpu cubeOS.bin` to `dcpu-16 cubeOS.bin`, 
# depending on your install of Benedek's emulator.
import os

import build	#Runs build.py
assembleStatus = os.spawnlp(os.P_WAIT,"das","das","-o","cubeOS.bin","cubeOS.dasm16")
if (assembleStatus==os.EX_OK):
	runStatus = os.spawnlp(os.P_WAIT,"dcpu-16","dcpu-16","cubeOS.bin")
	if (runStatus!=os.EX_OK): print("Error, dcpu-16 returned exit code %d".format(runStatus))
else:
	print("Error, das returned exit code %d".format(assembleStatus))

