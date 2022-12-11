---
title: Kali on Raspberry Pi
---

## First Boot

### Network Config

`/usr/bin/copy-user-wpasupplicant.sh` is invoked IFF `/boot/wpa_supplicant.conf`
exists.

If `nmcli` exists, we try to use it instead.  `#psk` comment will be used as
plaintext.

See also: [WPA CLI Config](https://jonathansblog.co.uk/kali-linux-wpa_supplicant-cli-config)

### SSH Enable

Create `/boot/ssh` or `/boot/ssh.txt` and it will enable SSH on boot.
