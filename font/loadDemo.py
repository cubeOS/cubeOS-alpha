output = "SET A, 0\n\
SET B, videoram \n\
HWI 0 \n\
\n\
SET A, 1 \n\
SET B, fontram \n\
HWI 0 \n\
\n\
SUB PC, 1 \n\
\n\
;;;;;;;;;;;;;;;;;;;;;;;;\n\
; Designated Video RAM ;\n\
;;;;;;;;;;;;;;;;;;;;;;;;\n\
\n\
:fontRam\n\
DAT "

output += open("values.txt", "r").read()

output += "\n\n:videoram\nDAT "

output += open("fontChars.txt", "r").read()

print(output)
