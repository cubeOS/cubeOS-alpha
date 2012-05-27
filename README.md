# cubeOS

**cubeOS** is a work-in-progress operating system for 0x10<sup>c</sup>'s emulated 16-bit computer, the DCPU-16. It is a UNIX-inspired, command line interface (CLI) driven, and powerful opating system, with the intent to be included on every ship that needs fast and powerful tools to quickly solve mathematical problems, including those posed by navigation, trading, warfare, and other number-crunching activities.

Package-writing should be trivial for the cubeOS, and most assembly programs will need little or no change, (besides being relocatable,) in order to be included (and not necessarily at boot time) and invoked by shell.

## Usage

Older versions of cubeOS were built on [deNULL's emulator](http://dcpu.ru), but as of May 22, 2012, an update made that emulator unusable. Any standard DCPU-16 emulator with at least the [Generic Clock](http://dcpu.com/highnerd/rc_1/clock.txt), [LEM1802](http://dcpu.com/highnerd/rc_1/lem1802.txt), and [Generic Keyboard](http://dcpu.com/highnerd/rc_1/keyboard.txt) attached should be able to run cubeOS.

The current version of cubeOS is built using the [das assembler](https://github.com/jonpovey/das) and run using [benedek's DCPU-16 emulator](https://bitbucket.org/benedek/dcpu-16). Binaries for current and stable releases should be provided regularly. Links to them are easy to get to at the GitHub Pages [page](http://cubeos.github.com/cubeOS-alpha/).

Feel free to contact me for any requests using a GitHub issue on the repository. It's no trouble at all for me to produce a binary, or run a script to collect all the assembly for pasting into an emulator, (in case I forgot to last time.) I don't bite!
