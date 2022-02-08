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
