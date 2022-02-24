![Gallery](https://user-images.githubusercontent.com/58165365/155577477-40448468-9d62-4ec6-8001-f936cac6d0ae.png)

# Windows Registry

The Windows Registry is a collection of databases that contains the system's configuration data. This configuration data can be about the hardware, the software, or the user's information. It also includes data about the recently used files, programs used, or devices connected to the system. This data is beneficial from a forensics standpoint.

The Windows registry consists of Keys and Values. When you open the regedit.exe utility to view the registry, the folders you see are `Registry Keys`. `Registry Values` are the data stored in these Registry Keys. A `Registry Hive` is a group of Keys, subkeys, and values stored in a single file on the disk.

# Structure of the Registry:

The registry on any Windows system contains the following five root keys:

- HKEY_CURRENT_USER
- HKEY_HKEY_USERS
- HKEY_LOCAL_MACHINE
- HKEY_CLASSES_ROOT
- HKEY_CURRENT_CONFIG

You can view these keys when you open the `regedit.exe` utility, a built-in Windows utility to view and edit the registry. To open the registry editor, press the Windows key and the R key simultaneously. It will open a run prompt that looks like this:

![image](https://user-images.githubusercontent.com/58165365/155318799-9d9f4bca-5de0-497c-bcf3-e57b7bcc8283.png)

In this prompt, type `regedit.exe`, and you will be greeted with the registry editor window. It will look something like this:

![image](https://user-images.githubusercontent.com/58165365/155319123-b6b06f11-d4e4-4e02-8b57-9d92c91d0a78.png)

Here you can see the root keys in the left pane in a tree view that shows the included registry keys, and the values in the selected key are shown in the right pane. You can right-click on the value shown in the right pane and select properties to view the properties of this value.

Here is how Microsoft defines each of these root keys. For more detail and information about the following Windows registry keys, please visit [Microsoft's documentation](https://docs.microsoft.com/en-US/troubleshoot/windows-server/performance/windows-registry-advanced-users).

| Folder/predefined key   | Description                                                                                                                                                                                                                                                                                                                                                                          |
| ----------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| **HKEY_CURRENT_USER**   | Contains the root of the configuration information for the user who is currently logged on. The user's folders, screen colors, and Control Panel settings are stored here. This information is associated with the user's profile. This key is sometimes abbreviated as HKCU.                                                                                                        |
| **HKEY_USERS**          | Contains all the actively loaded user profiles on the computer. HKEY_CURRENT_USER is a subkey of HKEY_USERS. HKEY_USERS is sometimes abbreviated as HKU.                                                                                                                                                                                                                             |
| **HKEY_LOCAL_MACHINE**  | Contains configuration information particular to the computer (for any user). This key is sometimes abbreviated as HKLM.                                                                                                                                                                                                                                                             |
| **HKEY_CLASSES_ROOT**   | Is a subkey of `HKEY_LOCAL_MACHINE\Software`. The information that is stored here makes sure that the correct program opens when you open a file by using Windows Explorer. This key is sometimes abbreviated as HKCR.                                                                                                                                                               |
|                         | Starting with Windows 2000, this information is stored under both the HKEY_LOCAL_MACHINE and HKEY_CURRENT_USER keys. The `HKEY_LOCAL_MACHINE\Software\Classes` key contains default settings that can apply to all users on the local computer. The `HKEY_CURRENT_USER\Software\Classes` key has settings that override the default settings and apply only to the interactive user. |
|                         | The HKEY_CLASSES_ROOT key provides a view of the registry that merges the information from these two sources. HKEY_CLASSES_ROOT also provides this merged view for programs that are designed for earlier versions of Windows. To change the settings for the interactive user, changes must be made under HKEY_CURRENT_USER\Software\Classes instead of under HKEY_CLASSES_ROOT.    |
|                         | To change the default settings, changes must be made under `HKEY_LOCAL_MACHINE\Software\Classes` .If you write keys to a key under HKEY_CLASSES_ROOT, the system stores the information under `HKEY_LOCAL_MACHINE\Software\Classes`.                                                                                                                                                 |
|                         | If you write values to a key under HKEY_CLASSES_ROOT, and the key already exists under `HKEY_CURRENT_USER\Software\Classes`, the system will store the information there instead of under `HKEY_LOCAL_MACHINE\Software\Classes`.                                                                                                                                                     |
| **HKEY_CURRENT_CONFIG** | Contains information about the hardware profile that is used by the local computer at system startup.                                                                                                                                                                                                                                                                                |

# Accessing registry hives offline

If you are accessing a live system, you will be able to access the registry using regedit.exe, and you will be greeted with all of the standard root keys we covered above . However, if you only have access to a disk image, you must know where the registry hives are located on the disk. The majority of these hives are located in the `C:\Windows\System32\Config` directory and are:

1. **DEFAULT** (mounted on `HKEY_USERS\DEFAULT`)
2. **SAM** (mounted on `HKEY_LOCAL_MACHINE\SAM`)
3. **SECURITY** (mounted on `HKEY_LOCAL_MACHINE\Security`)
4. **SOFTWARE** (mounted on `HKEY_LOCAL_MACHINE\Software`)
5. **SYSTEM** (mounted on `HKEY_LOCAL_MACHINE\System`)

![image](https://user-images.githubusercontent.com/58165365/155352337-93924923-faaa-4e94-95d8-7195d0d4510c.png)

Hives containing user information:

Apart from these hives, two other hives containing user information can be found in the User profile directory. For Windows 7 and above, a user’s profile directory is located in `C:\Users\<username>\` where the hives are:

1. **NTUSER.DAT** (mounted on HKEY_CURRENT_USER when a user logs in)
2. **USRCLASS.DAT** (mounted on HKEY_CURRENT_USER\Software\CLASSES)

Remember that `NTUSER.DAT` and `USRCLASS.DAT` are hidden files.

to be able to view hidden files:

![image](https://user-images.githubusercontent.com/58165365/155322157-95581597-d47d-414d-8ab0-918652228aa1.png)

The USRCLASS.DAT hive is located in the directory `C:\Users\<username>\AppData\Local\Microsoft\Windows`.

![image](https://user-images.githubusercontent.com/58165365/155321666-e6ab108f-b281-422e-b1c0-284aad0edf72.png)

The NTUSER.DAT hive is located in the directory C:\Users\<username>\.

![image](https://user-images.githubusercontent.com/58165365/155321946-634ec8b4-28d7-4abd-8f30-0abb09a78d53.png)

The Amcache Hive:

Apart from these files, there is another very important hive called the `AmCache hive`. This hive is located in `C:\Windows\AppCompat\Programs\Amcache.hve`. Windows creates this hive to save information on programs that were recently run on the system.

![image](https://user-images.githubusercontent.com/58165365/155349537-98ba6ee0-9f1f-48a3-9eec-41a9de032c1a.png)

## Transaction Logs and Backups:

Some other very vital sources of forensic data are the registry transaction logs and backups. The transaction logs can be considered as the journal of the changelog of the registry hive. Windows often uses transaction logs when writing data to registry hives. This means that the transaction logs can often have the latest changes in the registry that haven't made their way to the registry hives themselves. The transaction log for each hive is stored as a .LOG file in the same directory as the hive itself. It has the same name as the registry hive, but the extension is .LOG. For example, the transaction log for the SAM hive will be located in `C:\Windows\System32\Config` in the filename SAM.LOG. Sometimes there can be multiple transaction logs as well. In that case, they will have .LOG1, .LOG2 etc., as their extension. It is prudent to look at the transaction logs as well when performing registry forensics.

Registry backups are the opposite of Transaction logs. These are the backups of the registry hives located in the `C:\Windows\System32\Config directory. These hives are copied to the `C:\Windows\System32\Config\RegBack` directory every ten days. It might be an excellent place to look if you suspect that some registry keys might have been deleted/modified recently.

# Data Acquisition

When performing forensics, we will either encounter a live system or an image taken of the system. For the sake of accuracy, it is recommended practice to image the system or make a copy of the required data and perform forensics on it. This process is called data acquisition. Below we discuss different ways to acquire registry data from a live system or a disk image:

Though we can view the registry through the registry editor, the forensically correct method is to acquire a copy of this data and perform analysis on that. However, when we go to copy the registry hives from `%WINDIR%\System32\Config`, we cannot because it is a restricted file. So, what to do now?

For acquiring these files, we can use one of the following tools:

1. KAPE:
2. Autopsy
3. FTK Imager

## KAPE

[KAPE](https://www.kroll.com/en/insights/publications/cyber/kroll-artifact-parser-extractor-kape) (_Kroll Artifact Parser and Extractor_) is a live data acquisition and analysis tool which can be used to acquire registry data. It is primarily a command-line tool but also comes with a GUI. The below screenshot shows what the KAPE GUI looks like. I have already selected all the settings to extract the registry data using KAPE in this screenshot.

<!-- You can learn more about collecting forensic artifacts using KAPE in a dedicated KAPE room on [THM](). -->

![image](https://user-images.githubusercontent.com/58165365/155354515-0a79009d-bdbe-4afc-947d-7fc78de8c064.png)

## Autopsy:

[Autopsy](https://www.autopsy.com/) gives you the option to acquire data from both live systems or from a disk image. After adding your data source, navigate to the location of the files you want to extract, then right-click and select the Extract File(s) option. It will look similar to what you see in the screenshot below.

![image](https://user-images.githubusercontent.com/58165365/155355299-9298c27a-6d5a-42cd-ba34-b420264cbbed.png)

## FTK Imager:

[FTK Imager](https://www.exterro.com/ftk-imager) is similar to Autopsy and allows you to extract files from a disk image or a live system by mounting the said disk image or drive in FTK Imager. Below you can see the option to Export files as highlighted in the screenshot.

![image](https://user-images.githubusercontent.com/58165365/155355801-c9859ec7-0945-4c45-923b-68b79d0a5819.png)

Another way you can extract Registry files from FTK Imager is through the Obtain Protected Files option. This option is only available for live systems and is highlighted in the screenshot below. This option allows you to extract all the registry hives to a location of your choosing. However, it will not copy the `Amcache.hve` file, which is often necessary to investigate evidence of programs that were last executed.

![image](https://user-images.githubusercontent.com/58165365/155360295-5beb05b5-72c9-40ff-8831-31b4365b67ff.png)

# Exploring Windows Registry

Once we have extracted the registry hives, we need a tool to view these files as we would in the registry editor. Since the registry editor only works with live systems and can't load exported hives, we can use the following tools:

1. Registry Viewer
2. Zimmerman's Registry Explorer:

## Registry Viewer

As we can see in the screenshot below, AccessData's Registry Viewer has a similar user interface to the Windows Registry Editor. There are a couple of limitations, though. It only loads one hive at a time, and it can't take the transaction logs into account.

![image](https://user-images.githubusercontent.com/58165365/155366881-2be1ecf8-e80c-496c-a31b-1d230734d6b1.png)

## Zimmerman's Registry Explorer:

Eric Zimmerman has developed a handful of tools that are very useful for performing Digital Forensics and Incident Response. One of them is the Registry Explorer. It looks like the below screenshot. It can load multiple hives simultaneously and add data from transaction logs into the hive to make a more 'cleaner' hive with more up-to-date data. It also has a handy 'Bookmarks' option containing forensically important registry keys often sought by forensics investigators. Investigators can go straight to the interesting registry keys and values with the bookmarks menu item. I'll explore these in more detail later.

![image](https://user-images.githubusercontent.com/58165365/155367359-aadae7d7-872c-494a-b16d-1b6a9d21293c.png)

## RegRipper

RegRipper is a utility that takes a registry hive as input and outputs a report that extracts data from some of the forensically important keys and values in that hive. The output report is in a text file and shows all the results in sequential order.

RegRipper is available in both a CLI and GUI form which is shown in the screenshot below.

![image](https://user-images.githubusercontent.com/58165365/155368449-00bf0f78-b298-42a4-8e82-7ed013b05d58.png)

One shortcoming of RegRipper is that it does not take the transaction logs into account. We must use Registry Explorer to merge transaction logs with the respective registry hives before sending the output to RegRipper for a more accurate result.

# System Information and System Accounts

When we start performing forensic analysis, the first step is to find out about the system information.

## OS Version:

If we only have triage data to perform forensics, we can determine the OS version from which this data was pulled through the registry. To find the OS version, we can use the following registry key:

`SOFTWARE\Microsoft\Windows NT\CurrentVersion`

This is how Registry Explorer shows this registry key:

![image](https://user-images.githubusercontent.com/58165365/155579185-95f48ae1-ba3b-44fd-8bb7-6fba80e23461.png)

## Current control set:

The hives containing the machine’s configuration data used for controlling system startup are called **Control Sets**. Commonly, we will see two Control Sets, `ControlSet001` and `ControlSet002`, in the SYSTEM hive on a machine. In most cases, ControlSet001 will point to the Control Set that the machine booted with, and ControlSet002 will be the _last known good_ configuration. Their locations will be:

`SYSTEM\ControlSet001`

`SYSTEM\ControlSet002`

Windows creates a volatile Control Set when the machine is live, called the CurrentControlSet (`HKLM\SYSTEM\CurrentControlSet`). For getting the most accurate system information, this is the hive that we will refer to. We can find out which Control Set is being used as the CurrentControlSet by looking at the following registry value:

`SYSTEM\Select\Current`

Similarly, the _last known good_ configuration can be found using the following registry value:

`SYSTEM\Select\LastKnownGood`

This is how it looks like in Registry Explorer.

![image](https://user-images.githubusercontent.com/58165365/155579120-5bf6f5d4-5130-4234-8482-9b2f60921750.png)

It is vital to establish this information before moving forward with the analysis. Many forensic artifacts we collect will be collected from the Control Sets.

## Computer Name:

It is crucial to establish the Computer Name while performing forensic analysis to ensure that we are working on the machine we are supposed to work on. We can find the Computer Name from the following location:

`SYSTEM\CurrentControlSet\Control\ComputerName\ComputerName`

Registry Explorer shows it like this.

![image](https://user-images.githubusercontent.com/58165365/155579056-d93b07b8-3931-4e04-8da2-7f8038fcd78d.png)

## Time Zone Information:

For accuracy, it is important to establish what time zone the computer is located in. This will help us understand the chronology of the events as they happened. For finding the Time Zone Information, we can look at the following location:

`SYSTEM\CurrentControlSet\Control\TimeZoneInformation`

Here's how it looks in Registry Explorer.

![image](https://user-images.githubusercontent.com/58165365/155578981-c4b248f3-d4ce-4052-b139-562f5d96bb36.png)

Time Zone Information is important because some data in the computer will have their timestamps in UTC/GMT and others in the local time zone. Knowledge of the local time zone helps in establishing a timeline when merging data from all the sources.

## Network Interfaces and Past Networks:

The following registry key will give a list of network interfaces on the machine we are investigating:

`SYSTEM\CurrentControlSet\Services\Tcpip\Parameters\Interfaces`

Take a look at this registry key as shown in Registry Explorer

![image](https://user-images.githubusercontent.com/58165365/155578921-dd8c358f-43d1-43ba-8336-fa705a6a25b8.png)

Each Interface is represented with a unique identifier (GUID) subkey, which contains values relating to the interface’s TCP/IP configuration. This key will provide us with information like IP addresses, DHCP IP address and Subnet Mask, DNS Servers, and more. This information is significant because it helps you make sure that you are performing forensics on the machine that you are supposed to perform it on.

The past networks a given machine was connected to can be found in the following locations:

`SOFTWARE\Microsoft\Windows NT\CurrentVersion\NetworkList\Signatures\Unmanaged`

`SOFTWARE\Microsoft\Windows NT\CurrentVersion\NetworkList\Signatures\Managed`

![image](https://user-images.githubusercontent.com/58165365/155578882-a19d3c62-d3e6-432b-9e2f-b688f9bc86d6.png)

These registry keys contain past networks as well as the last time they were connected. The last write time of the registry key points to the last time these networks were connected.

## Autostart Programs (Autoruns):

The following registry keys include information about programs or commands that run when a user logs on.

`NTUSER.DAT\Software\Microsoft\Windows\CurrentVersion\Run`

`NTUSER.DAT\Software\Microsoft\Windows\CurrentVersion\RunOnce`

`SOFTWARE\Microsoft\Windows\CurrentVersion\RunOnce`

`SOFTWARE\Microsoft\Windows\CurrentVersion\policies\Explorer\Run`

`SOFTWARE\Microsoft\Windows\CurrentVersion\Run`

![image](https://user-images.githubusercontent.com/58165365/155578824-b7b0c385-b12d-4797-b210-ce70731b14db.png)

The following registry key contains information about services:

`SYSTEM\CurrentControlSet\Services`

Notice the Value of the Start key in the screenshot below.

![image](https://user-images.githubusercontent.com/58165365/155578779-c5901275-d070-4cb2-a8b2-fa78e53b4513.png)

In this registry key, if the start key is set to **0x02**, this means that this service will start at boot.

## SAM hive and user information:

The SAM hive contains user account information, login information, and group information. This information is mainly located in the following location:

`SAM\Domains\Account\Users`

Take a look at the below screenshot

![image](https://user-images.githubusercontent.com/58165365/155578704-b34c2dac-028c-4a66-8662-2fb4fa67a1fd.png)

The information contained here includes the relative identifier (RID) of the user, number of times the user logged in, last login time, last failed login, last password change, password expiry, password policy and password hint, and any groups that the user is a part of.

# Usage or knowledge of files/folders

## Recent Files:

Windows maintains a list of recently opened files for each user. As we might have seen when using Windows Explorer, it shows us a list of recently used files. This information is stored in the NTUSER hive and can be found on the following location:

`NTUSER.DAT\Software\Microsoft\Windows\CurrentVersion\Explorer\RecentDocs`

![image](https://user-images.githubusercontent.com/58165365/155578601-b64ebbfa-2e64-4046-bce2-a02854a1e43f.png)

Registry Explorer allows us to sort data contained in registry keys quickly. For example, the Recent documents tab arranges the Most Recently Used (MRU) file at the top of the list. Registry Explorer also arranges them so that the Most Recently Used (MRU) file is shown at the top of the list and the older ones later.

Another interesting piece of information in this registry key is that there are different keys with file extensions, such as `.pdf`, `.jpg`, `.docx` etc. These keys provide us with information about the last used files of a specific file extension. So if we are looking specifically for the last used PDF files, we can look at the following registry key:

`NTUSER.DAT\Software\Microsoft\Windows\CurrentVersion\Explorer\RecentDocs\.pdf`

Registry Explorer also lists the Last Opened time of the files.

## Office Recent Files

Similar to the Recent Docs maintained by Windows Explorer, Microsoft Office also maintains a list of recently opened documents. This list is also located in the NTUSER hive. It can be found in the following location:

`NTUSER.DAT\Software\Microsoft\Office\VERSION`

The version number for each Microsoft Office release is different. An example registry key will look like this:

`NTUSER.DAT\Software\Microsoft\Office\15.0\Word`

Here, the 15.0 refers to Office 2013. A list of different Office releases and their version numbers can be found on [this link](https://docs.microsoft.com/en-us/deployoffice/install-different-office-visio-and-project-versions-on-the-same-computer#office-releases-and-their-version-number).

Starting from Office 365, Microsoft now ties the location to the user's [live ID](https://www.microsoft.com/security/blog/2008/05/07/what-is-a-windows-live-id/). In such a scenario, the recent files can be found at the following location.

`NTUSER.DAT\Software\Microsoft\Office\VERSION\UserMRU\LiveID_####\FileMRU`

In such a scenario, the recent files can be found at the following location. This location also saves the complete path of the most recently used files.

# ShellBags:

When any user opens a folder, it opens in a specific layout. Users can change this layout according to their preferences. These layouts can be different for different folders. This information about the Windows 'shell' is stored and can identify the Most Recently Used files and folders. Since this setting is different for each user, it is located in the user hives. We can find this information on the following locations:

`USRCLASS.DAT\Local Settings\Software\Microsoft\Windows\Shell\Bags`

`USRCLASS.DAT\Local Settings\Software\Microsoft\Windows\Shell\BagMRU`

`NTUSER.DAT\Software\Microsoft\Windows\Shell\BagMRU`

`NTUSER.DAT\Software\Microsoft\Windows\Shell\Bags`

Registry Explorer doesn't give us much information about ShellBags. However, another tool from Eric Zimmerman's tools called the `ShellBag Explorer` shows us the information in an easy-to-use format. We just have to point to the hive file we have extracted, and it parses the data and shows us the results. An example is shown below.

![image](https://user-images.githubusercontent.com/58165365/155578517-7025b03c-e273-4d96-9bc2-64583e96d6f5.png)

# Open/Save and LastVisited Dialog MRUs:

When we open or save a file, a dialog box appears asking us where to save or open that file from. It might be noticed that once we open/save a file at a specific location, Windows remembers that location. This implies that we can find out recently used files if we get our hands on this information. We can do so by examining the following registry keys

`NTUSER.DAT\Software\Microsoft\Windows\CurrentVersion\Explorer\ComDlg32\OpenSavePIDlMRU`

`NTUSER.DAT\Software\Microsoft\Windows\CurrentVersion\Explorer\ComDlg32\LastVisitedPidlMRU`

This is how Registry Explorer shows this registry key.

![image](https://user-images.githubusercontent.com/58165365/155578466-be14b4a5-207e-44f3-a6a0-dd4bcb8cd4ee.png)

## Windows Explorer Address/Search Bars:

Another way to identify a user's recent activity is by looking at the paths typed in the Windows Explorer address bar or searches performed using the following registry keys, respectively.

`NTUSER.DAT\Software\Microsoft\Windows\CurrentVersion\Explorer\TypedPaths`

`NTUSER.DAT\Software\Microsoft\Windows\CurrentVersion\Explorer\WordWheelQuery`

Here is how the TypedPaths key looks like in Registry Explorer:

![image](https://user-images.githubusercontent.com/58165365/155578398-9daba32d-1bb2-4267-a680-004c86b04494.png)

# Evidence of Execution

## UserAssist:

Windows keeps track of applications launched by the user using Windows Explorer for statistical purposes in the User Assist registry keys. These keys contain information about the programs launched, the time of their launch, and the number of times they were executed. However, programs that were run using the command line can't be found in the User Assist keys. The User Assist key is present in the NTUSER hive, mapped to each user's GUID. We can find it at the following location:

`NTUSER.DAT\Software\Microsoft\Windows\Currentversion\Explorer\UserAssist\{GUID}\Count`

Take a look at the below screenshot from Registry Explorer

![image](https://user-images.githubusercontent.com/58165365/155578307-949987fb-a6bc-4250-b1a7-c5e44a0c8d96.png)

## ShimCache:

ShimCache is a mechanism used to keep track of application compatibility with the OS and tracks all applications launched on the machine. Its main purpose in Windows is to ensure backward compatibility of applications. It is also called Application Compatibility Cache (AppCompatCache). It is located in the following location in the SYSTEM hive:

`SYSTEM\CurrentControlSet\Control\Session Manager\AppCompatCache`

ShimCache stores file name, file size, and last modified time of the executables.

Our goto tool, the Registry Explorer, doesn't parse ShimCache data in a human-readable format, so we go to another tool called `AppCompatCache Parser`, also a part of Eric Zimmerman's tools. It takes the SYSTEM hive as input, parses the data, and outputs a CSV file that looks like this:

![image](https://user-images.githubusercontent.com/58165365/155578110-85d4d853-faff-4f52-8fa3-eb0b31693ba7.png)

We can use the following command to run the AppCompatCache Parser Utility:

```powershell
AppCompatCacheParser.exe --csv <path to save output> -f <path to SYSTEM hive for data parsing> -c <control set to parse>
```

The output can be viewed using EZviewer, another one of Eric Zimmerman's tools.

## AmCache:

The AmCache hive is an artifact related to ShimCache. This performs a similar function to ShimCache, and stores additional data related to program executions. This data includes execution path, installation, execution and deletion times, and SHA1 hashes of the executed programs. This hive is located in the file system at:

`C:\Windows\appcompat\Programs\Amcache.hve`

Information about the last executed programs can be found at the following location in the hive:

`Amcache.hve\Root\File\{Volume GUID}\`

This is how Registry Explorer parses the AmCache hive:

![image](https://user-images.githubusercontent.com/58165365/155565075-bdce6e60-cee9-4f78-b9fa-6c5d73fabb46.png)

## BAM/DAM:

**Background Activity Monitor** or BAM keeps a tab on the activity of background applications. Similar **Desktop Activity Moderator** or DAM is a part of Microsoft Windows that optimizes the power consumption of the device. Both of these are a part of the Modern Standby system in Microsoft Windows.

In the Windows registry, the following locations contain information related to BAM and DAM. This location contains information about last run programs, their full paths, and last execution time.

`SYSTEM\CurrentControlSet\Services\bam\UserSettings\{SID}`

`SYSTEM\CurrentControlSet\Services\dam\UserSettings\{SID}`

Below you can see how Registry Explorer parses data from BAM:

![image](https://user-images.githubusercontent.com/58165365/155567555-59ff8e58-d326-44db-905c-a15e628b1d0d.png)

# External Devices/USB device forensics

When performing forensics on a machine, often the need arises to identify if any USB or removable drives were attached to the machine. If so, any information related to those devices is important for a forensic investigator. In this task, we will go through the different ways to find information on connected devices and the drives on a system using the registry.

## Device identification:

The following locations keep track of USB keys plugged into a system. These locations store the vendor id, product id, and version of the USB device plugged in and can be used to identify unique devices. These locations also store the time the devices were plugged into the system.

`SYSTEM\CurrentControlSet\Enum\USBSTOR`

`SYSTEM\CurrentControlSet\Enum\USB`

Registry Explorer shows this information in a nice and easy-to-understand way.

![image](https://user-images.githubusercontent.com/58165365/155568712-21f6d145-a646-455b-9e94-f3c93819a5c0.png)

## First/Last Times:

Similarly, the following registry key tracks the first time the device was connected, the last time it was connected and the last time the device was removed from the system.

`SYSTEM\CurrentControlSet\Enum\USBSTOR\Ven_Prod_Version\USBSerial#\Properties\{83da6326-97a6-4088-9453-a19231573b29}\####`

In this key, the #### sign can be replaced by the following digits to get the required information:

| Value | Information           |
| ----- | --------------------- |
| 0064  | First Connection time |
| 0066  | Last Connection time  |
| 0067  | Last removal time     |

Although we can check this value manually, as we have seen above, Registry Explorer already parses this data and shows us if we select the USBSTOR key.

## USB device Volume Name:

The device name of the connected drive can be found at the following location:

`SOFTWARE\Microsoft\Windows Portable Devices\Devices`

![image](https://user-images.githubusercontent.com/58165365/155570879-368c3e30-e8a1-4811-a047-a518d1168b82.png)

We can compare the GUID we see here in this registry key and compare it with the Disk ID we see on keys mentioned in device identification to correlate the names with unique devices.

Combining all of this information, we can create a fair picture of any USB devices that were connected to the machine we're investigating.
