---
title: Wireless Networking
---

## hostapd config

This is a config that works on a Raspberry Pi 4 for a 802.11g network:

```
country_code=US
interface=wlan0
ssid=SSID_HERE
hw_mode=g
channel=1
ieee80211n=0
wmm_enabled=1
auth_algs=1
wpa=2
wpa_key_mgmt=WPA-PSK
rsn_pairwise=CCMP
wpa_passphrase=PASSPHRASE_HERE
logger_syslog=-1
logger_syslog_level=1
driver=nl80211
```
