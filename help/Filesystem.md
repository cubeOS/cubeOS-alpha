# CEFS - Cube Extended File System

This file system is a hybrid of the DCPU-16 standard filesystem [HAT](https://github.com/0x10cStandardsCommittee/0x10c-Standards/blob/master/FS/Draft_Harrys_Allocation_Table.txt) and the Linux filesystem ext2.

# About this document

This is version 1 of this document describing version 1 of CEFS.

The design is based on HAT and ext2 and was developed by Braden Shepherdson (shepheb) with input from Sasha Crofter (SashaCrofter).

# Introduction

All sizes are given in 16-bit words. The lowest level of addressing in this filesystem is 16-bit words, there is no addressing of bytes/halfwords/octets. The standard block size is 1K. That is, 1024 16-bit words. Since each block must be addressable by a 16-bit word, there is a maximum filesystem size of 64K blocks, for a total size of 64 x 1024 x 1024 words, or 128MB.

# Structure of the disk

The first few blocks of the disk are structured as follows:

* Header (1 block)
* Used block bitmap (4 blocks)
* Used inode bitmap (4 blocks)
* Inode meta table (1 block)

All blocks after these are filled with user data and inode tables.

## Header

The header sits in block 0 and describes the layout of the disk. It contains:

* A magic number. In this case, 0x6201. The high byte 0x62 indicates a CEFS filesystem, and the lower byte the version, 1.
* Number of 1K blocks on the disk, counting this one.
* Number of blocks which are used.
* Number of inodes which are used.

## Used block bitmap

This is a bitmap of all 64K blocks on the disk, with a 1 indicating the block is in use, and a 0 indicating it is free. Since there are 16 bits in each word, and a maximum of 64K blocks total, we need 64K/16 = 4096 words, therefore this section is 4 blocks long.

For simplicity, all four blocks are reserved even for disks with fewer than 64K blocks.

## Used inode bitmap

Similar to the used block bitmap, this is a 4-block-long bitmap of inode use. 1 indicates in use, 0 indicates free.

## Inode Meta-Table

This is a block pointing to other blocks where inodes may be found. A value of 0 indicates an empty entry. Each inode is 16 words, so 64 inodes to a block. Therefore when the inode meta-table is full, it points to 1024 inode tables, for a total of 64K inodes. Since inode numbers are 16-bit words, this is convenient.

This table is not densely packed; there will inevitably be gaps caused by deletion of files. The inode bitmap in the header allows swift location of empty inodes.


# inodes

An inode is the record of a file or directory. Since each inode is addressed with a 16-bit word, there are a maximum of 64K inodes, and therefore a maximum of 64K files and directories.

An inode is 16 words long, and has the following form:

* Mode: Flags giving the type of file/directory.
* Link count: The number of links to this inode.
* Block count: The number of blocks reserved for this file, regardless of how many are used.
* Size: The actual size of the file. 32 bits, little endian.
* (One word reserved for future use)
* 8 pointers to data blocks.
* Singly-indirect pointer: Points to a block full of pointers to more data blocks.
* Doubly-indirect pointer: Points to a block full of pointers to singly indirect blocks.

Given the maximum possible indirection, a file could be at most 8 + 1024 + 1024^2 blocks in size. That is, 1,049,608 blocks, that is just over 2GB. That is many times the size of a filesystem, but without the doubly indirect block the maximum size is only slightly over 2MB, which is not considered enough.

The root directory is always inode 0.

## Mode flags

The bits of the mode flag are:

* 2-0: inode type. 0 = free, 1 = file, 2 = directory, 3-7: reserved
* 3-15: unused, reserved.



# Types of files

Currently the system supports only regular files and directories. Other possibilities for later implementation include symbolic links, sockets, block and character devices, named pipes (fifos).

## Regular files

A regular file's data blocks contain its contents. There's no wrapper data of any kind. The inode simply points to its data blocks.

## Directories

A directory is stored like a file, but its contents take a particular form. That form is a linked list of file entries. These entries have the following form:

* Relative position of the next entry
* inode number for this file/directory.
* Length of the name field (in characters, not words)
* File name (ASCII string, packed (see appendix A))

The maximum length of a filename is 255 characters (128 words). The name need not have a null terminator because its length is given.

The entries are *not* kept in any specified order, except for the two special subdirectories described below.

A directory entry must fit fully inside a block, and cannot span two blocks. If an entry to be added is too long to fit in this block, leave the space blank and place the entry at the start of a new block.


### Special directory entries

The first two directory entries in any directory are `.` and `..`, in that order. `.` is a reference to the current directory, and `..` is a reference to the parent directory. The root directory's `..` points to itself.


# Algorithms

While implementations are ultimately responsible for how they approach manipulating the file system, here we give recommended approaches and highlight potential gotchas.

## Creating a new file/directory

1. Locate an unused inode using the bitmap.
  * Look up that inode in the meta-table, creating a new inode table if necessary.
  * Populate the inode data.
  * Mark the inode used in the bitmap.
  * Increment the used inode count in the header.
2. Locate a free data block using the bitmap and mark it used. Record its location in the inode. Increment the used block count.
3. Write data into the block.
4. Repeat 2 and 3 as necessary.

If the file is a directory, remember to populate the first two entries for `.` and `..`.

## Look up a file

If a relative path, start from the present directory's inode; the shell should keep track of its number. For an absolute path, the root directory `/` is always inode 0.

Walk the linked list of directory entries, comparing name lengths and names with the requested directory/file. Retrieve the inode of the next directory or the final file, and repeat.

Guard against treating a file like a directory: check the type.

## Delete a file

Look up the file's inode. Mark each of its data blocks unused. Set the type of the inode to 0 meaning it is unused. Mark its inode unused. There is no need to overwrite or otherwise change the data blocks.

### Deleting a directory

A directory should be empty before it is deleted. If it is, then its deletion is the same as that of a file.

To delete nonempty directories, recursively delete all contained files and directories, then delete the empty directory.

## Miscellaneous Notes

* Keep the file size and block count up to date, even for directories.
* Programs must not expect the contents of freshly allocated disk space to be initialized to any particular value.
* Programs storing sensitive data would be wise to overwrite that data themselves before deleting the files containing the sensitive data.


# Appendices

## Appendix A: Packed strings

Two 7-bit ASCII characters, packed into a 16-bit word thus: `0aaa aaaa 0bbb bbbb`. The string is the high octet of the first word, followed by the low octet of the first word, followed by the high octet of the second word, and so on.
