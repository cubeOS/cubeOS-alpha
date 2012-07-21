# Disk hardware spec

This document describes the hardware interface for a block device. This is a simple system that ignores disk geometry (platters, sides, tracks, sectors) and anything else of the kind. Data from the disk is memory mapped into a given location. Any data the operating system wishes to preserve while the disk moves on to other operations must be copied out of the memory mapped region.

Blocks are 1024 16-bit words long.

## Identification

* ID 0x89e1 79d2
* Version 1
* Manufacturer 0x1c6c8b36 (Nya Elektriska)

## Registers

* MMR - Memory map register: Holds the address in the DCPU-16 memory where the data for the disk will be memory mapped.

## Interrupts

Register `A` holds the message type. The meaning of the values are:

1. Set MMR to `B`.
2. Read block whose address is in `B` into the memory map.
3. Write the block from the memory map to the block whose address is in `B`.

The MMR must be set with message 1 prior to calling either of the others.
