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
