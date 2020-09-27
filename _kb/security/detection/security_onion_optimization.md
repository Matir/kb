---
title: Security Onion Optimization
---

### Logstash Configuration

Limit memory in `/etc/elasticsearch/jvm.options` and
`/etc/logstash/jvm.options`:

```
-Xms200m
```

Limit logstash workers in `/etc/logstash/logstash.yml`:

```
pipeline.workers: 1
```
