---
title: File Encryption
---

## Using OpenSSL

With OpenSSL, the parameters are not embedded in the resulting file, so you need
to know the same parameters when decrypting.  (Parameters include the cipher,
the message digest, and any KDF parameters.)

Encrypting:

```
openssl enc -aes-256-cbc -md sha512 -iter 100000 -in foo -out foo.enc
```

Decrypting:

```
openssl enc -d -aes-256-cbc -md sha512 -iter 100000 -in foo.enc -out foo
```

## Using GnuPG

Encrypting:

```
gpg -c < secrets.txt > secrets.txt.enc
```

Decrypting:

```
gpg -d < secrets.txt.enc > secrets.txt
```

## Using age

This uses [`age`](https://github.com/FiloSottile/age) which is designed around
modern crypto.  Unlike OpenSSL or GnuPG, it doesn't try to be a swiss army knife
of crypto, and is only for using modern crypto on files.

Encrypting:

```
age -p secrets.txt > secrets.txt.age
```

Decrypting:

```
age -d secrets.txt.age > secrets.txt
```
