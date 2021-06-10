---
title: Windows PostEx
tags:
  - Cheatsheet
---

## Windows Local PostEx ##

### File Reads ###

`%SYSTEMDRIVE%\boot.ini`
: Found on almost every windows machine, and a good
  file for checking that your read is working.

`%WINDIR%\win.ini`
: A good backup for `boot.ini`.

`%WINDIR%\System32\drivers\etc\hosts`
: Network hosts file.

### Basic Commands ###

`whoami` (`whoami /all`)
: Shows information about the current user and privileges.

`set`
: Shows information about currently set environment variables.  Can
  leak quite a bit of useful information.

### Networking Commands ###

`ipconfig /all`
: Displays the full information about your NIC’s.

`ipconfig /displaydns`
: Displays your local DNS cache.

`netstat -nabo`
: Lists ports / connections with corresponding process (`-b`), don’t perform
  looking (`-n`), all connections (`-a`) and owning process ID (`-o`)

`netstat -r`
: Displays the routing table.

`netstat -na | findstr :445`
: Find all listening ports and connections on port 445.

`netstat -nao | findstr LISTENING`
: Find all listening ports and their associated PIDs.

`net view`
: Uses NBNS/SMB to try to find all hosts in workgroup/domain.

`net view /domain`
: List all domains available to the host.

`net view /domain:otherdomain`
: Queries NBNS/SMB to try to find all hosts in the other domain.

`net user /domain`
: Lists all of the domain users.

`net accounts`
: Print the local password policy.

`net accounts /domain`
: Print the domain password policy.

`net localgroup administrators`
: Print the members of the local group administrators.

`net localgroup administrators /domain`
: Bizarrely gets the domain administrators.

`net group "Domain Admins" /domain`
: Print the members of the Domain Admins group.

`net share`
: Display the current shared SMB services.

`arp -a`
: Print the ARP table.

`route print`
: Print the routing table.  See also `netstat -r`.

`netsh wlan`
: Manipulate wireless profiles.

`wmic ntdomain list`
: Get information about the domain and domain controller.

### Configuration ###

`gpresult /z`
: Get current GPO settings for the current system and user.

`sc qc <svc>`
: Get the configuration of a service, including the binary path, user, and
  startup settings.

`sc query`
: Get a list of all services.

### Stored Credentials ###

Unattended installation creds:

```
C:\unattend.xml
C:\Windows\Panther\Unattend.xml
C:\Windows\Panther\Unattend\Unattend.xml
C:\Windows\system32\sysprep.inf
C:\Windows\system32\sysprep\sysprep.xml
```

These can be found with the metasploit module `post/windows/gather/enum_unattend`.

Find passwords in files:

```
findstr /si password *.txt
findstr /si password *.xml
findstr /si password *.ini
```

Find files with pass in the name:

```
dir /b /s *pass*
```

Other credential types:

- PuTTY: `reg query "HKCU\Software\SimonTatham\PuTTY\Sessions"`
- RealVNC: `reg query HKEY_LOCAL_MACHINE\SOFTWARE\RealVNC\WinVNC4 /v password`
- Windows AutoLogin: `reg query "HKLM\SOFTWARE\Microsoft\Windows NT\Currentversion\Winlogon"`
- SNMP: `reg query "HKLM\SYSTEM\Current\ControlSet\Services\SNMP"`

## Windows Domain PostEx ##

### Grab Hashes ###

* Use [Responder](https://github.com/lgandx/Responder) to grab hashes.

### Get Local Credentials ###

* [Windows Credential
  Editor](https://www.ampliasecurity.com/research/windows-credentials-editor/)
  extracts login credentials for Windows XP, 2003, Vista, 7, 2008 and Windows 8.
* [Mimikatz](https://github.com/gentilkiwi/mimikatz) is also a credential dumper
  for a variety of credential types.  It's now well known to extract plaintexts
  passwords, hash, PIN code and kerberos tickets from memory. mimikatz can also
  perform pass-the-hash, pass-the-ticket or build Golden tickets.

### Using Hashes ###

<!-- TODO: expand this -->

* psexec
* Pass the Hash
* Kerberoasting
* NTLM Relaying

## Windows Postexploitation Tools ##

<!-- TODO: expand this -->

* Bloodhound
* Powershell Empire
* Pupy
* Mimikatz
* Responder
* SETH
* [WinPEAS](https://github.com/carlospolop/privilege-escalation-awesome-scripts-suite/tree/master/winPEAS) -- Enumerate possible privilege escalation options

## Resources ##

* [Room362 Windows Postex List](https://docs.google.com/document/d/1U10isynOpQtrIK6ChuReu-K1WHTJm4fgG3joiuz43rw/edit?hl=en_US)
* [PentestLab Stored Credentials](https://pentestlab.blog/2017/04/19/stored-credentials/)
* [LOLBAS](https://lolbas-project.github.io/#) -- Living off the Land
* [AD Security](https://adsecurity.org/)
* [Windows Privilege Escalation](https://github.com/swisskyrepo/PayloadsAllTheThings/blob/master/Methodology%20and%20Resources/Windows%20-%20Privilege%20Escalation.md#eop---looting-for-passwords)
