---
title: Minikube
---

### Proxy for SSH Port Forwarding

```
minikube kubectl -- proxy -p8001 -v5 --reject-paths=''
```

Certain paths are filtered by default, so `--reject-paths=''` is included to
disable this.  This will listen on port 8001 then forward to the local minikube
API server.  To access, SSH port forward via:

```
ssh -N -f -L8001:localhost:8001 user@host
```

Then to configure a local kubectl:

```
kubectl config set-cluster mk --server=http://localhost:8001/
kubectl config set-context mk --cluster=mk --namespace=default
kubectl config use-context mk
```

### Networking

Must start `minikube tunnel` to setup routing, but it doesn't setup `iptables`
for you.  A rule like the following, with the service network and the shared
bridge allows traffic to flow:

```
iptables -A FORWARD -d 192.168.70.0/24 -o br-14a4d8142278 -j ACCEPT
```
