---
LUKS on KVM
---

**Currently, only LUKSv1 is supported.**

Create a secret:
```
<secret ephemeral='no' private='yes'>
   <description></description>
   <usage type='volume'>
      <volume>/vms/PATH</volume>
   </usage>
</secret>

virsh secret-define volume-secret.xml
```

Populate the secret:
```
virsh secret-set-value UUID --file FILE --plain
Secret value set
```

Modifications to Domain XML if underlying device is a file:
```
    <disk type='file' device='disk'>
      <driver name='qemu' type='raw'/>
      <source file='/vms/PATH'>
        <encryption format='luks'>
          <secret type='passphrase' uuid='SECRET_UUID'/>
        </encryption>
      </source>
      <target dev='vdb' bus='virtio'/>
    </disk>
```

Modifications to Domain XML if underlying device is a block device/LV:
```
    <disk type='block' device='disk'>
      <driver name='qemu' type='raw'/>
      <source dev='/vms/PATH'>
        <encryption format='luks'>
          <secret type='passphrase' uuid='SECRET_UUID'/>
        </encryption>
      </source>
      <target dev='vdb' bus='virtio'/>
    </disk>
```

### Full Setup Cycle

```
pwgen 32 1 > testkey
lvcreate -L20G -ndtest-luks pool1
cryptsetup luksFormat --type luks1 /dev/mapper/pool1-dtest--luks testkey
cat <<EOF | virsh secret-define /dev/stdin
<secret ephemeral='no' private='yes'>
   <description></description>
   <usage type='volume'>
      <volume>/dev/mapper/pool1-dtest--luks</volume>
   </usage>
</secret>
EOF
Secret 105d8a13-53d5-4e1f-8dd1-8d7f6c68f5ef created
virsh secret-set-value 105d8a13-53d5-4e1f-8dd1-8d7f6c68f5ef --file testkey
cat <<EOF | virsh attach-device --config dtest /dev/stdin
>     <disk type='block' device='disk'>
      <driver name='qemu' type='raw'/>
      <source dev='/dev/mapper/pool1-dtest--luks'>
        <encryption format='luks'>
          <secret type='passphrase' uuid='105d8a13-53d5-4e1f-8dd1-8d7f6c68f5ef'/>
        </encryption>
      </source>
      <target dev='vdb' bus='virtio'/>
    </disk>
EOF
```
