---
title: Port Forwarding on Windows
---

From [Microsoft Documentation](https://docs.microsoft.com/en-us/windows-server/networking/technologies/netsh/netsh-interface-portproxy):

```
netsh interface portproxy add v4tov4 listenaddress=localaddress listenport=localport connectaddress=destaddress connectport=destport
```

For example, to forward to an internal webserver:

```
netsh interface portproxy add v4tov4 listenaddress=192.168.1.1 listenport=8000 connectaddress=192.168.2.1 connectport=80
```
