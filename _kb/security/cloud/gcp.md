---
title: GCP Cloud Security
---

## Retrieve Info about Service Account Token

```
oauth2l info --token \
  $(curl "http://metadata.google.internal/computeMetadata/v1/instance/service-accounts/default/token"
    -H "Metadata-Flavor: Google" | jq -r '.access_token')
```

## Resources

* [GCP Pentesting Guide](https://slashparity.com/?p=938)
