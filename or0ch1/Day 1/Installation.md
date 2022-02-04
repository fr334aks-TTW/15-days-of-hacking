# The Beginning

- As with any journey there is always the first step that you have to take. In my case it was intsalling **nim** :laughing:.

- The installation process is pretty straight forward and you can choose between these two methods:

   #### 1. Official Installation

- This is whereby you use the official binaries provided by nim.

- There are two types:
    1. Pre-built Binary
    2. Source Distribution

- For the pre-built binary you just need to download, extract it into the directory of choice and add the bin directory to path.

- However if you choose the source Distribution there are some few extra steps you need to take in order to install. After extracting cd into the extracted directory and execute:

```
sh build.sh
bin/nim c koch
./koch boot -d:release
./koch tools
```
- Then add the **bin** and **~/.nimble/bin** directories to path and you are done.


   #### 2. Choosenim

- This is an installer for nim which allows one to easily switch between nim versions whether it is a stable release or latest development version.

- I personally went for this method :laughing: :skull:.

- I just downloaded the installer, ran it and followed the onscreen instructions.
```
curl https://nim-lang.org/choosenim/init.sh -sSf | sh
```

- The binray can be downloaded from [Nim Download](https://nim-lang.org/install.html).


Now that thats out of the way, i started exploring basic concepts of the language.


   ### Syntax
   - Nim syntax is python inspired so for people who have done python it will be really easy to pick up.
   - Lets Dive in:

      1. File naming and Compilation
      - Nim files are saved with  **.nim** extension and have to be compiled in order to get an exxecutable.

      - To compile and run the program in one action we use the following command:

      ```
      nim c -r {filename}.nim
      ```
      - The **c** flag compiles while the **-r** runs it.

      - you also have the option of compiling nd running separately, just ommit the **-r** flag from the command and then run the executable generated, on windows it will be a .exe file.

      2. Comments
      - Really simple and denoted by a **#** symbol before the comment to be made.

      - multiline comments are denoted by **#[ ]#**
      ```
      #This is a comment
      #[ This is a multiline comment
      It terminates when the square brackets are closed.
      ]#
      ```
      3. Output
      - Anything to be outputted to screen is done by using **echo**

      ```
      echo "hello world"
      ``` 
      4. Variables 
      - Nim supports 2 types of variables:
        - Mutable variables
          - Variables whose values can be changed.

          - declared using the **var** keyword
          ```
          var <name>: <type>
          or
          var <name>: <type> = <value>
          ```
          
          - Nim has type inference capability hence on can leave out type assignment and just assign value.

          - If you feeling lazy you can pass the variables as a block if you are assigning multiple

          ```
          var a:int    #type specified
          var a = 10   #type not specified
          var          #block assignments
            c = 10
            b = 20
            d = "hello"
          ```
          - Unlike other languages Nim is both case and underscore-insensitive meaning that helloWorld and hello_World are the same. However The first letter is case sensitive.
          - 
        - Immutable variables
          - Variables whose value cannot be changed once set.
          - Can be declared using **const** and **let** keywords.
          - The difference between the to is that when using **const** value must be known at compile time while when using **let** that isn't a must.
          ```
          const g = 30
          let k = 40 
          
          g = 25  #results in error
          k = 2   #results in error
          ```