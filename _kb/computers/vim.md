---
title: Vim
---

## Insert a file at Current Position ##

In `command` mode, use `:r <filename>` to read a file in and insert at the
current position.

### Insert stdout of a command instead ###

Just begin with a `!` and the command instead of a filename.

## Operations ##

|---------|-----------------------------------------------|
| Command | Operation                                     |
|---------|-----------------------------------------------|
| a       | **Append** after current position             |
| A       | **Append** at end of line                     |
| i       | **Insert** at current position                |
| o       | **Insert** next line                          |
|---------|-----------------------------------------------|

## Movement/Target Commands ##

|---------|-----------------------------------------------|
| Command | Operation                                     |
|---------|-----------------------------------------------|
| iw      | Entire word under cursor                      |
| w       | From cursor to end of current word            |
|---------|-----------------------------------------------|

## Miscellaneous Commands ##

Various things I end up using (and often forgetting):

|---------|---------|-------------------------------------|
| Command | Mode    | Operation                           |
|---------|---------|-------------------------------------|
| ciw     | Normal  | Replace word currently under cursor |
|---------|---------|-------------------------------------|

## Using ctags ##

After generating a tag file:

|---------|---------|-------------------------------------|
| Command | Mode    | Operation                           |
|---------|---------|-------------------------------------|
| ^]      | Normal  | Jump to definition |
| ^t      | Normal  | Jump to previous point |
|---------|---------|-------------------------------------|
