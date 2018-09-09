---
title: XXE
---

### Testing

Testing with python:

```
doc = etree.parse(open('/tmp/tmp.xml'), etree.XMLParser(resolve_entities=True,no_network=False))
```
