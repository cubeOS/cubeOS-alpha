# Application Programming Interface

CubeOS has a number of modules and utilities in its kernel, which can't be accessed directly by programs outside of it. As such, CubeOS provides a single API for programs to make use of.

## Screen Output

At the moment, programs must make calls to *DView* directly. There are no interrupts defined for this purpose.


