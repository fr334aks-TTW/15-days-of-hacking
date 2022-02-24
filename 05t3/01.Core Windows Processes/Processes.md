![image](https://user-images.githubusercontent.com/58165365/155579746-c2bd89a9-70f9-4b1d-b961-f8917137b69d.png)

It is vital to understand how the Windows operating system functions as a defender. Today i will be going through core processes as understanding how they operate normally can aid a defender to identify unusual activity on the endpoint.

# Core Windows Processes

## Task Manager

Task Manager is a built-in GUI-based Windows utility that allows users to see what is running on the Windows system. It also provides information on resource usage, such as how much CPU and memory are utilized by each process. When a program is not responding, Task Manager is used to end (kill) the process.

To open Task Manager, right-click the Taskbar. When the new window appears, select Task Manager (as shown below).

![image](https://user-images.githubusercontent.com/58165365/151594929-6a30b8a2-c7bb-4937-892e-37cb05035236.png)

You can also hold `Ctrl+Shift+Esc` to launch it.

There are 5 tabs within Task Manager. By default, the current tab is `Processes`. Notice that the processes are categorized: Apps, Background processes and Windows processes

![image](https://user-images.githubusercontent.com/58165365/151596701-9262017a-2ea8-473a-bf2b-7400db14324f.png)

The columns are very minimal. The columns `Name`, `Status`, `CPU`, and `Memory`, are the only ones visible. To view more columns, right-click on any of the column headers to open more options.

![image](https://user-images.githubusercontent.com/58165365/151597122-d244770e-e4d0-4425-a4bc-3d7c109b57ae.png)

![image](https://user-images.githubusercontent.com/58165365/151597997-b9ae56c7-9d7c-4eea-8316-41cb5cdd044f.png)

This looks a little better. Let's briefly go over each column (excluding Name, of course):

- `Type` - Each process falls into 1 of 3 categories (Apps, Background process, or Windows process).
- `Publisher` - Think of this column as the name of the author of the program/file.
- `PID` - This is known as the **process identifier number.** Windows assigns a unique process identifier each time a program starts. If the same program has multiple processes running, each will have its own unique process identifier (PID).
- `Process name` - This is the file name of the process. In the above image, the file name for Task Manager is **Taskmrg.exe**.
- `Command line` - The full command used to launch the process.
- `CPU` - The amount of CPU (processing power) used by the process.
- `Memory` - The amount of physical working memory utilized by the process.

In this walkthrough, i will be focussing on the `Details` tab which contains some of the core processes.

![image](https://user-images.githubusercontent.com/58165365/151605335-d5dffa5c-3835-4595-a2a6-a729bb9e5590.png)

I'm gonna add two columns `Image path name` and `Command line`.

![image](https://user-images.githubusercontent.com/58165365/151605869-c98e3cfa-4d2b-47a4-8d1d-22b3a19df4e5.png)

These 2 columns can quickly alert an analyst on any outliers with a given process. For example, in the below image, `PID 740` is paired with a process named `svchost.exe`, a Windows process, but if the Image path name or Command line is not what it's expected to be, then we can perform a deeper analysis on this process.

Task Manager is a powerful built-in Windows utility but lacks certain important information when analyzing processes, such as parent process information. This is another key column when identifying outliers. Back to svchost.exe, if the parent process for `PID 740` is not `services.exe`, then this will warrant further analysis.

![image](https://user-images.githubusercontent.com/58165365/151608222-01a4717a-5cde-4041-95a4-b41dee8b3b91.png)

Based on the above image, the PID for services.exe is 748. But wait, one of the svchost.exe processes has a PID of 740 and 624. How did svchost.exe start before services.exe? Well, it didn't. Task Manager doesn't show a Parent-Child process view. That is where other utilities, such as [Process Hacker](https://processhacker.sourceforge.io/) and [Process Explorer](https://docs.microsoft.com/en-us/sysinternals/downloads/process-explorer), come to the rescue.

Moving forward, I'll use both Process Hacker and Process Explorer instead of Task Manager to obtain information about each of the Windows processes.

## System

The first Windows process on the list is System. PID for any given process is assigned at random, but that is not the case for the System process. The PID for System is always `4` , otherwise it is malware. What does this process do exactly?

The official definition from Windows Internals 6th Edition:

> _"The System process (process ID 4) is the home for a special kind of thread that runs only in kernel mode a kernel-mode system thread. System threads have all the attributes and contexts of regular user-mode threads (such as a hardware context, priority, and so on) but are different in that they run only in kernel-mode executing code loaded in system space, whether that is in Ntoskrnl.exe or in any other loaded device driver. In addition, system threads don't have a user process address space and hence must allocate any dynamic storage from operating system memory heaps, such as a paged or nonpaged pool."_

Simply put:

> The system process is responsible for the system memory and compressed memory in the NT kernel. This system process is a single thread running on each processor. It is the host of all kind of drivers (network, disk, USB). The related file name is C:\Windows\System32\ntoskrnl.exe. The system process in Windows 10 has a additional task, it is compressing old pages of memory so that you have more free memory to use. That's why this process may use a lot of memory.

Normal behaviour for this process would look something like this.

![image](https://user-images.githubusercontent.com/58165365/151611346-0bd47932-d4d2-47eb-b070-44e2e771e313.png)

![image](https://user-images.githubusercontent.com/58165365/151611750-8e301d81-d610-4c59-bac0-928fe5dd64ac.png)

Ways to identify unusual behavior for this process?

- A parent process (aside from **System Idle Process (0))**
- Multiple instances of System. (Should only be 1 instance)
- A different PID. (Remember that the PID will always be **PID 4**)
- Not running in Session 0

### smss.exe

The next process is `smss.exe` (**Session Manager Subsystem**). This process, also known as the Windows Session Manager, is responsible for creating new sessions. This is the first user-mode process started by the kernel.

This process starts the kernel mode and user mode of the Windows subsystem (you can read more about the NT Architecture [here](https://en.wikipedia.org/wiki/Architecture_of_Windows_NT)). This subsystem includes:

- win32k.sys (kernel mode)
- winsrv.dll (user mode)
- csrss.exe (user mode)

Smss.exe starts csrss.exe (Windows subsystem) and wininit.exe in Session 0, an isolated Windows session for the operating system, and csrss.exe and winlogon.exe for Session 1, which is the user session. The first child instance creates child instances in new sessions. This is done by smss.exe copying itself into the new session and self-terminating. You can read more about this process [here](https://en.wikipedia.org/wiki/Session_Manager_Subsystem).

What is normal?

- Image Path: %SystemRoot%\System32\smss.exe
- Parent Process: System
- Number of Instances: One master instance and child instance per session. The child instance exits after creating the session.
- User Account: Local System
- Start Time: Within seconds of boot time for the master instance

What is unusual?

- A different parent process other than System(4)
- Image path is different from C:\Windows\System32
- More than 1 running process. (children self-terminate and exit after each new session)
- User is not SYSTEM
- Unexpected registry entries for Subsystem

#### csrss.exe

csrss.exe (Client Server Runtime Process) is the user-mode side of the Windows subsystem. This process is always running and is critical to system operation. If by chance this process is terminated it will result in system failure. This process is responsible for: the Win32 console window and process thread creation and deletion. For each instance csrsrv.dll, basesrv.dll, and winsrv.dll are loaded (along with others).

This process is also responsible for:

- Making the Windows API available to other processes
- Mapping drive letters
- Handling the Windows shutdown process.

You can read more about this process [here](https://en.wikipedia.org/wiki/Client/Server_Runtime_Subsystem).

What is normal?

- Image Path: %SystemRoot%\System32\csrss.exe
- Parent Process: Created by an instance of smss.exe
- Number of Instances: Two or more
- User Account: Local System
- Start Time: Within seconds of boot time for the first 2 instances (for Session 0 and 1). Start times for additional instances occur as new sessions are created, although often only Sessions 0 and 1 are created.

What is unusual?

- An actual parent process. (smss.exe calls this process and self-terminates)
- Image file path other than C:\Windows\System32
- Subtle misspellings to hide rogue process masquerading as csrss.exe in plain sight
- User is not SYSTEM

### wininit.exe

_TO ADD_

### lsass.exe

Per Wikipedia, "Local Security Authority Subsystem Service (LSASS) is a process in Microsoft Windows operating systems that is responsible for enforcing the security policy on the system. It verifies users logging on to a Windows computer or server, handles password changes, and creates access tokens. It also writes to the Windows Security Log.

It creates security tokens for SAM (Security Account Manager), AD (Active Directory), and NETLOGON. It uses authentication packages specified in `HKLM\System\CurrentControlSet\Control\Lsa`.

![image](https://user-images.githubusercontent.com/58165365/152241249-15b3f7ea-3ad0-4f83-a6d3-86b4c1acc0c5.png)

This is another process adversaries target. Common tools such as mimikatz is used to dump credentials or they mimic this process to hide in plain sight. Again, they do this by either naming their malware by this process name or simply misspelling the malware slightly.

**Extra reading:** How LSASS is maliciously used and additional features that Microsoft has put into place to prevent these attacks. [(here)](https://yungchou.wordpress.com/2016/03/14/an-introduction-of-windows-10-credential-guard/)

What is normal?

![image](https://user-images.githubusercontent.com/58165365/152242677-cda60709-ef09-4543-b037-aff94f34b3d4.png)

- Image Path: %SystemRoot%\System32\lsass.exe
- Parent Process: wininit.exe
- Number of Instances: One
- User Account: Local System
- Start Time: Within seconds of boot time

What is unusual?

- A parent process other than wininit.exe
- Image file path other than C:\Windows\System32
- Subtle misspellings to hide rogue process in plain sight
- Multiple running instances
- Not running as SYSTEM

#### winlogon.exe

The Windows Logon, winlogon.exe, is responsible for handling the Secure Attention Sequence (SAS). This is the `ALT+CTRL+DELETE` key combination users press to enter their username & password.

This process is also responsible for loading the user profile. This is done by loading the user's `NTUSER.DAT` into `HKCU` and via userinit.exe loads the user's shell.

![image](https://user-images.githubusercontent.com/58165365/152232160-9f6803a9-a4c6-4686-bbda-d1a6336da386.png)

It is also responsible for locking the screen and running the user's screensaver, among other functions. More deets can be found [here](https://en.wikipedia.org/wiki/Winlogon)

smss.exe launches this process along with a copy of csrss.exe within Session 1.

![image](https://user-images.githubusercontent.com/58165365/152234356-eabdb586-016a-4328-a26a-c889c3039e14.png)

What is normal?

![image](https://user-images.githubusercontent.com/58165365/152234235-e9f7c5f1-f460-48fb-b5f7-e38021e9d6c2.png)

![image](https://user-images.githubusercontent.com/58165365/152234019-699b79b9-327b-4859-8c9d-b07db99f0d28.png)

- Image Path: %SystemRoot%\System32\winlogon.exe
- Parent Process: Created by an instance of smss.exe that exits, so analysis tools usually do not provide the parent process name.
- Number of Instances: One or more
- User Account: Local System
- Start Time: Within seconds of boot time for the first instance (for Session 1). Additional instances occur as new sessions are created, typically through Remote Desktop or Fast User Switching logons.

What is unusual?

- An actual parent process. (smss.exe calls this process and self-terminates)
- Image file path other than C:\Windows\System32
- Subtle misspellings to hide rogue process in plain sight
- Not running as SYSTEM
- Shell value in the registry other than explorer.exe

## explorer.exe

Windows Explorer, explorer.exe. This is the process that gives the user access to their folders and files. It also provides functionality to other features such as the Start Menu, Taskbar, etc.

Winlogon process runs userinit.exe, which launches the value in `HKLM\Software\Microsoft\Windows NT\CurrentVersion\Winlogon\Shell`. Userinit.exe exits after spawning explorer.exe. Because of this, the parent process is non-existent.

![image](https://user-images.githubusercontent.com/58165365/152226033-20996d76-8490-4e45-961d-6148c42ca462.png)

What is normal?

![image](https://user-images.githubusercontent.com/58165365/152225622-08867f38-d9ff-492d-b5f1-53200464e9a3.png)

- Image Path: %SystemRoot%\explorer.exe
- Parent Process: Created by userinit.exe and exits
- Number of Instances: One or more per interactively logged-in user
- User Account: Logged-in user(s)
- Start Time: First instance when the first interactive user logon session begins

What is unusual?

- An actual parent process. (userinit.exe calls this process and exits)
- Image file path other than C:\Windows
- Running as an unknown user
- Subtle misspellings to hide rogue process in plain sight
- Outbound TCP/IP connections

![image](https://user-images.githubusercontent.com/58165365/152224907-b930eac3-faa4-4037-a422-a71d44f9c6e4.png)

Note: The above image is a screenshot for the explorer.exe properties view from Process Explorer.

# Summary

![image](https://user-images.githubusercontent.com/58165365/152251857-ff5aa13d-2b94-4412-a746-8c8142b1850b.png)

|              |              |              |     | Image Path                                      | Parent Process                                                                                                   | User Account                                                                                                                                       | Start Time                                                                                                                                                                                             | Number of Instances                                                                                      |
| ------------ | ------------ | ------------ | --- | ----------------------------------------------- | ---------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | -------------------------------------------------------------------------------------------------------- |
| System       |              |              |     | C:\Windows\system32\ntoskrnl.exe (NT OS Kernel) | System Idle Process (0)                                                                                          | Local System                                                                                                                                       | At boot time                                                                                                                                                                                           | One                                                                                                      |
|              | smss.exe     |              |     | %SystemRoot%\System32\smss.exe                  | System(4)                                                                                                        | Local System                                                                                                                                       | Within seconds of boot time for the master instance                                                                                                                                                    | One master instance and child instance per session. The child instance exits after creating the session. |
|              |              | csrss.exe    |     | %SystemRoot%\System32\csrss.exe                 | Created by an instance of smss.exe                                                                               | Local System                                                                                                                                       | Within seconds of boot time for the first 2 instances (for Session 0 and 1). Start times for additional instances occur as new sessions are created, although often only Sessions 0 and 1 are created. | Two or more                                                                                              |
|              |              | winlogon.exe |     | %SystemRoot%\System32\winlogon.exe              | Created by an instance of smss.exe that exits, so analysis tools usually do not provide the parent process name. | Local System                                                                                                                                       | Within seconds of boot time for the first instance (for Session 1). Additional instances occur as new sessions are created, typically through Remote Desktop or Fast User Switching logons.            | One or more                                                                                              |
| wininit.exe  |              |              |     | %SystemRoot%\System32\wininit.exe               | Created by an instance of smss.exe                                                                               | Local System                                                                                                                                       | Within seconds of boot time                                                                                                                                                                            | One                                                                                                      |
|              | services.exe |              |     | %SystemRoot%\System32\services.exe              | wininit.exe                                                                                                      | Local System                                                                                                                                       | Within seconds of boot time                                                                                                                                                                            | One                                                                                                      |
|              |              | svchost.exe  |     | %SystemRoot%\System32\svchost.exe               | services.exe                                                                                                     | Varies (SYSTEM, Network Service, Local Service) depending on the svchost.exe instance. In Windows 10 some instances can run as the logged-in user. | Typically within seconds of boot time. Other instances can be started after boot                                                                                                                       | Many                                                                                                     |
|              | lsass.exe    |              |     | %SystemRoot%\System32\lsass.exe                 | wininit.exe                                                                                                      | Local System                                                                                                                                       | Within seconds of boot time                                                                                                                                                                            | One                                                                                                      |
| explorer.exe |              |              |     | %SystemRoot%\explorer.exe                       | Created by userinit.exe and exits                                                                                | Logged-in user(s)                                                                                                                                  | First instance when the first interactive user logon session begins                                                                                                                                    | One or more per interactively logged-in user                                                             |

I have also attached a poster/cheatsheet for your perusal and indepth illustrations and explanations. [See](https://github.com/fr334aks-TTW/15-days-of-hacking/blob/7e8b18feb1c2cdabc6e4bd930f547e4170a18249/05t3/01.Core%20Windows%20Processes/HuntEvil.pdf)

# Resources

- [Microsoft - Processes and Threads](https://docs.microsoft.com/en-us/windows/win32/procthread/processes-and-threads)
- [Microsoft - Windows Internals Book](https://docs.microsoft.com/en-us/sysinternals/resources/windows-internals)
- [TryHackMe - Core Windows Processes](https://tryhackme.com/room/btwindowsinternals)
- [Microsoft - Finding the process ID](https://docs.microsoft.com/en-us/windows-hardware/drivers/debugger/finding-the-process-id)
- [Wikipedia - Session Manager Subsystem](https://en.wikipedia.org/wiki/Session_Manager_Subsystem)
- [SANS - Hunt Evil Poster](https://www.sans.org/posters/hunt-evil/)
