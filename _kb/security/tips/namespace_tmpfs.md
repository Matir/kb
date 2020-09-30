---
title: Use namespace'd tmpfs
---

```
unshare -urm; mount -t tmpfs none /whatever; echo "you're home free"
```
