Python 3.14.4 (tags/v3.14.4:23116f9, Apr  7 2026, 14:10:54) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
a=20
b=10
a+b
30
a-b
10
a*b
200
a/b
2.0
a//b
2
a%b
0
a**b
10240000000000
a
20
b
10
a<b
False
a.b
Traceback (most recent call last):
  File "<pyshell#12>", line 1, in <module>
    a.b
AttributeError: 'int' object has no attribute 'b'
a>b
True
a<=b
False
a>=b
True
a==b
False
a!=b
True



a
20
b
10
a=b
a+=b
a
20
b
10
c+=b
Traceback (most recent call last):
  File "<pyshell#27>", line 1, in <module>
    c+=b
NameError: name 'c' is not defined
NameError: name 'c' is not defined
SyntaxError: invalid syntax
a=10
b
10
a=20
a
20
a+=20
a
40
a-=20
a
20
>>> a*=20
>>> a
400
>>> a/=20
>>> a
20.0
>>> a//=20
>>> a
1.0
>>> a%=20
>>> a
1.0
>>> a**=20
>>> a
1.0
>>> 
...  
>>> 
>>> a>b and a>=b
False
>>> a
1.0
>>> a=10
>>> b=10
>>> b=20
>>> a
10
>>> b
20
>>> a>=b and b>a
False
>>> a<b and b>a
True
>>> a<=b or a>b
True
>>> not a<=b or a>b
False
>>> False
False
