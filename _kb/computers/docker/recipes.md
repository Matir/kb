---
title: Docker Recipes
---

## MySQL In Docker

```
docker volume create mysql-data
docker run -d --name mysql-server \
    --mount source=mysql-data,target=/var/lib/mysql \
    -e MYSQL_ROOT_PASSWORD=foobarbaz \
    -p 3306:3306 \
    mysql:latest
```
