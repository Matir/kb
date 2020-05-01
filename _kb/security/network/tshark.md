---
title: TShark
---

TShark is the command line tool that built around wireshark's dissectors.  It
can perform much more complex filtering and extraction than tcpdump alone.

## TShark Recipes ##

### Dump DNS Queries ###

Dumps DNS queries with just timestamp and hostname:

```
tshark -f "port 53" -T fields -e frame.time_epoch -e dns.qry.name
```
