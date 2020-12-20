---
title: Hash Pattern Extraction
---

### MD5 ###

```
egrep -oE '(^|[^a-fA-F0-9])[a-fA-F0-9]{32}([^a-fA-F0-9]|$)' *.txt | egrep -o '[a-fA-F0-9]{32}' > md5-hashes.txt
sed -rn 's/.*[^a-fA-F0-9]([a-fA-F0-9]{32})[^a-fA-F0-9].*/1/p' *.txt > md5-hashes
```

Adjust length for SHA-1, SHA-256, etc.

### MySQL-Old ###

```
grep -e "[0-7][0-9a-f]{7}[0-7][0-9a-f]{7}" *.txt > mysql-old-hashes.txt
```

### blowfish ###

```
grep -e "$2a\$\08\$(.){75}" *.txt > blowfish-hashes.txt
```

### Joomla ###

```
egrep -o "([0-9a-zA-Z]{32}):(w{16,32})" *.txt > joomla.txt
```

### VBulletin ###

```
egrep -o "([0-9a-zA-Z]{32}):(S{3,32})" *.txt > vbulletin.txt
```

### phpBB3

```
egrep -o '$H$S{31}' *.txt > phpBB3-md5.txt
```

### Wordpress-MD5

```
egrep -o '$P$S{31}' *.txt > wordpress-md5.txt
```

### Drupal 7

```
egrep -o '$S$S{52}' *.txt > drupal-7.txt
```

### Unix-md5

```
egrep -o '$1$w{8}S{22}' *.txt > md5-unix-old.txt
```

### md5-apr1

```
egrep -o '$apr1$w{8}S{22}' *.txt > md5-apr1.txt
```

### sha512crypt

```
egrep -o '$6$w{8}S{86}' *.txt > sha512crypt.txt
```
