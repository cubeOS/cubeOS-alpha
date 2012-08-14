#!/usr/bin/python2
#Converts the already assembled cubeOS.bin binary to
#a universally compatible DAT statement, and prints
#it on stdout

bin = open("cubeOS.bin", "rb").read()	#read the binary's contents into bin

output = "DAT "

for i in range(0, len(bin)/2):
	intermediate = bin[2*i] + bin[(2*i)+1]
	value = intermediate.encode('hex_codec')
	output += "0x" + value + ", "

output = output[:-2]

print output
