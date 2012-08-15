# CubeOS Process System Specifications

The general layout of the CubeOS Process System is as follows. The top-layer *process list* is kept in the heap and pointed to by static OS-memory. The process list contains a list of all active *PID*s and *process-memory pointers*. Every active process has exactly one PID and one pointer to process-memory.

A block of process-memory lives in the heap and is always 16 words long, containing, in order, `PC`, `SP`, `A`, `B`, `C`, `X`, `Y`, `Z`, `I`, `J`, *program memory*, *graphical options*, and four words of open space.

Program memory is a pointer to memory reserved by the non-OS code being run in the context of the process. For example, `usermadeprogram.bin` could reserve a block of sixty words, and store a pointer to that in the program memory slot, then later retrieve that pointer.

The graphical options word is a pointer to memory reserved for the given process by the in-place windowing system, currently DView. The length of such memory, and what such memory holds, is determined by the windowing system, with no intervention from the process system.

The remaining words are reserved for future additions.
