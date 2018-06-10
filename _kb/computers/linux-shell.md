---
title: Linux Shell
---

## Keybindings ##

|------------------------------|-----------------|----------------|
| Action                       | Emacs Mode      | Vi Mode        |
|------------------------------|-----------------|----------------|
| Switch to this mode (bash)   | `set -o emacs`  | `set -o vi`    |
| Switch to this mode (zsh)    | `bindkey -e`    | `bindkey -v`   |
|------------------------------|-----------------|----------------|

## Common Variables ##

|----------|------------------------------------------------|
| Variable | Definition                                     |
|----------|------------------------------------------------|
| `$$`     | Process ID of Shell                            |
| `$*`     | All arguments `$1`..                           |
| `"$*"`   | All arguments `$1`.. as a single quoted string |
| `$@`     | All arguments `$1`..                           |
| `"$@"`   | All arguments `$1`.., individually quoted      |
| `$!`     | Process ID of last created background process  |
| `$?`     | Return value of last statement                 |
|----------|------------------------------------------------|
