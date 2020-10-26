---
title: Get Info from gpg-agent
---

Get everything known about current keys:

```
gpg-connect-agent 'keyinfo --list --with-ssh --ssh-fpr=sha256' /bye
```
