---
title: Useful AWK Commands
---

### Select lines between delimiters

For example, selecting private key from ovpn unified file.

```
awk '/<key>/{flag=1;next}/<\/key>/{flag=0}flag' file.ovpn
```
