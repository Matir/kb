---
title: tmux
---

## Plugins ##

There's a script that allows `tmux` to support and load plugins (which are, of
course, just managed scripts themselves.)  [tmux Plugin
Manager](https://github.com/tmux-plugins/tpm)

## New Detached Session ##

To start a new detached session (e.g., on reboot):

```
tmux new-session -d "command"
```

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

## Session Groups ##

tmux can have multiple sessions pointing to the same session group.  Normally
when you attach to an existing session, you get the same view in the exact same
place.  Multiple sessions to a session group gives you different views of the
same windows, so you can put them next to each other or use the various windows
from multiple terminal emulators.

Start a session, then attach a new session to the group:

```
tmux new-session -s <session_name>
tmux new-session -t <session_name>
```

Note that this is similar to attaching an existing session, but the
`new-session` command is used with the target of the existing session.

## Logging ##

### Module
See the [tmux-logging](https://github.com/tmux-plugins/tmux-logging) module.

### Saving Current Buffer

Press `^B, :` to get into the `tmux` command line.

```
capture-pane -S - ; save-buffer OUTFILE
```

## Updating SSH-Agent ##

For a remote SSH agent updater:

* [Happy ssh agent forwarding for tmux/screen](https://werat.github.io/2017/02/04/tmux-ssh-agent-forwarding.html)

Basically update a symlink on SSH then use the symlink socket:

`~/.ssh/rc`:

```sh
#!/bin/sh

if [ ! -S ~/.ssh/ssh_auth_sock ] && [ -S "$SSH_AUTH_SOCK" ]; then
    ln -sf $SSH_AUTH_SOCK ~/.ssh/ssh_auth_sock
fi
```

`~/.tmux.conf`:

```
set-environment -g 'SSH_AUTH_SOCK' ~/.ssh/ssh_auth_sock
```
