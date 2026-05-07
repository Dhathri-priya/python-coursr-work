Python 3.14.4 (tags/v3.14.4:23116f9, Apr  7 2026, 14:10:54) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
s=set()
s={1,2,3,4,4,5,34,23,23,2}
s
{1, 2, 3, 4, 5, 34, 23}
s.add(100_
      
SyntaxError: invalid decimal literal
s.add(100)
      
s
      
{1, 2, 3, 4, 5, 34, 23, 100}
s.add(12)
      
s
      
{1, 2, 3, 4, 5, 12, 23, 34, 100}
s.add(10.2)
      
s
      
{1, 2, 3, 4, 5, 10.2, 12, 23, 34, 100}
s.add('string')
      
s
      
{1, 2, 3, 4, 5, 10.2, 12, 23, 34, 100, 'string'}
s.add((1,2,3))
      
s
      
{1, 2, 3, 4, 5, 10.2, 12, 23, 34, 100, (1, 2, 3), 'string'}
1 in s
      
True
a={1,2,3,4,5,6}
      
b={7,8,9,1,3,2,}
      
a
      
{1, 2, 3, 4, 5, 6}
b
      
{1, 2, 3, 7, 8, 9}
a.union(b)
      
{1, 2, 3, 4, 5, 6, 7, 8, 9}
a.intersection(b)
      
{1, 2, 3}
a
      
{1, 2, 3, 4, 5, 6}
b
      
{1, 2, 3, 7, 8, 9}
a - b
      
{4, 5, 6}
a^b
      
{4, 5, 6, 7, 8, 9}
{1}<a
      
True
{9,10}<a
      
False
a>{1}
      
True
a
      
{1, 2, 3, 4, 5, 6}
b
      
{1, 2, 3, 7, 8, 9}
a.isdisjoint(b)
      
False
c={10,11}
      
a.isdisjoint(c)
      
True

a.add(5)
      
a
      
{1, 2, 3, 4, 5, 6}
a.update({70,80,90})
      
a
      
{1, 2, 3, 4, 5, 6, 70, 80, 90}
a.remove()
      
Traceback (most recent call last):
  File "<pyshell#38>", line 1, in <module>
    a.remove()
TypeError: set.remove() takes exactly one argument (0 given)
a.remove(90)
      
a
      
{1, 2, 3, 4, 5, 6, 70, 80}
a.remove(2)
      
a.pop()
      
1

a
      
{3, 4, 5, 6, 70, 80}
a.pop()
      
3

a
      
{4, 5, 6, 70, 80}
a.clear()
      
a
      
set()
a={1, 2, 3, 4, 5, 6}
      
a
      
{1, 2, 3, 4, 5, 6}
>>> a.discard(7)
...       
>>> a
...       
{1, 2, 3, 4, 5, 6}
>>> a.remove(7)
...       
Traceback (most recent call last):
  File "<pyshell#54>", line 1, in <module>
    a.remove(7)
KeyError: 7
>>> a
...       
{1, 2, 3, 4, 5, 6}
>>> b={89,54,4,34,44,43,2}
...       
>>> a.intersection_update(b)
...       
>>> a
...       
{2, 4}
>>> b
...       
{2, 34, 4, 54, 89, 43, 44}
>>> c=b
...       
>>> c.add(10)
...       
>>> c
...       
{2, 34, 4, 54, 89, 10, 43, 44}
>>> b
...       
{2, 34, 4, 54, 89, 10, 43, 44}
>>> e = c.copy()
...       
>>> e
...       
{2, 34, 4, 10, 43, 44, 54, 89}
>>> c
...       
{2, 34, 4, 54, 89, 10, 43, 44}
>>> len(c)
...       
8
>>> max(c)
...       
89
>>> min(c)
...       
2
