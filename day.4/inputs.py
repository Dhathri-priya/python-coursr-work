Python 3.14.4 (tags/v3.14.4:23116f9, Apr  7 2026, 14:10:54) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
#input formatting

#string input

name = input("enter u r name: ")
enter u r name: priya
name
'priya'

#integer input

quantity = int(input("enter the age: "))
enter the age: 13
quantity
13

#float Input

price = float(input("Enter the product price: "))
Enter the product price: 12000
price
12000.0

#input as list
names = input("enter employee name: ").split()
enter employee name: priya
names
['priya']

#list of integers

marks = list(map(int, input("enter:").split()))
enter:1 2 3 4 
marks
[1, 2, 3, 4]

#list of float

values = list(map(float, input("enter:").spilt()))
enter:1 2 3 4  5
Traceback (most recent call last):
  File "<pyshell#28>", line 1, in <module>
    values = list(map(float, input("enter:").spilt()))
AttributeError: 'str' object has no attribute 'spilt'. Did you mean: 'split'?
>>> values = list(map(float, input("enter:").split()))
enter:1 2 3 4 45
>>> values
[1.0, 2.0, 3.0, 4.0, 45.0]
>>> 
>>> 
>>> #tuple input
>>> 
>>> value = tuple(map(int,input("enter legth,width,height: ").split()))
enter legth,width,height: 2 3 4
>>> values
[1.0, 2.0, 3.0, 4.0, 45.0]
>>> value
(2, 3, 4)
>>> 
>>> 
>>> #set input
>>> 
>>> ids= set(map(int, input("enter :").split()))
enter :1 2 3 4 
>>> ids
{1, 2, 3, 4}
>>> 
>>> 
>>> #dict input
>>> 
>>> profile = eval(input("enter :"))
enter :name priya age 2
Traceback (most recent call last):
  File "<pyshell#49>", line 1, in <module>
    profile = eval(input("enter :"))
  File "<string>", line 1
    name priya age 2
         ^^^^^
SyntaxError: invalid syntax
>>> profile = eval(input("enter :"))
enter : {'name': 'Ravi', 'age':30, 'role': 'admin'}
>>> profile
{'name': 'Ravi', 'age': 30, 'role': 'admin'}
