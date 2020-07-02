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
