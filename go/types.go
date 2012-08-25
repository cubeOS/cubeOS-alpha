package types

type Block uint
type InodeNumber uint

type Dword struct {
    lo, hi uint
}

type Inode struct {
    mode uint
    linkCount uint
    blockCount uint
    sizeLo uint
    sizeHi uint
    _reserved uint
    db0 Block
    db1 Block
    db2 Block
    db3 Block
    db4 Block
    db5 Block
    db6 Block
    db7 Block
    dbSingleIndirect Block
    dbDoubleIndirect Block
}

func DwordLT(x, y Dword) bool {
    if x.hi < y.hi { return true }
    if x.hi > y.hi { return false }
    return x.lo < y.lo
}

