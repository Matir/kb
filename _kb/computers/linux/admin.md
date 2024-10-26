---
title: Linux Admin
---

## Block Devices

### lsblk

** Output Formatting **

* default: `lsblk -o NAME,MAJ:MIN,RM,SIZE,RO,TYPE,MOUNTPOINTS`
* size & type info: `lsblk -o NAME,RM,SIZE,RO,TYPE,FSTYPE,FSUSE%,MOUNTPOINTS`
* label & transport: `lsblk -o NAME,RM,SIZE,RO,TYPE,TRAN,FSTYPE,LABEL,MOUNTPOINTS`
* model & serial info: `lsblk -o NAME,RM,SIZE,TYPE,TRAN,FSTYPE,LABEL,MODEL,SERIAL,MOUNTPOINTS`
