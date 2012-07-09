#!/usr/bin/python

import sys, os, glob, subprocess

kernel = ""
location = os.path.dirname(os.path.abspath(sys.argv[0])) + os.sep

modLoc = os.path.join(location, "modules")
moduleExtention = ".cubeos"
modules = []

packLoc = os.path.join(location, os.pardir, "cubeOS-packages", "stdlib")
packageExtention = ".package"

packageModule = os.path.join(modLoc, "package" + moduleExtention)
builtPackageModule = ""
packageLoads = ""
packages = ""

# Create a list of all modules
modules.append(os.path.join(modLoc, "environment" + moduleExtention))
modules.append(os.path.join(modLoc, "boot" + moduleExtention))

for files in glob.glob(os.path.join(modLoc, "*" + moduleExtention)):
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
kernelf = open(os.path.join(location, "cubeOS.dasm16"), 'w')
kernelf.seek(0)
kernelf.write(kernel)
kernelf.truncate()
kernelf.close()
