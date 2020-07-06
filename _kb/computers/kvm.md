---
title: KVM
---

(Mostly KVM/libvirt combined.)

## Resize Running Disk

Use `virsh dumpxml` to find the disk device being used.  You need the `target`
`dev` attribute.

```
    <disk type='file' device='disk'>
      <driver name='qemu' type='qcow2'/>
      <source file='/vms/Plex-Media.qcow2' index='1'/>
      <backingStore/>
      <target dev='vdb' bus='virtio'/>
      <alias name='virtio-disk1'/>
      <address type='pci' domain='0x0000' bus='0x00' slot='0x07' function='0x0'/>
    </disk>
```

In this example, the device is `vdb`.

Next, run `virsh blockresize <domain> <device> <newsize>`, so to resize this
disk to 2.2TB, we use:

```
virsh blockresize Plex vdb 2200G
```

Check `dmesg` on the target domain, and if using virtio, you will see the driver
noticing the updated size:

```
[701165.855490] virtio_blk virtio3: [vdb] new size: 4613734400 512-byte logical blocks (2.36 TB/2.15 TiB)
[701165.855495] vdb: detected capacity change from 1932735283200 to 2362232012800
```

Using fdisk, check the old partition start point.  (That's important, as we'll
have to delete and recreate it.)  Then create a new partition starting *at the
same sector*.

```
fdisk /dev/vdb

Command (m for help): p                                                                         [132/846]

Disk /dev/vdb: 2.2 TiB, 2362232012800 bytes, 4613734400 sectors
Units: sectors of 1 * 512 = 512 bytes
Sector size (logical/physical): 512 bytes / 512 bytes
I/O size (minimum/optimal): 512 bytes / 512 bytes
Disklabel type: dos
Disk identifier: 0x86e1564f

Device     Boot Start        End    Sectors  Size Id Type
/dev/vdb1        2048 3774873599 3774871552  1.8T 83 Linux

Command (m for help): d
Selected partition 1
Partition 1 has been deleted.

Command (m for help): n
Partition number (1-128, default 1):
First sector (34-4613734366, default 2048): 2048
Last sector, +/-sectors or +/-size{K,M,G,T,P} (2048-4613734366, default 4613734366):

Created a new partition 1 of type 'Linux filesystem' and of size 2.2 TiB.
Partition #1 contains a ext4 signature.

Do you want to remove the signature? [Y]es/[N]o: n
```

Finally, resize your filesystem using the appropriate tool:

```
resize2fs /dev/vdb1
resize2fs 1.44.5 (15-Dec-2018)
Filesystem at /dev/vdb1 is mounted on /media/plex; on-line resizing required
old_desc_blocks = 113, new_desc_blocks = 138
The filesystem on /dev/vdb1 is now 576716539 (4k) blocks long.
```

## Display Resizing

`spice-vdagent` must be installed on the guest, and the spicevmc channel must be
enabled on the host.  Must close the spice display session and reopen it to
establish communications.

At some point, `spice-vdagent` changed to not resize itself, but send a
notification to the desktop environment.  Noted in a [stackoverflow
discussion](https://stackoverflow.com/questions/41990600/virt-manager-guest-resize-not-working) ([another](https://superuser.com/questions/1183834/no-auto-resize-with-spice-and-virt-manager))
as well as [Debian bug](https://bugs.debian.org/cgi-bin/bugreport.cgi?bug=858549#15),
and a [MATE Bug](https://github.com/mate-desktop/marco/issues/338).

Manual resizing can be done via:

```
xrandr --output Virtual-0 --auto
```

## virt-viewer to access Spice Console

```
virt-viewer -c qemu:///system Kali
virt-viewer -c qemu+ssh://scar/system Kali
```
