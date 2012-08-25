package util


func Memcopy(from, to []uint, length uint) {
    calls := *((*[]*func([]uint, []uint, uint)) (8))
    calls[15](from, to, length)
}

