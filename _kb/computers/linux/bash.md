---
title: Bash
---

(Much of this also works in ZSH)

## Scripting

### Traps

You can add handling for exceptional cases (signals) as well as errors and exit.

```
trap "{echo ERR}" SIGINT SIGTERM ERR EXIT
```

Signals are fairly self-explanatory, EXIT is triggered on a normal exit (code
0), and ERR is triggered on a non-zero exit.

### Duplicating data without files on disk

Sometimes you want to use the output of a command and a bash variable is not
suitable (e.g., might contain special characters, etc.)

```
TESTD=$(mktemp -d)
mkfifo -m 0700 ${TESTD}/f1
mkfifo -m 0700 ${TESTD}/f2

(cat ${TESTD}/f1; cat ${TESTD}/f2) &

SOMECOMMAND | tee ${TESTD}/f1 | tee ${TESTD}/f2 >/dev/null

```
