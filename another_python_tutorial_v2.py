
#######################################
#          Browse to Python
#######################################
'''
Location of Python:
--------------------
C:\Program Files\Python27\python.exe

Location of 3.2:
---------------- 
~\AppData\Local\Programs\Pythin\Pythin38-32\python.exe

How to Run Python in Terminal:
-------------------------------- 
& c:/Users/sabdulg1/AppData/Local/Programs/Python/Python38-32/python.exe "y:/My Projects/Programming/python practice/MyPlayGround.py"


'''

############################################
'''
 https://www.techbeamers.com/python-module/

'''
############################################

#==========================================================


$ python MyFirstPythonScript.py


#==========================================================
'''
Find all Modules in PC
'''

$ python
>>> help('modules')


#==========================================================

        # SLICING  

#==========================================================

numbers = (4,5,6)
print(numbers[:-1])

# OUTPUT  (4,5)

colors=['red','blue','green']

print(colors[-1:])
['green']

print(colors[-2:])
['blue', 'green']


#==========================================================

        # Set   vs  Lists  vs Typles

#==========================================================
"""

Sets: {}
--------
- Cannot have multiple occurrences of the same element (unique) 
- Store unordered values ( when print() )
- Immutable 
- Set is faster than a list using find()
- used to test membership, remove duplicates from a sequence, and compute mathematical operations such as intersection, union, difference, and symmetric difference. Similar to <sets> in <Math>



Lists: []
---------
- Lists is like an Array in other progamming languages
- List is quite faster than a set when **iterating** (for-loop) over the values



Tuples: ()
---------
- tuples are ordered, unique (no multiple occurences), immutable ( the programmer and the interpreter a hint that the data should not be changed)(you can slice, re-assign/delete as whole only. not few elements)
- Tuples are commonly used as the equivalent of a dictionary without keys to store data. ...
- Reading data is simpler when tuples are stored inside a list.

Comparison:
1- Lists has variable length, tuple has fixed length.
2- List has mutable nature, tuple has immutable nature (give the programmer and the interpreter a hint that the data should not be changed.)
3- List has more functionality than the tuple.


"""
#==========================================================

            # When to Use Which

#==========================================================
'''
Use <tuple> when you want to store a person’s credentials for your website.
'''
person=('ABC','admin','12345')

'''
# And use <List> if you want an array.
'''
groceries=['bread','butter','cheese']


################################################
'''
- One:
-------
# You can’t use a list as a key for a dictionary. This is because only immutable values can be hashed. 
# Hence, we can only set immutable values like tuples as keys. 
# But if you still want to use a list as a key, you must turn it into a tuple first.

# In Other words:
# Tuples are commonly used as the equivalent of a dictionary without keys to store data. 

For Example,
[('Swordfish', 'Dominic Sena', 2001), ('Snowden', ' Oliver Stone', 2016), ('Taxi Driver', 'Martin Scorsese', 1976)]
Above example contains tuples inside list which has a list of movies.

# In Other Words:
Tuple can also be used as key in dictionary due to their hashable and immutable nature whereas Lists are not used as key in a dictionary because list can’t handle __hash__() and have mutable nature.

    key_val= {('alpha','bravo'):123} #Valid
    key_val = {['alpha','bravo']:123} #Invalid


- Two:
------
Easier to read:
--------------
[(2,4), (5,7), (3,8), (5,9)]
is easier to read than
[[2,4], [5,7], [3,8], [5,9]]

'''
################################################

"""
tuples are extremely useful data structures

1- Using a tuple instead of a list can give the programmer and the interpreter a hint that the data should not be changed.

2- Reading data is simpler when tuples are stored inside a list. For example,

"""
################################################

#==========================================================

            # LIST

#==========================================================

# First prepare a list of strings

subjects = [1, 'C', "Tips"]

for i, subject in enumerate(subjects):
    print(i, subject)

Output:
0 Python
1 Coding
2 Tips

#==============#
# Nested Lists #
#==============#

myotherlist=[[1,2],[3,[4,5]]]

#To access the element with the value 5, we write the following code.

myotherlist[1][1][1]

#==========================================================

            # SET

#==========================================================

# *** Create a set with strings and perform search in set

objects = {"python", "coding", "tips", "for", "beginners"}

# Print set.
print(objects)
print(len(objects))

# Use of "in" keyword.
if "tips" in objects:
    print("These are the best Python coding tips.")

# Use of "not in" keyword.
if "Java tips" not in objects:
    print("These are the best Python coding tips not Java tips.")

#################### 
# *** Lets initialize an empty set
items = set()

# Add three strings.
items.add("Python")
items.add("coding")
items.add("tips")

print(items)


#==========================================================

            # Tuples

#==========================================================

#######################
# Lists inside tuples #
#######################

mytuple=([1,2],[3,4],[5,6])

#################
# Nested tuples #
#################

mytuple=((1,2),(3,(4,5),(6,(7,(8,9)))))

# To access value 8 :

print(mytuple[1][2][1][1][0])

#==========================================================

                # Dynamic Typing.

#==========================================================

"""
In Java, C++, and other statically typed languages, you have to specify the data type of the function return value as well as the kind of each function argument. On the other hand, Python is a dynamically typed language.

In Python, you don’t explicitly provide the data types. Based on the value you’ve assigned, Python keeps track of the datatype internally. Another good definition of dynamic typing is as follows:
“Names are bound to objects at run-time with the help of assignment statements. And it is possible to attach a name to the objects of different types during the execution of the program.”

"""

# Test for dynamic typing:
# The following example demonstrates how a function can examine its arguments
# And do different things depending on their types.

from types import *

def CheckIt (x):
    if type(x) == IntType:
        print("You have entered an integer")
    else:
        print("Unable to recognize the input data type")

# Perform dynamic typing test
CheckIt(999)
    # Output:
    # You have entered an integer.

CheckIt("999")
    # Output:
    # Unable to recognize the input data type.
 
#==========================================================

#                  Return Function

#==========================================================

def ad(x,y):
    return x + y

#==========================================================

#                      PRINT

#==========================================================

def PrintSuhaib(x,y):

    print("{} and {}".format(x, 1)) # NEWER METHOD
    print('{}{}'.format(y, 2)) 

    print("number: %d" % (x)) # OLD METHOD

#==========================================================

#                    something

#==========================================================

x = 7
y= 5

PrintSuhaib(5,6)

#==========================================================

#                        WHILE

#==========================================================

while (x > y):
    print("*")
    x -= 1

#==========================================================

#                        IF

#==========================================================

if ( x == y ):
    print("*")

#==========================================================
#               INPUT - WHILE - ELSE - 
#                   
#                 BREAK - CONTINUE
#==========================================================

'''
BREAK ---> STOPS ALL ITERATIONS and move to outside loop.
'''

'''
CONTINUE ---> STOP Current LOOP and move to next iteration (in the same for-loop).
'''


def whileBreakAndIF(count):
    while count < 5 :
        num = int(input("Enter number between 0-100?"))
        if (num < 0) or (num > 100):
            print("Aborted while: You've entered an invalid number.")
            break
        count += 1
    else:
        print("While loop ended gracefully.")

whileBreakAndIF(4)

#==========================================================

#                    CLASS

#==========================================================

#"The Class Attributes"
#"Unlike the instance attributes which are visible at object-level, 
# the class attributes remain the same for all objecs"

class BookStoreMoreDetailed:

    noOfBooks = 0
 
    def __init__(self, title, author):
        self.title = title      # public variable
        self.__author = author  # private variable
        BookStoreMoreDetailed.noOfBooks += 1
 
    def get_an_Author(self):        
        return self.__author

    def set_an_Author(self, author): 
        self.__author = author

    def bookInfo(self):
        print("Book title:", self.title)
        print("Book author:", self.author,"\n")

 
#---------------------------------
# Create a virtual book store
b1 = BookStoreMoreDetailed("Great Expectations", "Charles Dickens")
b2 = BookStoreMoreDetailed("War and Peace", "Leo Tolstoy")
b3 = BookStoreMoreDetailed("Middlemarch", "George Eliot")


b1.set_an_Author("Roger Maynard")
b2.get_an_Author()
 

b1.bookInfo()
b2.bookInfo()
b3.bookInfo()


print("BookStore.noOfBooks:", BookStoreMoreDetailed.noOfBooks)


# output
#Book title: Great Expectations
#Book author: Charles Dickens 

#Book title: War and Peace
#Book author: Leo Tolstoy 

#Book title: Middlemarch
#Book author: George Eliot 

#BookStore.noOfBooks: 3


#==========================================================

#                Inheritance - BASE

#==========================================================

class Taxi:

    def __init__(self, model, capacity, variant):
        self.__model = model      # __model is private to Taxi class
        self.__capacity = capacity
        self.__variant = variant

    def getModel(self):          # getmodel() is accessible outside the class
        return self.__model

    def getCapacity(self):         # getCapacity() function is accessible to class Vehicle
        return self.__capacity

    def setCapacity(self, capacity):  # setCapacity() is accessible outside the class
        self.__capacity = capacity

    def getVariant(self):         # getVariant() function is accessible to class Vehicle
        return self.__variant

    def setVariant(self, variant):  # setVariant() is accessible outside the class
        self.__variant = variant

#==========================================================

#                Inheritance - CHILD

#==========================================================

class Vehicle(Taxi):

    def __init__(self, model, capacity, variant, color):
        # call parent constructor to set model and color  
        super().__init__(model, capacity, variant) # SUPER
        self.__color = color

    def vehicleInfo(self):
        return self.getModel() + " " + self.getVariant() + " in " + self.__color + " with " + self.getCapacity() + " seats"


#OUTPUT:
#-------
#v1 = Vehicle("i20 Active", "4", "SX", "Bronze")
#print(v1.vehicleInfo())
#print(v1.getModel()) # Vehicle has no method getModel() but it is accessible via Vehicle class

#v2 = Vehicle("Fortuner", "7", "MT2755", "White")
#print(v2.vehicleInfo())
#print(v2.getModel()) # Vehicle has no method getModel() but it is accessible via Vehicle class



#==========================================================

#                   READ from a FILE

#==========================================================

f = open("file_name", "wb")
f.close()

print ("File name: ", f.name)
print ("Opening mode: ", f.mode)
print ("Opening mode: ", f.mode)


"""  
Python File Encoding
In Python 3.x, there is a clear difference between strings (text) and a byte (8-bits). It states that the char ‘a’ doesn’t represent the ASCII value 97 until you specify it like that.
 So, while you want to use a file in text mode, then better you mention the correct encoding type.

Also, Python stores a file in the form of bytes on the disk, so you need to decode them in strings before reading. And, similarly, encode them while writing texts to the file.

For a note, Python enables platform-dependent encoding by default. Hence, if you don’t change it, then it’s set to <cp1252> for Windows and <utf-8> for Linux.

Thus, the documentation says to quote the desired encoding while opening a file in Python. See the below Python code snippet.

# f = open('app.log', mode = 'r', encoding = 'utf-8')

For a note, you should import the <io> module in Python 2.x to enable the encoding feature. Python 3.x does it implicitly.
"""


#Auto Close Using ‘With’

with open('app.log', encoding = 'utf-8') as f:
   #do any file operation.
    print(f)



#==========================================================

#                    Try - Catch I/O

#==========================================================

try:
   f1 = open('app.log', encoding = 'utf-8')
   # do file operations.
finally:
   f1.close()



#==========================================================

#     Error at (compile time)  Vs. Exception at (runtime) 

#==========================================================

# Python script encounters an error situation that it can’t cope with, it raises an exception.
# When a Python script raises an exception, it creates an exception object.

"""
the script handles the exception immediately. 
If it doesn’t do so, then the program will terminate and print a traceback to the error along with its whereabouts.

>>> 1 / 0
Traceback (most recent call last):
 File "<string>", line 301, in run code
 File "<interactive input>", line 1, in <module>
ZeroDivisionError: division by zero

"""

#                 Exception Handling

try:
   fob = open("test", "w")
   fob.write("This is my test file for exception handling!!")
except IOError:
   print ("Error: can\'t find the file or read data")
else: #  If there is no exception then execute this block
   print ("Write operation is performed successfully on the file")
   fob.close()


#               Multiple Try()

try:
    fob = open('test', 'r')
    try:
        fob.write("It's my test file to verify try-finally in exception handling!!"
                  )
        print ('try block executed')
    finally:
        fob.close()
        print ('finally block executed to close the file')
except IOError:
    print("Error: can\'t find file or read data")


#==========================================================

#                    READ + WRITE - 

#==========================================================

with open('app.log', 'w', encoding = 'utf-8') as f:
   #first line
   f.write('my first file\n')
   #second line
   f.write('This file\n')
   #third line
   f.write('contains three lines\n')

with open('app.log', 'r', encoding = 'utf-8') as f:
   content = f.readlines()

for line in content:
   print(line)

print(f.read(4))    # read the next 4 data
#'ile\n'

print(f.read())     # read in the rest till end of file
#'This file\ncontains three lines\n'

print(f.read())  # further reading returns empty sting
#''


# This method gives you the current offset of the file pointer in a file.
file.tell()

#This method can help you change the position of a file pointer in a file.

#Reposition pointer at the beginning once again
position = f.seek(0, 0);
data = f.read(19);
print('Again read String is : ', data)



#==========================================================

#                    Import OS 

#==========================================================

import os
os.popen('cp 1.txt.py 2.txt.py')

#This method creates a pipe to or from the command. It returns an open file object which connects to a pipe. 
#You can use it for reading or writing according to the file mode, i.e., ‘r’ (default) or ‘w.’

import os
os.system('cp 1.txt.py 2.txt.py')

# The system() method allows you to instantly execute any OS command or a script in the subshell.



#=========================================================

#                   Threading

#=========================================================

"""
you want to copy a file asynchronously, then use the below method. I
n this, we’ve used Python’s threading module to run the copy operation in the background.
While using this method, please make sure to employ locking to avoid deadlocks. 
You may face it if your application is using multiple threads reading/writing a file.
"""
import shutil
from threading import Thread

src="1.txt.py"
dst="3.txt.py"

Thread(target=shutil.copy, args=[src, dst]).start()


#=========================================================

#                   Subprocess call()

#=========================================================

#Use Subprocess’s Call() Method To Copy A File In Python
#The subprocess module gives a simple interface to work with child processes. 
# It enables us to launch subprocesses, attach to their input/output/error pipes, and retrieve the return values.
#The subprocess module aims to replace the legacy modules and functions like – os.system, os.spawn*, os.popen*, popen2.*.
#It exposes a call() method to invoke system commands to execute user tasks.

import subprocess

src="1.txt.py"
dst="2.txt.py"
cmd='copy "%s" "%s"' % (src, dst)

status = subprocess.call(cmd, shell=True)

if status != 0:
     if status < 0:
         print("Killed by signal", status)
     else:
         print("Command failed with return code - ", status)
else:
     print('Execution of %s passed!\n' % cmd)



#Use Subprocess’s Check_output() Method To Copy A File In Python
#With subprocess’s check_output() method, you can run an external command or a program and capture its output. It also supports pipes.

import os, subprocess

src=os.path.realpath(os.getcwd() + "./1.txt.py")
dst=os.path.realpath(os.getcwd() + "./2.txt.py")
cmd='copy "%s" "%s"' % (src, dst)

status = subprocess.check_output(['copy', src, dst], shell=True)

print("status: ", status.decode('utf-8'))


#=========================================================

#                 Raise an Exception

#=========================================================

# We can also optionally pass values to the exception and specify why it has occurred.

raise MemoryError
#Traceback (most recent call last):
#...
#MemoryError
 
raise MemoryError("This is an argument")
#Traceback (most recent call last):
#...
#MemoryError: This is an argument
 
 
#=========================================================

#               Create your own exception

#=========================================================

 #define Python user-defined exceptions
class Error(Exception):
   """Base class for other exceptions"""
   pass
 
class InputTooSmallError(Error):
   """Raised when the entered alpahbet is smaller than the actual one"""
   pass
 
class InputTooLargeError(Error):
   """Raised when the entered alpahbet is larger than the actual one"""
   pass

#our main program
#user guesses an alphabet until he/she gets it right
 
#you need to guess this alphabet.

alphabet = 'm'
 
while True:
   try:
       apb =  raw_input("Enter an alphabet: ")
       if apb < alphabet:
           raise InputTooSmallError
       elif apb > alphabet:
           raise InputTooLargeError
       break
   except InputTooSmallError:
       print("The entered alphabet is too small, try again!")
       print('')
   except InputTooLargeError:
       print("The entered alphabet is too large, try again!")
       print('')
 
print("Congratulations! You guessed it correctly.")

"""
Enter an alphabet: s
This value is too large, try again!
 
Enter an alphabet: a
This value is too small, try again!
 
Enter an alphabet: l
This value is too small, try again!
 
Enter an alphabet: p
This value is too large, try again!
 
Enter a number: m
Congratulations! You guessed it correctly.

"""

# Python Built-In Exceptions

# IndexError	When the index of a sequence is out of range.
# TypeError	When a function is using an object of the incorrect type.
# EnvironmentError	For errors that occur outside the Python environment.
# SyntaxError	For errors in Python syntax.
# SystemError	When interpreter detects an internal error.


#=========================================================

#                    Lambda

#=========================================================

#lambda inside a list :

alist = [lambda m:m**2, lambda m,n:m*n, lambda m:m**4]

print(alist[0](10), alist[1](2, 20), alist[2](3)) # Output: 100 40 81

#lambda inside a dictionary :

key = 'm'

aDict = {'m': lambda x:2*x, 'n': lambda x:3*x}

print(aDict[key](9)) # Output: 18



#=========================================================

#                 Lambda + Map

#=========================================================

# The output of map() is a list which contains the result returned by the lambda function for each item it gets called.

#Example 1:

alist = ['learn', 'python', 'step', 'by', 'step']

output = list(map(lambda x: x.upper() , alist))

# Output: ['LEARN', 'PYTHON', 'STEP', 'BY', 'STEP']

#--------------------------------------------------

# Example 2: # Python lambda demo to use map() for adding elements of two lists


list1 = [1, 2, 3, 4]
list2 = [100, 200, 300, 400]

output = list(map(lambda x, y: x+y , list1, list2))

# Output: [101, 202, 303, 404]



#=========================================================

#                 Lambda + Filter

#=========================================================
"""
# It returns a final list containing items for which the lambda function evaluates to True.

# Python lambda demo to filter out vowles from a list
"""

alphabets = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i']
vowels = ['a', 'e', 'i', 'o', 'u']

output = list(filter(lambda x: (x in vowels) , alphabets))

# Output: ['a', 'e', 'i']

listy = [1,2,3,4,5]

output2 = map(lambda x: x * 2, listy)


#=========================================================

#                 Lambda + Reduce

#=========================================================

# It produces a non-iterable result, i.e., returns a single value.

from functools import reduce

def fn(m, n) : return m + n

print(reduce((lambda m, n: m + n), [1, 2, 3, 4]))
print(reduce(fn, [1, 2, 3, 4]))

#=========================================================

#                 Python Generator

#=========================================================
"""
# what makes a generator different from an iterator and a regular function?

# Demonstrate Python Generator Function
"""
def fibonacci(xterms):
    # first two terms
    x1 = 0
    x2 = 1
    count = 0
    #CHECK IF num < 0 and if num == 1

    while count < xterms:
        xth = x1 + x2
        print("x1", x1 ,"x2", x2)
        x1 = x2
        print("x1 after x1=x2", x1)
        x2 = xth
        print("x2 after x2=xth", x2)
        count += 1
        yield xth   ######## THIS HERE

fib = fibonacci(5)

# print(fib) ---> Doesn't have any value coz YEILD didnt give

print(next(fib))
print(next(fib))
print(next(fib))
print(next(fib)) # Request a value from the generator function. 
                 # next() method triggers its execution which gives a result back to the caller.

# Python Generator Function with Multiple Yield

def testGen():
    x = 2
    print('First yield')
    # Generator function has many yield statements
    yield x

    x *= 1
    print('Second yield')
    yield x

    x *= 1
    print('Last yield')
    yield x

# Call the generator
iter = testGen()

# Invoke the first yield
next(iter)

# Invoke the second yield
next(iter)

# Invoke the last yield
next(iter)

"""
After executing the above coding snippet, we get the following output:

First yield
Second yield
Last yield
"""

#=========================================================

#                 Generator Expression

#=========================================================

# Generator Expression Syntax

"""
# 1- The syntax of a generator expression is same as of a list comprehension in Python. 
# However, the former uses the round parentheses instead of square brackets
# 2- LC gives back the full list whereas the generator expression returns one value at a time.
"""

gen_expr = (var**(1/2) for var in seq)

# Demonstrate Python Generator Expression

# Define the list
alist = [4, 16, 64, 256]

# Find square root using the list comprehension
out = [a**(1/2) for a in alist]
print(out)

# Use generator expression to calculate the square root
out = (a**(1/2) for a in alist)
print(out)
print(next(out))
print(next(out))
print(next(out))
print(next(out))
print(next(out))

"""
Since we called the next() method one more time, it caused the StopIteration exception. Please check from the below output.

[2.00, 4.0, 8.00, 16.0]
 at 0x000000000359E308>
2.0
4.0
8.0
16.0
Traceback (most recent call last):
  File "C:/Python/Python35/python_generator.py", line 17, in 
    print(next(out))
StopIteration
"""

#=========================================================

#                 How To Use Generator? 

#=========================================================

# 1- Using Next() Method
#-------------------------

# Generator next() Method Demo

alist = ['Python', 'Java', 'C', 'C++', 'CSharp']

def list_items():
    for item in alist:
        yield item

gen = list_items() # merely an identifier holding state of the generator

iter = 0

while iter < len(alist):  
    print(next(gen))
    iter += 1

"""Each next() call on the generator object causes its function to execute until it finds a yield statement. 
Then, Python sends the yielded value back to the caller and preserves the state of the generator for future use.
"""

# 2- Using For Loop
#-------------------

# Generator For Loop Demo
#
alist = ['Python', 'Java', 'C', 'C++', 'CSharp']
def list_items():
    for item in alist:
        yield item

gen = list_items()

for item in gen: # next() call happens implicitly, and we get to use all elements one by one.
    print(item)


#==========================================================

#                 Generator Vs. Function 

#==========================================================

"""
1- The yield call pauses the execution and returns an iterator whereas the return statement is the last one to be executed.
2- Local variables and their states retain between successive calls to the next() method.
3- Any additional call to the next() will raise the StopIteration exception if the there is no further item to process.


"""


#==========================================================

#                 When To Use A Generator?

#==========================================================

"""
There are many use cases where generators can be useful. We have mentioned some of them here:

Generators can help to process large amounts of data. They can let us do the calculation when we want, also known as the lazy evaluation. The stream processing uses this approach.
We can also stack the generators one by one and use them as pipes as we do with the Unix pipes.
The generators can also let us establish concurrency.
We can utilize Generators for reading a vast amount of large files. It will help in keeping the code cleaner and leaner by splitting the entire process into smaller entities.
Generators are super useful for web scraping and help increasing crawl efficiency. They can allow us to fetch the single page, do some operation and move on to the next. This approach is far more efficient and straightforward than retrieving all pages at once and then use another loop to process them.

"""

#==========================================================

#                 Why Use Generators?

#==========================================================

"""
Generators provide many programming-level benefits and extend many run-time advantages which influence programmers to use them.

1. Programmer-Friendly Feature
It seems like a complicated concept, but the truth is that you can easily incorporate them into programs. They are a perfect alternative for the iterators.

Let’s consider the following example to implement the Arithmetic Progression using the Iterator Class.

# Generate Arithmetic Progression Using Iterator Class
# 
class AP:
    def __init__(self, a1, d, size):
        self.ele = a1
        self.diff = d
        self.len = size
        self.count = 0

    def __iter__(self):
        return self

    def __next__(self): 
        if self.count >= self.len:
            raise StopIteration
        elif self.count == 0:
            self.count += 1
            return self.ele
        else:
            self.count += 1
            self.ele += self.diff
            return self.ele

for ele in AP(1, 2, 10):
    print(ele)
The same logic is much easier to write with the help of a generator. See the below code.

# Generate Arithmetic Progression Using Generator Function
# 
def AP(a1, d, size):
    count = 1
    while count <= size:
        yield a1
        a1 += d
        count += 1

for ele in AP(1, 2, 10):
    print(ele)

2. Memory Agnostic
If we use a regular function to return a list, then it will form the full sequence in the memory before sending to the caller. Such an operation would cause high memory usage and become extremely inefficient.

On the contrary, using a generator will consume less memory, and your program will become much more efficient as it will have to process only one item at a time.

3. Capable Of Handling Big Data
Generators can be useful if you have to deal with data of enormous size such as the Big Data. They work as an infinite stream of data.

We can not contain data of such magnitude in memory. But the generator which gives us one value at a time does represent an infinite stream of data.

The following code can produce all the prime numbers theoretically.

# Find All Prime Numbers Using Generator
# 
def find_prime():
    num = 1
    while True:
        if num > 1:
            for i in range(2, num):
                if (num % i) == 0:
                    break
            else:
                yield num
        num += 1

for ele in find_prime():
    print(ele)
Please note, when you run the above code, it will execute infinitely printing all the prime numbers, so you will have to press CTRL+C to stop.

4. Generator Pipeline
With the help of generators, we can create a pipeline of different operations. It is a cleaner way to sub-divide responsibilities among various components and then integrates them to achieve the desired result.

In the below example, we’ve chained two functions, the first finds the prime number between 1 to 100, and the latter selects the odd one from them.

# Chain Multiple Operations Using Generator Pipeline
# 
def find_prime():
    num = 1
    while num < 100:
        if num > 1:
            for i in range(2, num):
                if (num % i) == 0:
                    break
            else:
                yield num
        num += 1

def find_odd_prime(seq):
    for num in seq:
        if (num % 2) != 0:
            yield num

a_pipeline = find_odd_prime(find_prime())

for a_ele in a_pipeline:
    print(a_ele)
Now, it’s up to your imagination how well and what you like to accomplish with this cool Python Generator feature.

"""

# Quick Wrap up
#Generators can produce a sequence on the fly and allow us to access one of its items whenever we need it.
# While doing so, it doesn’t consume a lot of memory and still gives us the ability to work with infinite streams of data. 
# All in all, it is a trickier programming concept and worth trying in projects.


# Syntax – Using A Short Name
#import module_name as shortened_module_name
#Example:
import math as m

#PIP
python -m pip3 install module_package_name

#Conda
conda install module_package_name

#Apt-get
sudo apt install module_package_name



#Import Another File
#------------------   
def Anas():
#------------------   
import AnasFile
AnasFile.Anas()

# https://www.techbeamers.com/python-multithreading-concepts/


#==========================================================

#                 MultiThreading

#==========================================================

# CONS

"""
1- Synchronization is required to avoid mutual exclusion while accessing shared resources of the process. 
It directly leads to more memory and CPU utilization.

2- It raises the possibility of potential deadlocks.

3- It may cause starvation when a thread doesn’t get regular access to shared resources. It would then fail to resume its work.
"""

Type serverType = Type.GetTypeFromProgID("ControlDeskNG.Application");
this.ControlDeskApplication = Activator.CreateInstance(serverType) as IXaApplication;

ControlDeskNGApplication = actxserver('ControlDeskNG.Application')

