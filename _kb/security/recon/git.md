---
title: Git (Github)
---

GitHub can be a wealth of information.

## GitHub/Repos ##

* Things to look for
  * Hostnames
  * Credentials
    * SSL Keys
    * SSH Keys
    * Tokens
  * Application Configs

### General Strategy ###

* Find official repos
  * Look at history for deleted resources
* Find committers
* Look at other repos for leaks

## Tools ##

* [Gitrob](https://github.com/michenriksen/gitrob) -- Look for keys and
  sensitive files in repositories and present the results as a web interface.
* [truffleHog](https://github.com/dxa4481/truffleHog) -- digs through commit
  history and branches looking for secrets checked in
* [git-all-secrets](https://github.com/anshumanbh/git-all-secrets) -- search
  through multiple git repos and run scanners against them
* [github dorks](https://github.com/techgaun/github-dorks) -- search github for
  interesting information

### Git grep ###


