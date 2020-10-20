---
title: QR Codes for Wireless Configuration
---

### Open Network

```
echo "WIFI:S:myssid;;" | qrencode
```

### WPA2 PSK Network

```
echo "WIFI:T:WPA;S:myssid;P:secrets;;" | qrencode
```
