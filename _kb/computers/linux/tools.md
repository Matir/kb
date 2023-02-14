---
title: Useful Linux Tools
---

## Terminal Emulation/Useful for Terminal

* [Terminator Terminal Emulator](https://gnome-terminator.org/) -
  Nice way to split terminals, etc.

## CLI Tools

* [duf](https://github.com/muesli/duf) - Disk Usage/Free Utility
* [gf](https://github.com/tomnomnom/gf) - A Wrapper Around Grep
* [unfurl](https://github.com/tomnomnom/unfurl) - Parse URLs on the command line.
* [gron](https://github.com/tomnomnom/gron) - Make JSON greppable.
* [jq](https://stedolan.github.io/jq/) - Structured JSON querying.
* [bat](https://github.com/sharkdp/bat) - cat, but pretty
* [delta](https://github.com/dandavison/delta) - better diff viewer
* [dust](https://github.com/bootandy/dust) - better disk usage viewer
* [ripgrep](https://github.com/BurntSushi/ripgrep) - extremely fast grep
* [ag](https://github.com/ggreer/the_silver_searcher) - code-specific search
* [sd](https://github.com/chmln/sd) - sed alternative for find and replace
* [tldr](https://github.com/tldr-pages/tldr) - Practical examples for man pages
* [procs](https://github.com/dalance/procs) - Modern replacement for ps
* [httpie](https://github.com/httpie/httpie) - Modern command-line client for
  HTTP.

## Prompts/Shell Frameworks

* [Starship](https://starship.rs/) - Powerful, configurable, prompt written in Rust.
* [oh-my-zsh](https://ohmyz.sh/) - Customizable shell framework for `zsh`.

## Modern/Improved Standard Tools

* File Listing
    * [exa](https://the.exa.website/) - Not a drop-in replacement for ls, but an
      improvement. (Debian: `exa`; Arch: `exa`)
    * [lsd](https://github.com/Peltoche/lsd) - `ls` with colors/icons/tree-view and more.
* File and diff browsing (Arch: `lsd`)
    * [bat](https://github.com/sharkdp/bat) - Syntax highlighting, diff-aware
      version of `cat`. (Debian: `bat`; Arch: `bat`)
* Process Management
    * [procs](https://github.com/dalance/procs) - Nicer process listing with
      color coding, tree view, and more. (Arch: `procs`)
    * [bottom](https://github.com/ClementTsang/bottom) - Nice graphical
      alternative to `top`. (Arch: `bottom`)
    * [glances](https://github.com/nicolargo/glances) - Quick overview of system
      status. (Debian: `glances`; Arch: `glances`)
    * [gtop](https://github.com/aksakalli/gtop) - Another GUI in terminal system monitor.
* Finding Files/File Content (`grep`)
    * [ripgrep](https://github.com/BurntSushi/ripgrep) - Much faster `grep` that
      is `gitignore` aware and ignores binaries. (Debian: `ripgrep`; Arch:
      `ripgrep`)
    * [ag](https://github.com/ggreer/the_silver_searcher) - AKA "The Silver
      Searcher" - Faster version of `ack` in C. (Arch: `the_silver_searcher`)
    * [ack](https://beyondgrep.com/) - `ack-grep` is an improved `grep` intended
      for source code searching. (Debian: `ack`; Arch: `ack`)
    * [fd](https://github.com/sharkdp/fd) - Faster version of find, color
      highlighting, `gitignore` aware. (Arch: `fd`)
    * [fzf](https://github.com/junegunn/fzf) - Fuzzy file finder. (Debian:
      `fzf`; Arch: `fzf`)
* Network Tools
    * [dog](https://github.com/ogham/dog) - More user-friendly version of `dig`.
      Can emit `JSON`. (Arch: `dog`)
* Disk Usage
    * [duf](https://github.com/muesli/duf) - Cleaner version of `df`, with ASCII
      graphs, color highlighting, grouping by filesystem type. (Debian: `duf`;
      Arch: `duf`)
    * [dust](https://github.com/bootandy/dust) - `du` alternative in rust,
      showing cumulutative usage and ASCII graphs. (Arch: `dust`)
* Text Editing/Processing
    * [sd](https://github.com/chmln/sd) - Find & replace specific tool, intended
      as a nicer `sed` for the common case. (Arch: `sd`)
    * [difftastic](https://github.com/Wilfred/difftastic) - Syntax-aware
      structural `diff` tool. (Arch: `difftastic`)
    * [delta](https://github.com/dandavison/delta) - Highlighting drop-in
      replacement for `diff`. (Debian: `git-delta`; Arch: `git-delta`)
    * [choose](https://github.com/theryangeary/choose) - A human-friendly
      alternative to `cut`/`awk`. (Arch: `choose`)

## General Purpose/Power Tools

* HTTP/Network Tools
    * [httpie](https://github.com/httpie/httpie) - User-friendly http client for
      the API era. (Debian: `httpie`; Arch: `httpie`)
    * [curlie](https://github.com/rs/curlie) - Power of `curl`, the ease of
      `httpie`. (Arch: `curlie`)
    * [xh](https://github.com/ducaale/xh) - Performant alternative to `httpie`.
      (Arch: `xh`)
* Pipelines/Data Processing
    * [jq](https://stedolan.github.io/jq/) - A command line processor for JSON.
      Very powerful for processing JSON in/out. (Debian: `jq`; Arch: `jq`)
    * [nushell](https://www.nushell.sh/) - A shell specifically for processing pipelines of data. Cross-platform. **Not syntax-compatible with other
    shells.** (Arch: `nushell`)
    * [fq](https://github.com/wader/fq) - Decoders for working with binary data
      on the CLI. (Debian: `fq`; Arch: `fq`)
* Shell Management
    * [mcfly](https://github.com/cantino/mcfly) - Shell history
      browser/manipulator. (Arch: `mcfly`)
    * [zoxide](https://github.com/ajeetdsouza/zoxide) - Smarter `cd` (i.e.,
      replace in your path, etc.) (Arch: `zoxide`)

## Cheat Sheets/Documentation

* [tldr](https://github.com/tldr-pages/tldr) - Practical examples of various
  commands. (Debian: `tldr-py`; Arch: `tldr`)
* [cheat](https://github.com/cheat/cheat) - Interactive cheatsheet manager.
