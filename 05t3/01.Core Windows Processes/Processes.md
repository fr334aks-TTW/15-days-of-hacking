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

# TO BE CONTINUED

# Summary

| System | Image Path          | C:\Windows\system32\ntoskrnl.exe (NT OS Kernel) |
| ------ | ------------------- | ----------------------------------------------- |
|        | Parent Process      | System Idle Process (0)                         |
|        | User Account        | Local System                                    |
|        | Start Time          | At boot time                                    |
|        | Number of Instances | One                                             |

# Resources

- [Microsoft - Processes and Threads](https://docs.microsoft.com/en-us/windows/win32/procthread/processes-and-threads)
- [TryHackMe - Core Windows Processes](https://tryhackme.com/room/btwindowsinternals)
- [Microsoft - Finding the process ID](https://docs.microsoft.com/en-us/windows-hardware/drivers/debugger/finding-the-process-id)
- [Wikipedia - Session Manager Subsystem](https://en.wikipedia.org/wiki/Session_Manager_Subsystem)
