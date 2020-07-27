---
title: Bridging on Linux
---

## Making sure IPTables doesn't apply to bridging ##

Temporarily:

```
sysctl -w net.bridge.bridge-nf-call-arptables=0
sysctl -w net.bridge.bridge-nf-call-iptables=0
sysctl -w net.bridge.bridge-nf-call-ip6tables=0
sysctl -w net.bridge.bridge-nf-filter-vlan-tagged=0
sysctl -w net.bridge.bridge-nf-filter-pppoe-tagged=0
```

Permanently:

```
mkdir -p /etc/sysctl.d
cat > /etc/sysctl.d/40-unfilter-bridge.conf <<EOF
# Prevent bridges from calling iptables
net.bridge.bridge-nf-call-arptables=0
net.bridge.bridge-nf-call-iptables=0
net.bridge.bridge-nf-call-ip6tables=0
net.bridge.bridge-nf-filter-vlan-tagged=0
net.bridge.bridge-nf-filter-pppoe-tagged=0
EOF
sysctl -p /etc/sysctl.d/40-unfilter-bridge.conf
```

## Passing all Bridge Traffic ##

Because docker prefers to have `bridge-nf-call-iptables` set to `1`, you can
alternatively add rules to allow all bridge-to-bridge traffic to cross iptables:

```
iptables -A FORWARD -i br-lab -o br-lab -j ACCEPT
```

## Passing 802.1x traffic over a bridge ##

[Source](https://www.gremwell.com/linux_kernel_can_forward_802_1x)

```
echo 8 > /sys/class/net/br*/bridge/group_fwd_mask
```

## Turning a Bridge into a Hub ##

(All traffic reflected to all ports.)

```
brctl setageing <bridge> 0
```

Or with iproute2:

```
ip link set <bridge> type bridge ageing_time 0
```
