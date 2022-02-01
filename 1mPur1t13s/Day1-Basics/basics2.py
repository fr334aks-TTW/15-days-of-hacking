#Primitive data types in python
#1. Numbers
       # => Integers - whole numbers
        num1 = 100; print(num1)
      #  => Floats - numbers with decimal points
        num2 = 56.4; print(num2)

#2. Strings - sequence of chars
        greetings = "welcome to python 101"; print(greetings)

        #Changing Case
        #>> title() -  capitalizes first letter
                firstName = 'Lewinsky'
                print(firstname.title())

        #>> upper() and lower()
                firstName = 'peter'
                print(firstName.upper())
                secondName = 'Fiona'
                print(secondName.lower())

        #String concat
                firstName = 'sweet'
                lastName = 'impurities'
                fullname = firstName + ' ' + lastName
                message = fullName.title() + ' ' + "is the worlsd' best hacker"
                print(message)

        #Slicing - extracts a substring within the stated range
hack ="Haking is fun ansd so exciting"
print(hack[2:8]) #slices from position 2 to 8(excluded)

        #Splitting and Stripping
names =  " lewinsky, fiona, ken, john, chloe "
splits = name.split(','); print(splits)
strips = name.strip(); print(strips)

#Finding substrings
#find() - returns the index of the first character that matches your keyword
message = "There were many presentation at the conference but rEvil was more  intresting"
grep = "interesting"
match = message.find(grep)
print(match)

        #Escape characters
\', \", \n. \t, \b ...


#Boolean - returns True/False given a condition
a, b = 3, 4
print(a == b)   #---> returns false

#input( ) -->  captures data
        Username = input("Enter your username: ")
        Password = input("Enter your password: ")
        print("Credentials Verified. You're logged in!")
