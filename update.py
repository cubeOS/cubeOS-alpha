import sys, os, glob

kernel = ""
location = os.path.dirname(os.path.abspath(sys.argv[0])) + os.sep
modLoc = location + "modules/"

modules = []
moduleExtention = ".cubeos"

packageModule = ""

modules.append(modLoc + "environment" + moduleExtention)
modules.append(modLoc + "boot" + moduleExtention)

for files in glob.glob(location + "modules/*" + moduleExtention):
	if files != modules[0] and files != modules[1]:
		modules.append(files)


kernel += open(location + "LICENSE", 'r').read()
print(modules)
