---
title: IPTables Connection Forwarding
---

This is basically an in-kernel connection proxy.

```
echo 1 > /proc/sys/net/ipv4/ip_forward
iptables -P FORWARD DROP
PROXY_IP=10.1.1.1
PROXY_PORT=4444
TARGET_IP=10.2.2.2
TARGET_PORT=6666

iptables -A FORWARD -p tcp -d ${TARGET_IP} --dport ${TARGET_PORT} -j ACCEPT
iptables -A FORWARD -m state --state ESTABLISHED,RELATED -j ACCEPT
iptables -t nat -A PREROUTING --dst ${PROXY_IP} -p tcp --dport ${PROXY_PORT} \
    -j DNAT --to-destination ${TARGET_IP}:${TARGET_PORT}
iptables -t nat -A POSTROUTING -p tcp --dst ${TARGET_IP} \
    --dport ${TARGET_PORT} -j SNAT --to-source ${PROXY_IP}
iptables -t nat -A OUTPUT --dst ${PROXY_IP} -p tcp --dport ${PROXY_PORT} \
    -j DNAT --to-destination ${TARGET_IP}:${TARGET_PORT}
```
