#!/usr/bin/bython
import sys
str = raw_input(">")
shift = 1;
chars = []
for c in str:
	n = ord(c)
	if shift:
		chars.append(n << 8)
		shift = 0
	else:
		shift = 1
		chars[-1] |= n
sys.stdout.write('DAT ')
last = ''
for n in chars:
	if (last !=''): sys.stdout.write(last+', ')
	last = hex(n)
print(last)
