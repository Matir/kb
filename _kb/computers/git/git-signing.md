---
title: Git Signing
---

## Sign a commit

```
git commit -S
```

## Sign a tag

```
git commit -s tagname -m 'message'
```

## Verify signed tag

```
git tag -v tagname
```

## Verify signed commit

For last commit:

```
git log --show-signature -1
```

In a short log (`%G?`):

```
git log --pretty="format:%h %G? %aN  %s"
```
