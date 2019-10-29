---
title: Google Cloud Platform (GCP)
---

## Configurations ##

[Configurations](https://cloud.google.com/sdk/gcloud/reference/config/configurations/)
are conceptually similar to virtualenvs or other "containers" of configuration
data.

### Creating a new Config ###

`gcloud config configurations create <name>` creates a new named configuration.

### Activating a Config ###

`gcloud config configurations activate <name>` changes the default config for
all gcloud commands.

Setting the environment variable `CLOUDSDK_ACTIVE_CONFIG_NAME` sets
configuration for as long as the variable is set.

`gcloud --configuration=<name>` uses an alternative configuration for one
command.
