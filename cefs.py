#!/usr/bin/python2

# This script allows interaction between files on the host and in a CEFS disk image.
# Run it with the help command (cefs.py help) for more information.

import sys


def cmdHelp():
    print "Usage: {} command args..."
    print ""
    print "Commands:"
    print "help\t\t\t\tDisplay this help message."
    print "create CEFS_image size\t\t\tCreates a new CEFS disk image with the given name and size (in kilowords)."
    print "format CEFS_image\t\t\tFormat the given CEFS disk image. THIS WILL DESTROY ALL DATA ON THE IMAGE!"
    print "read CEFS_image sourcefile destfile\tReads sourcefile from the given image and writes it to destfile on the host."
    print "\t\t\t\t\tThe sourcefile must be an absolute path; destfile can be relative or absolute."
    print "write CEFS_image sourcefile destfile\tReads sourcefile from the host, and writes it into destfile on the image."
    print "\t\t\t\t\tThe destfile must be an absolute path, sourcefile can be relative."
    print "mkdir CEFS_image path\t\t\tCreates the given directory. Will create multiple layers of directories if necessary."


def cmdCreate():
    print "Create"

def cmdFormat():
    print "Format"

def cmdRead():
    print "Read"

def cmdWrite():
    print "Write"

def cmdMkdir():
    print "Mkdir"


command = {
    'help': cmdHelp,
    'create': cmdCreate,
    'format': cmdFormat,
    'read': cmdRead,
    'write': cmdWrite,
    'mkdir': cmdMkdir
}


if len(sys.argv) < 3:
    command['help']()
    sys.exit(0)

cmd = command[sys.argv[1]]
if cmd:
    cmd()
else:
    command['help']()



