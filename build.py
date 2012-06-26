import sys, os, glob

kernel = ""
location = os.path.dirname(os.path.abspath(sys.argv[0])) + os.sep

modLoc = location + "modules/"
moduleExtention = ".cubeos"
modules = []


packLoc = location + "modules/packages/"
packageExtention = ".package"

packageModule = ""
builtPackageModule = ""
packages = ""


# Create a list of all modules
modules.append(modLoc + "environment" + moduleExtention)
modules.append(modLoc + "boot" + moduleExtention)

for files in glob.glob(modLoc + "*" + moduleExtention):
	if files != modules[0] and files != modules[1]:
		modules.append(files)

# Create a string containing all packages
for files in glob.glob(packLoc + "*" + packageExtention):
    packages += open(files, 'r').read()

builtPackageModule = 

kernel += open(location + "LICENSE", 'r').read()

for i in range(0, len(modules)):
    kernel += open(modules[i], 'r').read() + "\n; ; ; ;\n"


