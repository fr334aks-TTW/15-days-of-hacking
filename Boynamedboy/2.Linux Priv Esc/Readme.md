## Linux Priv Esc
>>> Welcome to the rootverse
- Privesc involves going from a lower permission account to a higher permission account, by either exploiting a vulnerability, design flow or configuration oversight in an OS or Application

## Enumeration
- Is the process of gathering info about a system or device you will/or have exploited.

### hostname
- **hostname** command returns name of target machine
e.g. SQL-PROD-01 as hostname may have juicy info about the machine.

### uname -a
- will print system info i.e kernel used. (useful esp. to find kernel exploits for priv esc)

### /proc/version
- provides info on target system processes.(may give info on kernel version, additional info.e.g.compiler installed gcc etc)

### /etc/issue
- contains info on OS.(**nb**it can be easily changed or customized)

### ps command
- is an effective way to see the running process on a linux system
```
ps -a			//view all running processes
ps axjf			//view process tree
```

### env
- the **env** command shows environmental variables(e.g. path variable may have a compiler or scripting language which can be used for priv esc)

### sudo -l
- Target may be configure to allow users to run some(or all) commands with root priviledges.
- used to list list commands the user can run using **sudo**

### ls
- used to list contents of a directory.
- use **ls -la** when looking for potential vectors to use for priv esc

### id
- provides a general overview of user's privilege level and group memberships.
- can also be used to obtain info about another user.e.g. **id bnb**

### /etc/passwd
- provides an easy way to discover users on the system

### history
- can gives us an idea about target system in some cases

### ifconfig
- target system may be pivoting to another network.
- ifconfig will give us info about the network interfaces of the system.

### netstat
- used with different options to gather info on existing connections
```
netstat -a			//shows all listening ports and established connections
netstat -at			//list all tcp connections
netstat -au			//list all udp connections
netstat -l			//list ports in listening mode
netstat -s			//list network usage statistics
netstat -p 			//list connections with their pid info
netstat -i			//shows interface statistics
netstat -ano		//n(don't resolve hostnames),a(display all sockets),o(display timers)
```

### find
- search target system for important info and potetial priviledge escalation vectors
- redirect erros to **/dev/null** to have a cleaner output.e.g.
```
find / -size +10G -type f 2>/dev/null
```
e.g. finding files with suid bit set:
```
find / -perm -u=s -type f 2>/dev/null
```
### Automated Enumeration
- several tools may be used for automated enumeration e.g.:
1. Linpeas
2. LinEnum
3. Linux Exploit Suggestor
4. Linux Smart Enumeration
5. Linux Priv Checker


## Priviledge Escalation Techniques
### 1. Kernel Exploits
- Kernel manages communication between components such as memory on system and apps.
- Thus, as its functions are critical, this requires the kernel to have specific privileges, thus a successful exploit will lead to root privileges.<br>
<ins>steps:<ins>
1. Identify kernel version/vulnerable kernel
2. Search for exploit code of kernel for the target system
3. Execute exploit on target system

### 2. Sudo

### 3. SUID(set user identification)
- Linux privilege controls rely on controlling the users and files interactions using permissions.
- Files can have rwx permissions.
- Files with suid bit set allow them to be executed with permission level of the owner of the files and have an "s" bit set showing their special permission level.
- Find files with suid and sgid bit set using
```
find / -type f -perm 04000 -ls 2>/dev/null
```
- Use gtfobins.com to check if binary can be exploited through suid bit.
- e.g. to escalate using python3 with suid bit set:
```
python3 -c 'import pty;pty.spawn("\bin\bash -p")';
```
-e.g. using bas64:
```
LFILE=file_to_read
./base64 "$LFILE" | base64 --decode
```
etc

### 4. Capabilities
- Capabilities help manage privileges at a granular level.
- We can check for tools with such enables capabilities using getcap e.g.:
```
getcap / -r 2>/deev/null
```
- From output, of the binaries, use either of them for privilege escalation or to read files. Use gtfobins for help where needed
- **nb** files here do not have the suid bit set

