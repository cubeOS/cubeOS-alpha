# Coding Standards

These are the guidelines for writing assembly code in CubeOS. If you come across code that doesn't follow these standards, feel free to clean it up.

## Formatting

* Each instruction gets its own line.
* All functions must have documentation at the top, giving their name, arguments, and return value. Any registers they clobber in addition to their arguments must be documented. See below for the calling conventions.
* Comments beginning with ;: instead of just ; will be extracted by a script to populate the Github wiki of documentation. Function header documentation should be in this style, explanatory comments in code probably not.


## Register Use

None of the general-purpose registers (`A`, `B`, `C`, `X`, `Y`, `Z`, `I`, `J`) are reserved for use by the OS; all are available everywhere. Don't abuse the special purpose registers (`EX`, `IA`, `SP`) for things other than their intended purpose.

## Register Clobbering

Functions should not clobber registers other than their arguments and return value (see below). If you need more, save them on the stack and restore them at the end. Make sure all exit points from your function restore the values from the stack -- the easiest way to do this is to have one, labeled exit point and jump to it.

## Jumps

Always `SET PC, label`, never `SUB PC, n`. The latter is much, much too fragile to changes in the arguments or length of the surrounding code.

## Labels

Labels should be namespaced with `.`s, giving their module/package and function name. For example, `heap.alloc` might contain `heap.alloc.search` and `heap.alloc.done`. Try to give all labels meaningful names. `search` and `copy` and `done`, not `2` or `loop`.

## Calling Conventions

Calling functions.

### Arguments

Arguments are passed in the first three general purpose registers, in the order `A`, `B`, `C`. Any further arguments must be pushed to the stack in the order specified by the documentation of the target subroutine. If you need more than that, you should seriously reconsider the design of your code. If you still need more, use the stack and document it carefully.

Argument values need *not* be preserved by a call, so they may be changed without documenting it as a clobber.

### Return values

Return values are to be placed in `A`. If you want multiple return values, reconsider your design, make `A` a pointer to the relevant information. If necessary, reserve an amount of heap space for the purpose, but *be very clear in doing so*, because the program calling your routine must then unreserve it.

## Strings

The preferred string type is C-style null-terminated strings. Although "unpacked" (one ASCII value per word) strings are preferred where said strings must be frequently accessed, "packed strings" (two ASCII values per word in little endian) are preferred in situations where reading is relatively infrequent, or the size of the string is relatively large.

## Heap memory

The functions `heap.alloc` and `heap.free` work similarly to C's `malloc` and `free`. `heap.alloc` takes a size in words and returns a pointer, `heap.free` takes a pointer and frees the memory. Free your memory! Although calls to the heap can be made directly by routines in the kernel, it is highly recommended for processes to call `tusk.getMem`, which behaves similarly to `heap.free`, but keeps track of the location of the heap that it returns. The next call to `tusk.dropMem` will free the memory reserved by the last call to `tusk.getMem`.
