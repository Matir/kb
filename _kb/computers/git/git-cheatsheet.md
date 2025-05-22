---
title: Git Cheatsheet/Recipes
---

## Diffing/Comparison

### See commits in a branch but not in main

`git log BRANCH ^main`

### Diff what would happen in a merge

`git diff --merge-base main TARGET_BRANCH`
