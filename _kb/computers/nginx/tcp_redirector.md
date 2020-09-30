---
title: Nginx TCP Redirector
---

Quick TCP redirector in nginx:

```
stream {
	server {
		listen 80;
		proxy_pass 192.168.0.2:80;
	}
}
```
