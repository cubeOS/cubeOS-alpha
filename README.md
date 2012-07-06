# CubeOS

**CubeOS** is an operating system for the DCPU-16, intended for fast, scalable computing, and very easy development. It is modeled after UNIX in origin, but has since acquired its own oddities and optimizations. Besides its working filesystem, standard hardware support, and shell, it implements a modular package system with the objective of being able to run all sorts of programs without the difficulty of porting them to a specific form.

CubeOS Organization actively encourages anyone and everything to use CubeOS, develop CubeOS, and develop *for* CubeOS. Its modular package system makes the last two very different; writing packages to be run in CubeOS, as well as printing to the screen and taking command line arguments. If you want to try writing a package from scratch, or making one of your programs into a package to be run on CubeOS, head over [here](http://github.com/cubeOS/cubeOS-packages/). As for actually running CubeOS, we recommend using the [das assembler](http://github.com/jonpovey/das/) and [Benedek's emulator](https://bitbucket.org/benedek/dcpu-16/). See [help](http://github.com/cubeOS/cubeOS-alpha/tree/master/help/), and by all means contact us at cubeos-org@googlegroups.com.

**CubeOS has one major philosophy by which we encourage all developers to live by.

*Release early, release often, and think outside the cube.***


# Old README

## Usage

Older versions of cubeOS were built on [deNULL's emulator](http://dcpu.ru), but as of May 22, 2012, an update made that emulator unusable. Any standard DCPU-16 emulator with at least the [Generic Clock](http://dcpu.com/highnerd/rc_1/clock.txt), [LEM1802](http://dcpu.com/highnerd/rc_1/lem1802.txt), and [Generic Keyboard](http://dcpu.com/highnerd/rc_1/keyboard.txt) attached should be able to run cubeOS.

The current version of cubeOS is built using the [das assembler](https://github.com/jonpovey/das) and run using [benedek's DCPU-16 emulator](https://bitbucket.org/benedek/dcpu-16). Binaries for current and stable releases should be provided regularly. Links to them are easy to get to at the GitHub Pages [page](http://cubeos.github.com/cubeOS-alpha/).

Feel free to contact me for any requests using a GitHub issue on the repository. It's no trouble at all for me to produce a binary, or run a script to collect all the assembly for pasting into an emulator, (in case I forgot to last time.) I don't bite!

## Questions or Requests

Most questions or requests can be addressed within GitHub, through the issue opening feature. However, it may be desirable to contact me (Sasha Crofter) with, say, an interest in joining the GitHub team. CubeOS is open source because I love the idea of anyone liking my idea so much to actually put time and effort into developing it. Join me in the cubeOS Jabber chatroom `cubeos@conference.jabber.org`.
*If I don't respond, send a message such as "SashaCrofter: Are you there?" It should get my attenion if I am at my computer.*
