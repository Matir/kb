---
title: Fuzzing Documentation
---

## GoAhead

```
make CC=$(which afl-clang) DFLAGS=-DFUZZING ME_GOAHEAD_PAM=false

(printf 'GET / HTTP/1.1\r\nHost: localhost\r\n\r\n') | PREENY_DEBUG=0 PREENY_INFO=1 PREENY_ERROR=1 LD_PRELOAD=${HOME}/preeny/x86_64-linux-gnu/desock.so ./build/linux-x64-default/bin/goahead --home build/linux-x64-default/bin . :4444
```

Currently hangs on invalid request.
