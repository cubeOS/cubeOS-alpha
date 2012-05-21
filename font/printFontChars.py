out = ""

i = 0
while(i<128):
	x = hex(i)[2:]
	if(len(x) < 2):
		x = "0" + x

	out = out + "0xF0" + x + ", "
	i += 1

out = out[:-2]
print(out)
