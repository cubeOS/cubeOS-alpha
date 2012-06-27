#!/bin/sh
# This is a script to automate building, compiling, and assembling on 
# Linux. A platform-independent version will be made available soon. You 
# may have to change the line `dcpu cubeOS.bin` to `dcpu-16 cubeOS.bin`, 
# depending on your install of Benedek's emulator.

python build.py
das -o cubeOS.bin cubeOS.dasm16
dcpu cubeOS.bin
