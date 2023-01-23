---
title: USB
---

## UAS Quirks

Lots of devices appear to have issues with the UAS driver on Linux.  These can
be blacklisted by using a module parameter `quirks=VID:PID:u` (i.e., in
`/etc/modprobe.d`).  This can even be enabled at runtime if you can't unload the
module:

```
echo '174c:55aa:u' | tee /sys/module/usb_storage/parameters/quirks
```
