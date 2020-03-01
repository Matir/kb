---
title: Using `find`
---

### Find all setuid root binaries ###

```
find / -xdev -perm -4111 -type f -user root
```
