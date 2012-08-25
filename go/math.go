package math

import "types"


func MinU(x, y uint) uint {
    if y < x { return y }
    return x
}

func DwordPlusUint(dw *types.Dword, n uint) {
    calls := *((*[]*func(*types.Dword, uint)) (8))
    calls[16](dw, n)
}

