#!/usr/bin/python2

# This script allows interaction between files on the host and in a CEFS disk image.
# Run it with the help command (cefs.py help) for more information.

import sys
import os
import subprocess
import struct


# Utility functions

# Returns the seek position for a given block number.
def block(n):
    return n * 2048

def getWord(f):
    return struct.unpack(">H", f.read(2))


# Some constants
HEADER = 0
BLOCK_BITMAP = block(1)
INODE_BITMAP = block(5)
INODE_META_TABLE = block(9)

# Returns the contents of the given inode, as an inode object.
def getInode(f, n):
    # Grab the inode meta table and the relevant entry.
    f.seek(INODE_META_TABLE + (2*n//64))

    inodeTableBlock = getWord(f)
    f.seek(block(inodeTableBlock) + (2 * (n & 63))) # Points at the inode

    inode = {}
    inode['mode'] = getWord(f)
    inode['blockCount'] = getWord(f)
    inode['linkCount'] = getWord(f)

    sizeLo = getWord(f)
    sizeHi = getWord(f)

    inode['size'] = (sizeHi << 16) + sizeLo

    inode['reserved'] = getWord(f)

    dataBlocks = []
    for i in range(8):
        dataBlocks.append(getWord(f))

    inode['data'] = dataBlocks
    inode['singlyIndirect'] = getWord(f)
    inode['doublyIndirect'] = getWord(f)

    return inode


# Compares a slice of memory with a Python string. Does not compare their lengths. Pads with 0x00 in the last word.
def compare(words, string):
    string.append(0)
    for i in range(len(words)):
        strWord = (string[2*i] << 16) + string[2*i + 1]
        if strWord != words[i]:
            return False
    return True


def fileContents(f, inodeNum):
    inode = getInode(f, inodeNum)

    lenToGo = inode['size']
    contents = []

    # Read from the direct data blocks
    for b in inode['blocks']:
        if lenToGo <= 0:
            return contents
        toRead = min(1024, lenToGo)
        while toRead > 0:
            contents.append(getWord(f))
            toRead -= 1
            lenToGo -= 1

    if lenToGo <= 0:
        return contents

    # If we didn't return, expand the singly indirect block.
    # TODO: Implement indirect block support.
    print "File extends into indirect blocks, which aren't supported."
    sys.exit(1)



# Given an absolute path, returns the inode number for the file.
# Dies with error messages if the file is not found.
def lookupFile(f, path):
    if path[0] != '/':
        print "ERROR: CEFS paths must be absolute (beginning with /)."
        sys.exit(1)

    dirs = path[1:].split('/')
    inodeNum = 0 # start with the root directory.

    for target in dirs:
        dirContents = fileContents(f, inodeNum)
        dirIndex = 0

        targetLen = (len(target) + 1) // 2 # length in words.
        while True:
            if dirContents[dirIndex+2] == targetLen:
                found = compare(dirContents[dirIndex + 3 : dirIndex + targetLen + 3], target)
                if found:
                    break

            # Mismatch in length or content, move to the next word.
            if dirContents[dirIndex] == 0:
                # No more words. Failed to find.
                print "ERROR: Could not find file/directory {}".format(target)
                sys.exit(1)

            dirIndex += dirContents[dirIndex]

        # If the loop exited, then the directory was found. Load its inode number and continue to the next dir.
        inodeNum = dirContents[dirIndex+1]

    # When we get down here, we've found the file in question.
    return inodeNum


# Given an absolute path, returns the complete contents of the file as a word array.
def readFile(f, path):
    inode = lookupFile(f, path)
    return fileContents(f, inode)


# Command handlers
def cmdHelp():
    print "Usage: {} command args..."
    print ""
    print "Commands:"
    print "help\t\t\t\t\tDisplay this help message."
    print "create CEFS_image size\t\t\tCreates a new CEFS disk image with the given name and size (in kilowords)."
    print "format CEFS_image size\t\t\tFormat the given CEFS disk image with a filesystem of the given size (in kilowords).\n\t\t\t\t\tTHIS WILL DESTROY ALL DATA ON THE IMAGE!"
    print "read CEFS_image sourcefile destfile\tReads sourcefile from the given image and writes it to destfile on the host."
    print "\t\t\t\t\tThe sourcefile must be an absolute path; destfile can be relative or absolute."
    print "write CEFS_image sourcefile destfile\tReads sourcefile from the host, and writes it into destfile on the image."
    print "\t\t\t\t\tThe destfile must be an absolute path, sourcefile can be relative."
    print "mkdir CEFS_image path\t\t\tCreates the given directory. Will create multiple layers of directories if necessary."


def cmdCreate():
    if len(sys.argv) < 4:
        cmdHelp()
        sys.exit(1)

    target = sys.argv[2]
    size = sys.argv[3]

    # Attempt to stat the file, warning the user if it already exists.
    try:
        st = os.stat(target)

        if st:
            sys.stdout.write("Target file {} already exists. Continue? [yN] ".format(target))
            x = sys.stdin.readline()
            if x[0] == 'y' or x[0] == 'Y':
                print "Overwriting the existing file..."
            else:
                print "Aborting!"
                sys.exit(0)
    except OSError:
        pass

    # If we made it down here, either the file doesn't exist yet or we've been bidden to overwrite it.
    subprocess.call(["dd", "if=/dev/zero", "of="+target, "bs=2048", "count="+size])
    print "Successfully created {}\nNB: It is blank and needs formatting before it can be used.".format(target)


def cmdFormat():
    if len(sys.argv) < 4:
        cmdHelp()
        sys.exit(1)

    target = sys.argv[2]
    size = int(sys.argv[3])

    # Open the file, for binary read/write. Write-only would truncate.
    f = open(target, 'r+b')

    # Write the header:
    # Magic number 0x6201, number of blocks, used blocks, used inodes.
    f.write(struct.pack(">4H", 0x6201, size, 12, 1))

    # Write the used block bitmap blocks
    f.seek(block(1))
    f.write(struct.pack(">H", 0x0fff)) # First 12 blocks are used.

    freeBlocks = size-16 # -1 to remove the first word we already wrote
    allBlocks = 0xfff0 # one less than 64k

    while allBlocks > 0:
        if freeBlocks >= 16:
            f.write(struct.pack(">H", 0))
            freeBlocks -= 16
        elif freeBlocks == 0:
            f.write(struct.pack(">H", 0xffff))
        else:
            word = 0
            for i in range(freeBlocks):
                word = (word << 1) + 1
            f.write(struct.pack(">H", word))
            freeBlocks = 0

        allBlocks -= 16

    # Now the whole bitmap should have been written, cursor is at the beginning of the next block.
    # SANITY CHECK: Beginning of block 5
    if f.tell() != block(5):
        print "Sanity check failed: Not at block 5 after writing block bitmap. Expected {}, actual {}".format(block(5), f.tell())
        sys.exit(1)

    # Write the inode table, only the first one used.
    f.write(struct.pack(">H", 0x0001)) # Just the first inode used for the root directory.
    allBlocks = 4095
    while allBlocks > 0:
        f.write(struct.pack(">H", 0))
        allBlocks -= 1

    # Now the cursor is at the beginning of the inode meta table.
    # SANITY CHECK: Beginning of block 9
    if f.tell() != block(9):
        print "Sanity check failed: Not at block 9 after writing inode bitmap. Expected {}, actual {}".format(block(9), f.tell())
        sys.exit(1)

    # The first inode table block is always block 10.
    f.write(struct.pack(">H", 10))
    # And the rest are 0:
    allBlocks = 1023
    while allBlocks > 0:
        f.write(struct.pack(">H", 0))
        allBlocks -= 1

    # SANITY CHECK: Beginning of block 10
    if f.tell() != block(10):
        print "Sanity check failed: Not at block 10 after writing inode meta table. Expected {}, actual {}".format(block(10), f.tell())
        sys.exit(1)

    # Now write the inode for the root directory.
    f.write(struct.pack(">16H",
        2, # Mode, directory.
        1, # Link count
        1, # Block count
        8, # Size low word
        0, # Size high word
        0, # Reserved word
        11, # Data word 0
        0, # Data word 1
        0, # Data word 2
        0, # Data word 3
        0, # Data word 4
        0, # Data word 5
        0, # Data word 6
        0, # Data word 7
        0, # Singly indirect block
        0 # Doubly indirect block
        ))

    for i in range(63*16):
        f.write(struct.pack(">H", 0))

    # SANITY CHECK: Beginning of block 11, the root directory.
    if f.tell() != block(11):
        print "Sanity check failed: Not at block 11 after writing inode meta table. Expected {}, actual {}".format(block(11), f.tell())
        sys.exit(1)

    # Write the directory entry for the root directory.
    f.write(struct.pack(">3HcB", 4, 0, 1, ".", 0))
    f.write(struct.pack(">3H2s", 0, 0, 1, ".."))

    # And we're done.
    f.close()
    print "Formatting complete."



def cmdRead():
    if len(sys.argv) < 5:
        cmdHelp()
        sys.exit(1)

    image = sys.argv[2]
    source = sys.argv[3]
    dest = sys.argv[4]

    # Load the image file, binary reading.
    f = open(image, 'rb')

    # Loads the whole thing into memory in Python. Less than ideal, but so be it.
    contents = readFile(f, source)
    f.close()

    df = open(dest, 'wb')
    for w in contents:
        df.write(struct.pack(">H", w))
    df.close()

    count = len(contents)
    print "Read complete, {} words ({} bytes).".format(count, 2*count)



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



# Main

if len(sys.argv) < 3:
    command['help']()
    sys.exit(0)

cmd = command[sys.argv[1]]
if cmd:
    cmd()
else:
    command['help']()





