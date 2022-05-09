---
title: Makefiles
---

## Common Recipes

**Compile a bunch of files from the dependencies:**

```make
# Results in COMMAND -o foo -- bar baz bang
foo: bar baz bang
  COMMAND -o $@ -- $^
```

**Describe how to make a .o from a .c**

```make
%.o: %.c
  gcc -c -o $^ $<
```

## References

* [Automatic Variables](https://www.gnu.org/software/make/manual/html_node/Automatic-Variables.html)
