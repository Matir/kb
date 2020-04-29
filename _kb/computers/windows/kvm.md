---
title: Windows VMs
---

## Improving CPU Usage on KVM ##

By default, Windows starts polling the timer.  Inform it that a virtualized
timer is available:

```
<clock offset='localtime'>
    <timer name='hpet' present='yes'/>
    <timer name='hypervclock' present='yes'/>
</clock>
```
