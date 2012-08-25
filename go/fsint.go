package fsint

import "types"

// Keep this in sync with the value in disk.dasm16.
const MMR uint = 0x4000


// Defines the low-level filesystem system calls
// Intended only to be used to implement the higher-level filesystem functions in fs.go, not in user code.

// Finds and loads a new block, returning the block number.
func NewBlock() types.Block {
    calls := * ((*([]*func() types.Block)) (8))
    return calls[0]()
}

// Reserves a new inode and returns its number. Does NOT load the inode table into the MMR.
func NewInode() types.InodeNumber {
    calls := *((*[]*func() types.InodeNumber) (8))
    return calls[1]()
}

// Given an inode number, loads the inode table and returns the block number.
func GetInode(inode types.InodeNumber) types.Block {
    calls := *((*[]*func(types.InodeNumber) types.Block) (8))
    return calls[2](inode)
}

// Given an inode number, makes a copy of the inode on the heap, which must be `delete()`ed later.
func MkInodePtr(inode types.InodeNumber) *types.Inode {
    calls := *((*[]*func(types.InodeNumber) *types.Inode) (8))
    return calls[12](inode)
}

func BitmapFree(typ, number uint) {
    calls := *((*[]*func(uint,uint)) (8))
    calls[3](typ, number)
}

func ReadFileAt(inodePtr *types.Inode, offsetPtr *types.Dword) types.Block {
    calls := *((*[]*func(*types.Inode, *types.Dword) types.Block) (8))
    return calls[4](inodePtr, offsetPtr)
}

func DirLookup(directory types.InodeNumber, filename string) types.InodeNumber {
    calls := *((*[]*func(types.InodeNumber, string) types.InodeNumber) (8))
    return calls[5](directory, filename)
}

func AddBlock(inodePtr *types.Inode) types.Block {
    calls := *((*[]*func(*types.Inode) types.Block) (8))
    return calls[6](inodePtr)
}

func AddToDir(parent, inode types.InodeNumber, filename string) {
    calls := *((*[]*func(types.InodeNumber, types.InodeNumber, string)) (8))
    calls[7](parent, inode, filename)
}

func NewFile(parent types.InodeNumber, filename string) types.InodeNumber {
    calls := *((*[]*func(types.InodeNumber, string) types.InodeNumber) (8))
    return calls[8](parent, filename)
}

func NewDir(parent types.InodeNumber, name string) types.InodeNumber {
    calls := *((*[]*func(types.InodeNumber, string) types.InodeNumber) (8))
    return calls[9](parent, name)
}

func Delete(dirInode types.InodeNumber, filename string) {
    calls := *((*[]*func(types.InodeNumber, string)) (8))
    calls[10](dirInode, filename)
}

func Format(sizeInKW uint) {
    calls := *((*[]*func(uint)) (8))
    calls[11](sizeInKW)
}


// Returns a pointer to an inode on the disk.
func ReadInode(inode types.InodeNumber) *types.Inode {
    GetInode(inode)
    return (*types.Inode)(MMR + (inode & 0x003f) * 16)
}

// Does not delete the inode pointer.
func WriteInode(num types.InodeNumber, inode *types.Inode) {
    block := GetInode(num)
    rawInode := (*types.Inode) (MMR + (num & 0x003f) * 16)

    rawInode.mode = inode.mode
    rawInode.linkCount = inode.linkCount
    rawInode.blockCount = inode.blockCount
    rawInode.sizeLo = inode.sizeLo
    rawInode.sizeHi = inode.sizeHi
    rawInode._reserved = rawInode._reserved
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

    WriteBlock(block)
}

func ReadBlock(block types.Block) {
    calls := *((*[]*func(types.Block)) (8))
    calls[13](block)
}

func WriteBlock(block types.Block) {
    calls := *((*[]*func(types.Block)) (8))
    calls[14](block)
}


