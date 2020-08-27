---
title: Linux Networking
---

## Mirror Traffic from Interface to Interface

```
SRC_IF=eth0
DST_IF=eth1
tc qdisc add dev "${SRC_IF}" ingress
tc filter add dev "${SRC_IF}" parent ffff: protocol all u32 match u8 0 0 action mirred egress mirror dev "${DST_IF}"
```
