# CubeOS

**CubeOS** is an operating system for the DCPU-16, intended for fast, scalable computing, and very easy development. It is modeled after UNIX in origin, but has since acquired its own oddities and optimizations. Besides its working filesystem, standard hardware support, and shell, it implements a modular package system with the objective of being able to run all sorts of programs without the difficulty of porting them to a specific form.

CubeOS Organization actively encourages anyone and everything to use CubeOS, develop CubeOS, and develop *for* CubeOS. Its modular package system makes the last two very different; writing packages to be run in CubeOS, as well as printing to the screen and taking command line arguments are made very easy. If you want to try writing a package from scratch, or making one of your programs into a package to be run on CubeOS, head over [here](http://github.com/cubeOS/cubeOS-packages/). As for actually running CubeOS, we recommend using the [das assembler](http://github.com/jonpovey/das/) and [Benedek's emulator](https://bitbucket.org/benedek/dcpu-16/). See [help](http://github.com/cubeOS/cubeOS-alpha/tree/master/help/), and by all means contact us at cubeos-org@googlegroups.com, or on our IRC chatroom on Freenode at `#cubeos`.

**CubeOS has one major philosophy by which we encourage all developers to live by.**

***Release early, release often, and think outside the cube.***

# Installation

To run a CubeOS binary, one only needs a standards-compliant DCPU-16 emulator, such as [Benedek's emulator](https://bitbucket.org/benedek/dcpu-16/), which can run DCPU-16 binaries.

A pre-built *CubeOS.dasm16* file can be assembled and run by any standards-compliant DCPU-16 assembler, such as [das](https://github.com/jonpovey/das), or compiler/emulator combination, such as [dcpu.ru](http://dcpu.ru).

CubeOS can be built from source, as long as one has the necessary tools: [das](https://github.com/jonpovey/das) and [go10cc](https://github.com/shepheb/go10c). These must be present on the system PATH, (easily accomplished on UNIX systems,) or in the CubeOS-alpha directory.
