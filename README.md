# MOPPER
_A simple tool to overwrite opcodes in a binary._

## Usage
```
./mopper.py [file] "[command1];[command2];..."
```

The first parameter is the binary to read.
The second, a list of commands separated by a semicolon.
The output file will be named with the prefix "MOPPED".
Bear in mind that the output binary will not have executable permissions by default, you must change them with "chmod".

## Commands
### NOP (alias N)
Nops an address or an area.
The syntax is: `N[address, hex](:size, decimal)`.
Examples:
- `Nee12` just writes a NOP opcode (0x90) to the position `0xee12`.
- `Ndeadbeef:12` fills from `0xDEADBEEF` to `0xDEADBEFB` with NOPs.

### Write (alias W)
Writes a hexadecimal string to a given position, taking it as the beginning.
Syntax: `W[address, hex]=[value, hex]`
Examples:
- `Wdeadbeef=00` writes a null byte to `0xDEADBEEF`.
- `Wcaca=baca` writes `BA CA` to `0xCACA`.
