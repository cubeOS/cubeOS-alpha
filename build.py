#!/usr/bin/python

import sys, os, glob, subprocess

kernel = ""
location = os.path.dirname(os.path.abspath(sys.argv[0])) + os.sep

modLoc = location + "modules" + os.sep
moduleExtention = ".dasm16"
modules = []


packLoc = location + os.pardir + os.sep + "cubeOS-packages" + os.sep + "stdlib" + os.sep
packageExtention = ".package"

# Turn any .go files in the packages directory into .package files.
for files in glob.glob(packLoc + "*.go"):
    subprocess.check_call(["go10cc", "-o", files.replace(".go", ".package"), "-p", "-L", packLoc, files])

packageModule = modLoc + "package" + moduleExtention
builtPackageModule = ""
packageLoads = ""
packages = ""

# Create a list of all modules
modules.append(modLoc + "environment" + moduleExtention)
modules.append(modLoc + "boot" + moduleExtention)

for files in glob.glob(modLoc + "*" + moduleExtention):
	if files != modules[0] and files != modules[1] and files != packageModule:
		modules.append(files)

goDir = location + "go" + os.sep

for files in glob.glob(goDir + "*.go"):
    outputFile = files.replace(".go", ".dasm16")
    subprocess.check_call(["go10cc", "-o", outputFile, "-L", goDir, files])
    modules.append(outputFile)

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
