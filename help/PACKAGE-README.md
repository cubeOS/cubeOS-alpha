

## Package Writing is No Harder than Assembly
A "package" in cubeOS is distinguished by its having a specific header, and being in a specific place, so that *build.py* is able to add it at build time. Once the package exists, it can be executed by means of an identifier, which is defined within the package header.

## How to Write a Package
For the moment, let us assume that you are writing a package entitled "test." It must be located under modules/packages, by the name test.package. In it, it must contain the following header. *identifier* can be anything of your choosing.

```
:package.test
DAT 0xffab, 0xcdff
DAT "identifier", 0
```

The instruction following 0 is considered to be the first instruction in your package, and that word will be jumped to when *identifier* is entered in the DASH Shell.

## Things to Know
When your package begins executing, **B points to stdin/argv** and **C points to stdout**. More details follow.

### argv
*B* points to an array of pointers to null-terminated strings. [B] is the pointer to the command name, [B+1] the first argument, [B+2] the second, and so on. The last entry in the array is an empty string, signaling the end.

### stdout
*C* points to an output buffer, which should (upon termination of your package) contain a null-terminated string. It has a maximum size of 128 characters (counting the null terminator).

