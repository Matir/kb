---
title: XFCE
---

## Shortcuts

```
xfconf-query -c xfce4-keyboard-shortcuts -p /commands/custom/Print -s "/usr/bin/flameshot gui"
xfconf-query -c xfce4-keyboard-shortcuts -p '/commands/custom/<Alt>Print' -s "flameshot full -p $HOME/Pictures/Screenshots"
```
