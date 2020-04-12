---
title: Various Pre-Setup Options
---

## Pi Zero `g_ether` Mode ##

1. Download the latest image.
2. Setup partitions from it.

    `sudo kpartx -av 2020-02-13-raspbian-buster-lite.g_ether.img`

3. Mount the FAT filesystem.

    `sudo mount /dev/mapper/loop0p1 /tmp/boot`

4. Enable Overlays in `/tmp/boot`

    `echo 'dtoverlay=dwc2,dr_mode=peripheral' >> config.txt`

5. Enable Kernel Options for `g_ether`.

    `sed -i 's/$/ modules-load=dwc2,g_ether/' cmdline.txt`

6. Enable sshd

    `touch ssh`

7. Unmount and cleanup.

    `cd ..;umount boot;kpartx -d 2020-02-13-raspbian-buster-lite.g_ether.img`

8. If no DHCP server is available, the pi will start with a link-local IP
   address.
