Python 3.14.4 (tags/v3.14.4:23116f9, Apr  7 2026, 14:10:54) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
t =()
t = tuple()
type(t)
<class 'tuple'>
t=(1,2,3,45,5)
t
(1, 2, 3, 45, 5)
t=(1,12.2,'string',[1,2,3],{1,2,3},(1,2,3),{1:1},False)
t
(1, 12.2, 'string', [1, 2, 3], {1, 2, 3}, (1, 2, 3), {1: 1}, False)
l=(1,1,1)
l
(1, 1, 1)
a=(1,2,3)
b=(4,5,6)
a+b)
SyntaxError: unmatched ')'
a+b
(1, 2, 3, 4, 5, 6)
a*3
(1, 2, 3, 1, 2, 3, 1, 2, 3)
a
(1, 2, 3)
a[2]
3
t
(1, 12.2, 'string', [1, 2, 3], {1, 2, 3}, (1, 2, 3), {1: 1}, False)
t[1:4]
(12.2, 'string', [1, 2, 3])
>>> t[-3:]
((1, 2, 3), {1: 1}, False)
>>> 'string' in t
True
>>> (4321) in t
False
>>> len(t)
8
>>> max(t)
Traceback (most recent call last):
  File "<pyshell#22>", line 1, in <module>
    max(t)
TypeError: '>' not supported between instances of 'str' and 'float'
>>> t=(1,2,3,4,4,5,5)
>>> max(t)
5
>>> min(t)
1
>>> sort(t)
Traceback (most recent call last):
  File "<pyshell#26>", line 1, in <module>
    sort(t)
NameError: name 'sort' is not defined. Did you mean: 'sorted'?
>>> sorted(T)
Traceback (most recent call last):
  File "<pyshell#27>", line 1, in <module>
    sorted(T)
NameError: name 'T' is not defined. Did you mean: 't'?
>>> sorted(t)
[1, 2, 3, 4, 4, 5, 5]
>>> t.count(1)
1
>>> a=(1,2,4,46,7)
>>> a.index(1)
0
>>> sum(a)
60
>>> a
(1, 2, 4, 46, 7)
>>> t
(1, 2, 3, 4, 4, 5, 5)
>>> t=(1,2,3,[4,5])
>>> t
(1, 2, 3, [4, 5])
>>> t.[3]
SyntaxError: invalid syntax
>>> t[3]
[4, 5]
>>> t[3].append(10)
>>> t
(1, 2, 3, [4, 5, 10])
