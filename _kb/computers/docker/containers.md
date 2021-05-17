---
title: Useful Docker Containers
---

## Jupyter

```
docker run -d --name jupyter \
  -p 8888:8888 \
  --mount source=jupyter-data,target=/home/jovyan/work \
  jupyter/scipy-notebook
```

## MySQL

```
docker volume create mysql-data
docker run -d --name mysql-server \
    --mount source=mysql-data,target=/var/lib/mysql \
    -e MYSQL_ROOT_PASSWORD=foobarbaz \
    -p 3306:3306 \
    mysql:latest
```
