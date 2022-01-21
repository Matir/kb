---
title: Network Manager with dnsmasq
---

## Enabling

In `/etc/NetworkManager/NetworkManager.conf`, add `dns=dnsmasq` to `[main]`
section.

## Config

For "shared" connections (offering DHCP), configs can be dropped in
`/etc/NetworkManager/dnsmasq-shared.d/`.  For all other connections (the common
case), additional configs can be dropped in `/etc/NetworkManager/dnsmasq.d/`.

## Dynamic Hosts

Add file to source hosts dir in `dnsmasq.d`:

```
hostsdir=/etc/dnshosts
```

```
mkdir /etc/dnshosts
chown root:dnsadm /etc/dnshosts
chmod 2775 /etc/dnshosts
```

Allows users in the `dnsadm` group to administer hosts resolved by dnsmasq.
