---
title: ChromeOS Setup
---

## Terminal (Secure Shell App) ##

### Solarized Palette ###

* `color-palette-override`
  * `{"0":"#073642","1":"#dc322f","2":"#859900","3":"#b58900","4":"#268bd2","5":"#d33682","6":"#2aa198","7":"#eee8d5","8":"#002b36","9":"#cb4b16","10":"#586e75","11":"#657b83","12":"#839496","13":"#6c71c4","14":"#93a1a1","15":"#fdf6e3"}`
* `background-color`
  * `#002b36`
* `cursor-color`
  * `#eee8d5`
* `foreground-color`
  * `#eee8d5`

### Inconsolata Font ###

* `user-css`
  * `https://cdn.jsdelivr.net/gh/wernight/powerline-web-fonts@ba4426cb0c0b05eb6cb342c7719776a41e1f2114/PowerlineFonts.css`
* `font-family`
  * `Inconsolata`,...

### Load from Network ###

`Ctrl+Shift+J` in console to open developer tools.

`fetch('https://raw.githubusercontent.com/Matir/skel/master/chromeos/hterm.json').then(function(r){r.json().then(function(j){term_.prefs_.importFromJson(j)})})`
