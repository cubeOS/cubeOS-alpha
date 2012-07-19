# CubeOS Alpha Developers' Guide #
This guide is intended to act as a technical reference for developers deploying on the CubeOS operating system.

## File System ##

The file system is dubbed CAT - it is a HAT filesystem with an API offered by the OS, however you are free to write your own HAT manager as long as it does not conflict with existing files and follows the following guide for data structure:  
```
0x0000 - 0x0004: Four word inode
0x0000: Inode type
0x0001: Parent Inode's Sector Number
0x0002: Reserved
0x0003: Content Length
0x0004 - n-1: Content
n     : EOF; 0x4
```

## Default File Types ##

* .TXT - Packed Text Data - Opens with eTYPE by default
* .ECF - encore's compression format file - Converted to .TXT by eDC by default.
* .BIN - Binary File - Can be Executed by the OS
 * .EXE - Executable File - Opened by the OS
* .RAW - Raw binary file - Non-Executable - Not associated with a program. (A word editor would be a good program to open these with.)
 * .RTF - Raw binary file - Contains unpacked, coloured text. - Opens with eTYPE by default.
* .MUS - Music Sequence Data - Opens with TRXR by default.
* .SH - Shell file to be opened and run by DASH
* .ENC - Encrypted data
* .LMP - LaMP programming language sourcefile.

## Communication ##
When sending files, `EOF`(0x4) should be stripped from the end of files, along with the inode `(Words 0x0000 - 0x0004 of the file.)`  
When receiving files, these should be re-added so the files can be recognized by the OS.

## Subroutines ##

### Tasker ###

#### tusk.newProcess ####
Registers a new process of unique ID. <strike>Adds the process id to the table at *v.tusk.PIDloc*.</strike>
**Modifies:** A
**Returns:** a pointer to the first memory for the process's use

#### tusk.getMem (length) ####
Reserves a *length* amount of memory from the heap using *heap.alloc*, and stores *length* and the location of the reserved memory on the "memory stack," which allows that memory to be freed either when the process calls *tusk.free* or when it terminates.

**Modifies** A
**Returns** the first location of the reserved memory

#### tusk.dropMem ####
Frees up the memory previously reserved by tusk.getMem
**Modifies:** Nothing
**Returns:** Nothing

### Template ###

#### Template.title(input) ####
Description
**Modifies:** Register 1, Register 2
**Returns:** Return 1, Return 2