---
title: IPTables/NFTables
include:
  - /computers/networking/iptables_proxy
---

## NFTables

### Resources

* [Migrating from iptables to nftables](https://wiki.nftables.org/wiki-nftables/index.php/Moving_from_iptables_to_nftables)

## IPTables

### Port Forwarding

Something like:

```
iptables -t nat -A PREROUTING -i eth0 -p tcp --dport 4040:4049 -j DNAT --to-destination 10.13.37.4
```

Forwards ports 4040-4049 to 10.13.37.44
