package str

import "types"


func IndexOf(c char, s string) int {
    for i := 0; true; i++ {
        if (s[i] == char(0)) {
            return -1
        }
        if (s[i] == c) {
            return i
        }
    }
}

