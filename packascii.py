#!/usr/bin/env python2
import sys
shift = 1;
chars = []
print 'Enter an empty line to exit'
while 1:
	str = raw_input(">")
	if str=='': break
	for c in str:
		n = ord(c)
		if shift:
			chars.append(n << 8)
			shift = 0
		else:
			shift = 1
			chars[-1] |= n
	#add a newline where the enter key was pressed
	if shift:
		chars.append(0x0A << 8)
		shift = 0
	else:
		shift = 1
		chars[-1] |= 0x0A
sys.stdout.write('DAT ')
#but remove the very last newline because it actually shouldn't be there
if shift: chars[-1] &= 0xFF00
else: chars[-1] = 0x0000
last = ''
for n in chars:
	if (last !=''): sys.stdout.write(last+', ')
	last = hex(n)
print last
