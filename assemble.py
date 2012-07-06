#!/usr/bin/python
import os

daslocation=""
execfile("./pconfig")

os.spawnlp(os.P_WAIT, daslocation, "-o cubeOS.bin cubeOS.dasm16")
