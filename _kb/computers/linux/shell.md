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

## Logging I/O in the Shell ##

Using the script command:

```
script $(date -I).$$.log
```

### tmux ###

`tmux` lacks native support, but there's a great [`tmux-logging`
plugin](https://github.com/tmux-plugins/tmux-logging).

Alternatively, there's a keybinding that can be used with the `tmux` `pipe-pane`
command:

```
bind-key H pipe-pane -o "exec cat >>$HOME/'#W-tmux.log'" \; display-message 'Toggled logging to $HOME/#W-tmux.log'
```

Other replacements can be seen in `tmux(1)` or [tmux notes](/computers/tmux).

### GNU Screen ###

`screen` can easily log.  From within a screen session, press the command
character (default `^A`) and then:

```
:log <name of log>
```

## Cool Shell Utilities ##

* [bat](https://github.com/sharkdp/bat) - A modern take on `cat`.
* [modern-unix](https://github.com/ibraheemdev/modern-unix) - List of "modern
  unix" utilities.
* [starship](https://starship.rs/) - A modern cross-shell prompt.
