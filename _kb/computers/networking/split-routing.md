---
title: Split Routing
---

To get traffic from one service to bypass the default routing tables, we can
create a substitute routing table.

## Create New Routing Table ##

Create a new named routing table by creating a file like
`/etc/iproute2/rt_tables.d/redirect.conf` with the contents:

```
2 redirect
```

The table number is arbitrary, but 253-255 and 0 are reserved.  The name is
likewise arbitrary.

## Create Routes in New Table ##

If your routes you want to avoid haven't been created yet, this is easy:

```
ip route show table main | \
  while read rule ; do
    ip route add $rule table redirect
  done
```

You can also use grep to eliminate (for example) tunnel connections:

```
ip route show table main | grep -v tun | grep -v tap | \
  while read rule ; do
    ip route add $rule table redirect
  done
```

## Select Which Traffic Uses this Table ##

```
ip rule add fwmark 0x2 table redirect
```

Again, the value `0x2` is arbitrary, but `0x0` is reserved.

## Mark the appropriate traffic ##

As an example, this covers traffic coming from the SSH port (i.e., response
traffic to an SSH connection).

``` 
iptables -A PREROUTING -j CONNMARK --restore-mark
iptables -A PREROUTING -m mark ! --mark 0x0 -j ACCEPT
iptables -A PREROUTING -p tcp -m tcp --dport 22 -j MARK --set-mark 0x2
iptables -A PREROUTING -j CONNMARK --save-mark
iptables -A OUTPUT -j CONNMARK --restore-mark
iptables -A OUTPUT -m mark ! --mark 0x0 -j ACCEPT
iptables -A OUTPUT -p tcp -m tcp --sport 22 -j MARK --set-mark 0x2
iptables -A OUTPUT -j CONNMARK --save-mark
```

The `CONNMARK` lines use the connection tracking module to get all of the
packets in a single connection (as tracked by `nf_conntrack`) the same mark.
The mark value in the `--set-mark` statement should be the same as the value
used in the `ip rule` statement above.  `OUTPUT` rules are for the packets
originating from the local host.  `PREROUTING` rules are for the packets coming
in from remote hosts.  (This initially sets up the connection tracking with the
mark.)

## Flush the Cache ##

```
ip route flush cache
```

This clears any cached routes.

## References ##

* https://arstechnica.com/civis/viewtopic.php?f=16&t=1195455
* http://linux-ip.net/html/routing-tables.html
