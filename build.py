#!/usr/bin/python

import sys, os, glob, subprocess

kernel = ""
location = os.path.dirname(os.path.abspath(sys.argv[0])) + os.sep

modLoc = location + "modules/"
moduleExtention = ".cubeos"
modules = []

packLoc = location + "modules/packages/"
packageExtention = ".package"

packageModule = modLoc + "package" + moduleExtention
builtPackageModule = ""
packageLoads = ""
packages = ""

dasloc = open("das-location", 'r').read()

# Create a list of all modules
modules.append(modLoc + "environment" + moduleExtention)
modules.append(modLoc + "boot" + moduleExtention)

for files in glob.glob(modLoc + "*" + moduleExtention):
	if files != modules[0] and files != modules[1] and files != packageModule:
		modules.append(files)

# Create a string containing all packages
# also create a DASM string to load the packages
for files in glob.glob(packLoc + "*" + packageExtention):
    packages += open(files, 'r').read()
    filename = os.path.splitext(os.path.basename(files))[0]
    packageLoads += "\nSET A, package." + filename + "\nJSR p.loadPackage\n"

builtPackageModule = open(packageModule, 'r').read().replace(";>loadcalls", packageLoads, 1).replace(";>packages", packages, 1)

kernel += open(location + "LICENSE", 'r').read()

for i in range(0, len(modules)):
    kernel += open(modules[i], 'r').read() + "\n; ; ; ;\n"

kernel += builtPackageModule

# Overwrite old kernel
kernelf = open(location + "cubeOS.dasm16", 'w')
kernelf.seek(0)
kernelf.write(kernel)
kernelf.truncate()
kernelf.close()

args = (dasloc, "-o", "cubeOS.bin", "cubeOS.dasm16")
