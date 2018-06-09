---
title: Computer Setup
---

Setting up my environment on a new (Debian-derivative) Linux Box:

```
apt-get update && apt-get install -y vim zsh tmux git
git clone --depth=1 https://github.com/Matir/skel.git ${HOME}/.skel
sh ${HOME}/.skel/install.sh
```
