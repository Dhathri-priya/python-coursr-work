Python 3.14.4 (tags/v3.14.4:23116f9, Apr  7 2026, 14:10:54) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
>>> s = 'python programming lang'
>>> s.startswith('p')
True
>>> s.startswith('P')
False
>>> s.endswith('.ing')
False
>>> s.endwith('lang')
Traceback (most recent call last):
  File "<pyshell#4>", line 1, in <module>
    s.endwith('lang')
AttributeError: 'str' object has no attribute 'endwith'. Did you mean: 'endswith'?
>>> s.endswith('lang')
True
>>> 'asdfg'.isalpha()
True
>>> 'python3.14'.isaplha()
Traceback (most recent call last):
  File "<pyshell#7>", line 1, in <module>
    'python3.14'.isaplha()
AttributeError: 'str' object has no attribute 'isaplha'. Did you mean: 'isalpha'?
>>> 'python3.14'.isalpha()
False
>>> 'python'.isalnum()
True
>>> '12345'.isalnum()
True
>>> 'python1234'.isalnum()
True
>>> 'p'.islower()
True
>>> 'Python'.islower()
False
>>> 'P'.isupper()
True
>>> 'python  1234'.islower()
True
>>> ' '.isspace()
True
>>> 'python  123'.isspace()
False
>>> s
'python programming lang'
>>> s.istitle()
False
>>> if.isidentifier()
SyntaxError: invalid syntax
>>> '12.3'.isdecimal()
False
>>> '123'.isdecimal()
True
'12345'.isdigit()
True
'123456'.isnumeric()
True











l=[]
type(1)
<class 'int'>
l=list()
l
[]
type(list)
<class 'type'>
l=[6,9.0,'fhbf',[],{},{1:},True}
SyntaxError: closing parenthesis '}' does not match opening parenthesis '['
l=[6,9.0,'fhbf',[],{},{1:},True]
SyntaxError: expression expected after dictionary key and ':'
l=[6,9.0,'fhbf',[],{},{1:1},True}
SyntaxError: closing parenthesis '}' does not match opening parenthesis '['
l=[6,9.0,'fhbf',[],{},{1:1},True]
l
[6, 9.0, 'fhbf', [], {}, {1: 1}, True]
a=[1,2,3,4,5]
b=[7,8,9,6]
a+b
[1, 2, 3, 4, 5, 7, 8, 9, 6]
a*12
[1, 2, 3, 4, 5, 1, 2, 3, 4, 5, 1, 2, 3, 4, 5, 1, 2, 3, 4, 5, 1, 2, 3, 4, 5, 1, 2, 3, 4, 5, 1, 2, 3, 4, 5, 1, 2, 3, 4, 5, 1, 2, 3, 4, 5, 1, 2, 3, 4, 5, 1, 2, 3, 4, 5, 1, 2, 3, 4, 5]
names = ['asif','sameer','mehaboob','priya']
names[1]
'sameer'
names[-1]
'priya'
names[3]
'priya'
names[1:3]
['sameer', 'mehaboob']
names[::-1]
['priya', 'mehaboob', 'sameer', 'asif']
names[-3:]
['sameer', 'mehaboob', 'priya']
names[:3]
['asif', 'sameer', 'mehaboob']
'priya' in names
True
'nagaraj' in names
False
len(names)
4
sorted(names)
['asif', 'mehaboob', 'priya', 'sameer']
max(names)
'sameer'
min(names)
'asif'
names
['asif', 'sameer', 'mehaboob', 'priya']
id(names)
2153649581568
names[2]='akki'
names
['asif', 'sameer', 'akki', 'priya']
id(names)
2153649581568
names
['asif', 'sameer', 'akki', 'priya']
names.append('vasu')
names
['asif', 'sameer', 'akki', 'priya', 'vasu']
names.insert(3,'sai')
names
['asif', 'sameer', 'akki', 'sai', 'priya', 'vasu']
names.extend(['yash','dheshik','pinky'])
names
['asif', 'sameer', 'akki', 'sai', 'priya', 'vasu', 'yash', 'dheshik', 'pinky']
names.pop(0)
'asif'
names
['sameer', 'akki', 'sai', 'priya', 'vasu', 'yash', 'dheshik', 'pinky']
names.pop(3)
'priya'
names
['sameer', 'akki', 'sai', 'vasu', 'yash', 'dheshik', 'pinky']
names.pop()
'pinky'
names
['sameer', 'akki', 'sai', 'vasu', 'yash', 'dheshik']
names.remove('akki')
names
['sameer', 'sai', 'vasu', 'yash', 'dheshik']
del names[1]
names
['sameer', 'vasu', 'yash', 'dheshik']
names.clear()
names
[]















names=['asif', 'sameer', 'akki', 'sai', 'priya', 'vasu', 'yash', 'dheshik', 'pinky']
names
['asif', 'sameer', 'akki', 'sai', 'priya', 'vasu', 'yash', 'dheshik', 'pinky']
names.index('akki')
2
names.index('sai')
3
l=[1,2,3,42,1,1,2,3,2,3,23,32,3]
l.count(1)
3
sorted(l)
[1, 1, 1, 2, 2, 2, 3, 3, 3, 3, 23, 32, 42]
l.sort()
l
[1, 1, 1, 2, 2, 2, 3, 3, 3, 3, 23, 32, 42]
l.sort(reverse=true)
Traceback (most recent call last):
  File "<pyshell#102>", line 1, in <module>
    l.sort(reverse=true)
NameError: name 'true' is not defined. Did you mean: 'True'?
l.sort(reverse=True)
l
[42, 32, 23, 3, 3, 3, 3, 2, 2, 2, 1, 1, 1]
l.reverse()
l
[1, 1, 1, 2, 2, 2, 3, 3, 3, 3, 23, 32, 42]
a=[1,2,3,4]
b=a
b
[1, 2, 3, 4]
b.append(10)
b
[1, 2, 3, 4, 10]
a
[1, 2, 3, 4, 10]
c=a.copy()
a
[1, 2, 3, 4, 10]
b
[1, 2, 3, 4, 10]
c=a.copy()
c
[1, 2, 3, 4, 10]
c.append(19)
c
[1, 2, 3, 4, 10, 19]
a
[1, 2, 3, 4, 10]
sum(a)
20
len(a)
5


#[0,0.0,'',[],{},set(),(),False]
any([0,0.0,'',[],{},set(),(),False])
False
any([0,0.0,'',[],{},set(),(),False,1])
True
all([1,-1,0.1,'djf'])
True
