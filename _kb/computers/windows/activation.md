---
title: Activating Windows
---

## Volume Activation ##

For offline/isolated network volume activation, there's a Microsoft KMS
emulator here: [vlmcsd](https://github.com/Wind4/vlmcsd)  Details on using the
emulator from
[HosakaCorp](https://hosakacorp.net/n/84395d60b7185f8f50d6fb108bec09769459d1b5/):

```
PS C:\ > slmgr.vbs /skms 10.13.37.69:1688
PS C:\ > slmgr.vbs /ipk NPPR9-FWDCX-D2C8J-H872k-2YT43
PS C:\ > slmgr.vbs /ato
```

[KMS Client Keys from
Microsoft](https://docs.microsoft.com/en-us/windows-server/get-started/kmsclientkeys)
