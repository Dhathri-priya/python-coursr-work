Python 3.14.4 (tags/v3.14.4:23116f9, Apr  7 2026, 14:10:54) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
#input

name = input()
priya
name
'priya'
type(name)
<class 'str'>
name = input("enter the value")
enter the value priya
name
' priya'


for ages
SyntaxError: invalid syntax
# for integers
age = int(input())
12
age
12


#price
price= float(input())
12.3
price
12.3


#for list
lang = input("enter the lang: ").split()
enter the lang: python java c c++

lang
['python', 'java', 'c', 'c++']

names = input("enter the name: ").split(',')
enter the name: priya,bhavana
names
['priya', 'bhavana']


numbers = list(map(int,input("enter the nums: ").split()))
enter the nums: 1 2 3  5 
numbers
[1, 2, 3, 5]
numbers = tuple(map(float,input("").split()))
1 2 3 3
numbers
(1.0, 2.0, 3.0, 3.0)
set(input().split())
msjdn djnf sjndfhi
{'djnf', 'msjdn', 'sjndfhi'}


email,password = ['@gmail.com','pass@123']
email, password = input().split()
priya@gmail.com 123
email
'priya@gmail.com'
password
'123'









a=eval(input("enter the input: "))
enter the input: [1,2,3,4,5]
a
[1, 2, 3, 4, 5]
#eval is a function which takes input in sytax format and give same syntax as answer{'djnf', 'msjdn', 'sjndfhi'}





map(int,[12,2,3,4,])
<map object at 0x00000175C84E6580>
list(map(int,[12,121,32,34,34,5]))
[12, 121, 32, 34, 34, 5]
numbers = list(map(int,input("enter the nums:").split()))
enter the nums:12,2,3,4,
Traceback (most recent call last):
  File "<pyshell#56>", line 1, in <module>
    numbers = list(map(int,input("enter the nums:").split()))
ValueError: invalid literal for int() with base 10: '12,2,3,4,'
numbers = list(map(int,input("enter the nums:").split()))
enter the nums:1,2,3,4,4
Traceback (most recent call last):
  File "<pyshell#57>", line 1, in <module>
    numbers = list(map(int,input("enter the nums:").split()))
ValueError: invalid literal for int() with base 10: '1,2,3,4,4'
numbers = list(map(int,input("enter the nums:").split()))
enter the nums:1 2 3 4 
numbers
[1, 2, 3, 4]
numbers = tuple(map(int,input("enter the nums:").split()))
enter the nums:1 2 3 4
numbers
(1, 2, 3, 4)
numbers = tuple(map(float,input("enter the nums:").split()))
enter the nums:1 2 3 4
numbers
(1.0, 2.0, 3.0, 4.0)
(1.0, 2.0, 3.0, 4.0)
(1.0, 2.0, 3.0, 4.0)

>>> numbers = set(map(int,input("enter the nums:").split()))
enter the nums:1 23 4 4 34
>>> numbers
{1, 34, 4, 23}
>>> a,b,c = list(map(int,input().split()))
1 2 3
>>> a
1
>>> b
2
>>> c
3
>>> 
>>> 
>>> 

... 
>>> 

>>> 

... 
... 
>>> #outputss
>>> a,b,c = 1,2.3,"python"
>>> a
1
>>> b
2.3
>>> c
'python'
>>> print(a,b,c)
1 2.3 python
>>> print("a=",a,"b=",b,"c=",c)
a= 1 b= 2.3 c= python
>>> print("a=",a,"b=",b,"c=",c,sep="")
a=1b=2.3c=python
>>> 
>>> 
>>> print(f'a={a} b={b} c={c}')
a=1 b=2.3 c=python
>>> print('a=%d b=%.2f c=%s'%(a,b,c))
a=1 b=2.30 c=python\
>>> print('a={} b={} c={}'.format(a,b,c))
a=1 b=2.3 c=python
>>> print('a={2} b={} c={}'.format(c,b,a))
Traceback (most recent call last):
  File "<pyshell#93>", line 1, in <module>
    print('a={2} b={} c={}'.format(c,b,a))
ValueError: cannot switch from manual field specification to automatic field numbering
>>> print('a={2} b={0} c={1}'.format(a,b,c))
a=python b=1 c=2.3
