---
title: Nmap
---

Quick scan with all features, most common ports, log to all 3 output formats:

```
nmap -Pn -F -A -T4 -oA scan_results $TARGET
```

Thorough scan, internet speed.

```
nmap -Pn -p- -sV -T3 -sS -oA scan_results $TARGET
```

## Companion Tools

* [nmap-parse-output](https://github.com/ernw/nmap-parse-output) - Shell plugin
  to parse output from nmap.
