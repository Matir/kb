---
title: Pi UART
---

The UART of the Raspberry Pi is disabled by default.  You may enable it by
placing `enable_uart=1` in the file `/boot/config.txt`.  By default, it is a
`115200bps 8n1` UART.

## Kali Issues

On Kali, you need to remove `kgdboc=ttyAMA0,115200` from cmdline.txt, per [this
bug](https://gitlab.com/kalilinux/build-scripts/kali-arm/-/issues/168)
