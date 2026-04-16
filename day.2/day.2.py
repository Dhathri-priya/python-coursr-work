Python 3.14.4 (tags/v3.14.4:23116f9, Apr  7 2026, 14:10:54) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
length = 10
width = 5
area = length * width
if area > 30:
    print("large area")
else:
    print("small area")

    
large area


#statement
x = 10
print(x)
10

#identifier
age = 25
def greet():
    print()

    

age = 25
_name = "john"
score1 = 88


comment
Traceback (most recent call last):
  File "<pyshell#46>", line 1, in <module>
    comment
NameError: name 'comment' is not defined
#commentss
#single line comment
"""multiple
line comment
is """
'multiple\nline comment\nis '





#keywords

import keyword
print(keyword.kwlist)
['False', 'None', 'True', 'and', 'as', 'assert', 'async', 'await', 'break', 'class', 'continue', 'def', 'del', 'elif', 'else', 'except', 'finally', 'for', 'from', 'global', 'if', 'import', 'in', 'is', 'lambda', 'nonlocal', 'not', 'or', 'pass', 'raise', 'return', 'try', 'while', 'with', 'yield']
print(len(keyword.kwlist))
35





#variable

product_name = "laptop"
price = 45000
in_stock = true
Traceback (most recent call last):
  File "<pyshell#69>", line 1, in <module>
    in_stock = true
NameError: name 'true' is not defined. Did you mean: 'True'?
>>> in_stock = True
>>> print(product_name, price, in_stock)
laptop 45000 True
>>> 
>>> 
>>> #multiple assignment
>>> a,b,c = 10,20,30
>>> print(a,b,c)
10 20 30
>>> x=y=z=100
>>> print(x,y,z)
100 100 100
>>> x= 5
>>> x= 10
>>> print(x)
10
>>> #swapping
>>> a,b = 5,10
>>> a,b =b,a
>>> print(a,b)
10 5
>>> #delete variable
>>> x = 100
>>> del x
>>> print(x)
Traceback (most recent call last):
  File "<pyshell#89>", line 1, in <module>
    print(x)
NameError: name 'x' is not defined
>>> x= 100
>>> del X
Traceback (most recent call last):
  File "<pyshell#91>", line 1, in <module>
    del X
NameError: name 'X' is not defined. Did you mean: 'x'?
>>> x
100
