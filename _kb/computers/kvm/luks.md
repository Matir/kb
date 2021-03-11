---
LUKS on KVM
---



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
virsh secret-set-value UUID --file --plain FILE
Secret value set
```

Modifications to Domain XML:
```
    <disk type='file' device='disk'>
      <driver name='qemu' type='raw'/>
      <source file='/vms/PATH'>
        <encryption format='luks'>
          <secret type='passphrase' uuid='SECRET_UUID'/>
        </encryption>
      </source>
      <target dev='vdb' bus='virtio'/>
      <address type='pci' domain='0x0000' bus='0x07' slot='0x00' function='0x0'/>
    </disk>
```
