---
title: tmux
---

## Plugins ##

There's a script that allows `tmux` to support and load plugins (which are, of
course, just managed scripts themselves.)  [tmux Plugin
Manager](https://github.com/tmux-plugins/tpm)

## Replacements ##

Some commands can have expansions in them.  These commands include:

* `pipe-pane`
* `status-left`

Variables can be replaced:

```
string will be passed through strftime(3) before being used.
string may contain any of the following special character sequences:

#(shell-command) -- First line of the command's output
#[attributes] -- Colour or attribute change
#H -- Hostname of local host
#h -- Hostname of local host without the domain name
#F -- Current window flag
#I -- Current window index
#D -- Current pane unique identifier
#P -- Current pane index
#S -- Session name
#T -- Current pane title
#W -- Current window name
## -- A literal `#'

The #(shell-command) form executes `shell-command' and inserts the first line of its output.
```

## Shared Session ##

If both clients are to be run by the same user on the same machine, this is
simple:

```
tmux new-session -s <session_name>
tmux attach-session -t <session_name>
```

From different users, it gets a little more complex.  Anyone in a shared group
will be able to access the session.

```
tmux -S /tmp/shared-session new-session -s <session_name>
chgrp <common_group> /tmp/shared-session
tmux -S /tmp/shared-session attach -t <session_name>
```

The second session can be readonly by providing the `-r` flag when attaching to
the session.
