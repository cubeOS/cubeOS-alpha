package fs

import "types"
import "fsint"
import "str"
import "math"
import "util"

type File struct {
    inode types.InodeNumber
    pos *types.Dword
}

// Defines the high-level filesystem calls, intended to be called by the user.
// Also some helper functions used by them but not exported.

// Requires an absolute path to a file. Directories may not be open()ed directly.
// TODO: Should opening directories be allowed? How does one inspect the contents of a directory?
// Opens the file for reading or writing, doesn't matter. Initially points at the beginning.
// Returns a File to be used as an opaque handle.
// Returns nil/0 if the File is a directory or doesn't exist.
func Open(path string) *File {
    f := new(File)
    f.inode = resolveAbsolutePath(path)
    if (f.inode == 0) {
        return nil
    }
    fsint.ReadInode(f.inode)

    f.pos = new(types.Dword)
    f.pos.lo = 0
    f.pos.hi = 0
    return f
}


// Resolves an absolute path down to an inode number.
// Returns 0 if the requested path does not exist.
func resolveAbsolutePath(path string) types.InodeNumber {
    // Check the path is really absolute.
    if (path[0] != '/') {
        return 0
    }

    // Hand off to the general resolver, starting from the root.
    return resolvePath(0, &path[1])
}

// Resolves a relative path, starting from a given directory.
// Returns 0 if the requested path does not exist.
func resolvePath(dir types.InodeNumber, path string) types.InodeNumber {
    if path[0] == '\000' {
        return dir
    }
    slash := str.IndexOf('/', path)

    // If the slash is -1, no need to insert the NUL.
    // Otherwise we overwrite the / with a NUL
    end := true
    if slash != -1 {
        path[slash] = '\000'
        end = false
    }

    // And look it up using DirLookup
    inode := fsint.DirLookup(dir, path)
    if end || inode == 0 {
        return inode
    }

    // Otherwise recurse.
    return resolvePath(inode, &path[slash+1])
}



// Sets the position into the given file to be equal to the given offset.
// If the seek position is outside the file, blocks will be added to the file to fit. The contents of the new blocks are undefined. Be careful not to exceed the size of the file.
func Seek(f *File, offset *types.Dword) {
    // This is a heap-allocated copy of the inode which must eventually be written out again.
    inode := fsint.MkInodePtr(f.inode)
    blocksToHoldOffset := (offset.hi << 6) + (offset.lo >> 10)
    for blocksToHoldOffset < inode.blockCount {
        // Position is outside the file. Add a block and loop until it's inside the file.
        fsint.AddBlock(inode)
    }

    // Now the file is big enough to contain the offset.
    f.pos = offset
    block := fsint.GetInode(f.inode)
    rawInode := fsint.ReadInode(f.inode)

    rawInode.blockCount = inode.blockCount
    rawInode.db0 = inode.db0
    rawInode.db1 = inode.db1
    rawInode.db2 = inode.db2
    rawInode.db3 = inode.db3
    rawInode.db4 = inode.db4
    rawInode.db5 = inode.db5
    rawInode.db6 = inode.db6
    rawInode.db7 = inode.db7
    rawInode.dbSingleIndirect = inode.dbSingleIndirect
    rawInode.dbDoubleIndirect = inode.dbDoubleIndirect

    delete(inode)
    fsint.WriteBlock(block)
}


// Reads `maxlen` words (not bytes!) from the file, copying into `buf`.
// `buf` must be at least `maxlen` words long, or Bad Things will happen.
// Returns the number of words read, 0xffff/-1 on error.
// Returns 0 on end-of-file.
// The system guarantees to read `maxlen` words into the buffer if and only if `f` is a regular file with at least `maxlen` words to go before end of file. In no other case is the read amount guaranteed.
func Read(f *File, maxlen uint, buf []uint) uint {
    // We can call Read recursively if necessary, but that is better avoided.
    // So, the simple case is easy. Reaching EOF is easy enough too.
    // The tricky case is when the read spans multiple blocks in the file.

    inode := fsint.MkInodePtr(f.inode)
    readSoFar := 0

    // Looping until EOF or maxlen:
    // * readFileAt the running position
    // * Determine how many words I can read until the min of end-of-block and maxlen
    // * Copy the words.
    // * Adjust the running position.

    for (inode.sizeHi > f.pos.hi || (inode.sizeHi == f.pos.hi && inode.sizeLo > f.pos.lo)) && readSoFar < maxlen {
        block := fsint.ReadFileAt(inode, f.pos)

        start := (f.pos.lo & 0x03ff) + fsint.MMR
        end := math.MinU( (start + 0x03ff) & 0xfc00, start+maxlen+1 )

        delta := end - start
        util.Memcopy(([]uint)(start), buf, delta)
        math.DwordPlusUint(f.pos, delta)
        readSoFar += delta
    }

    // When this loop finishes, either we've read all there is to read, or all we were asked to provide.
    return readSoFar
}


