package fsint

import "types"

// Defines the low-level filesystem system calls
// Intended only to be used to implement the higher-level filesystem functions in fs.go, not in user code.

// Finds and loads a new block, returning the block number.
func NewBlock() uint {
    calls := * ((*([]*func() uint)) (8))
    return calls[0]()
}

// Reserves a new inode and returns its number. Does NOT load the inode table into the MMR.
func NewInode() uint {
    calls := *((*[]*func() uint) (8))
    return calls[1]()
}

// Given an inode number, loads the inode table and returns the block number.
func GetInode(inode uint) uint {
    calls := *((*[]*func(uint) uint) (8))
    return calls[2](inode)
}

func BitmapFree(typ, number uint) {
    calls := *((*[]*func(uint,uint)) (8))
    calls[3](typ, number)
}

func ReadFileAt(inodePtr types.Inode, offsetPtr types.Dword) uint {
    calls := *((*[]*func(types.Inode, types.Dword) uint) (8))
    return calls[4](inodePtr, offsetPtr)
}

func DirLookup(directory uint, filename string) uint {
    calls := *((*[]*func(uint,string) uint) (8))
    return calls[5](directory, filename)
}

func AddBlock(inodePtr types.Inode) uint {
    calls := *((*[]*func(types.Inode) uint) (8))
    return calls[6](inodePtr)
}

func AddToDir(parent, inode uint, filename string) {
    calls := *((*[]*func(uint, uint, string)) (8))
    calls[7](parent, inode, filename)
}

func NewFile(parent uint, filename string) uint {
    calls := *((*[]*func(uint, string) uint) (8))
    return calls[8](parent, filename)
}

func NewDir(parent uint, name string) uint {
    calls := *((*[]*func(uint, string) uint) (8))
    return calls[9](parent, name)
}

func Delete(dirInode uint, filename string) {
    calls := *((*[]*func(uint, string)) (8))
    calls[10](dirInode, filename)
}

func Format(sizeInKW uint) {
    calls := *((*[]*func(uint)) (8))
    calls[11](sizeInKW)
}

