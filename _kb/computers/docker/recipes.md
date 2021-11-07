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

## MariaDB in Docker

```
docker run -d --rm -p 3306:3306 --name wpdb \
  -e MARIADB_USER=wordpress \
  -e MARIADB_PASSWORD=wppass \
  -e MARIADB_DATABASE=wordpress \
  -e MARIADB_RANDOM_ROOT_PASSWORD=yes \
  mariadb:latest
```

## Wordpress in Docker

* Needs MySQL/MariaDB as above

```
docker run -d --rm -p 8123:80 --name wordpress \
  -e WORDPRESS_DB_HOST=192.168.10.209 \
  -e WORDPRESS_DB_NAME=wordpress \
  -e WORDPRESS_DB_USER=wordpress \
  -e WORDPRESS_DB_PASSWORD=wppass \
  wordpress
```
