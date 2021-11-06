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
