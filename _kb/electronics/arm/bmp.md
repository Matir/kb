---
title: Using Black Magic Probe
---

## Flashing

Can flash via gdb using
`load`(https://sourceware.org/gdb/current/onlinedocs/gdb/Target-Commands.html)
to load a .hex file into the target's Flash.

```
load gcc/firmware.hex
'.../gcc/firmware.elf' has changed; re-reading symbols.
Loading section .sec1, size 0x4284 lma 0x0
Start address 0x00000000, load size 17028
Transfer rate: 18 KB/sec, 946 bytes/write.
```
