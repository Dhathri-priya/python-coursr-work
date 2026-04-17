Python 3.14.4 (tags/v3.14.4:23116f9, Apr  7 2026, 14:10:54) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
a=10
type(a)
<class 'int'>
float(a)
10.0
complex(a)
(10+0j)
str(a)
'10'
list(a)
Traceback (most recent call last):
  File "<pyshell#6>", line 1, in <module>
    list(a)
TypeError: 'int' object is not iterable
tuple(a)
Traceback (most recent call last):
  File "<pyshell#7>", line 1, in <module>
    tuple(a)
TypeError: 'int' object is not iterable
set(a)
Traceback (most recent call last):
  File "<pyshell#8>", line 1, in <module>
    set(a)
TypeError: 'int' object is not iterable
dict(a)
Traceback (most recent call last):
  File "<pyshell#9>", line 1, in <module>
    dict(a)
TypeError: 'int' object is not iterable
bool(a)
True


f= 1.2
int(f)
1
complex
<class 'complex'>
comple(f)
Traceback (most recent call last):
  File "<pyshell#16>", line 1, in <module>
    comple(f)
NameError: name 'comple' is not defined. Did you mean: 'compile'?
complex(f)
(1.2+0j)
str(f)
'1.2'
list(f)
Traceback (most recent call last):
  File "<pyshell#19>", line 1, in <module>
    list(f)
TypeError: 'float' object is not iterable
tuple(f)
Traceback (most recent call last):
  File "<pyshell#20>", line 1, in <module>
    tuple(f)
TypeError: 'float' object is not iterable
set(f)
Traceback (most recent call last):
  File "<pyshell#21>", line 1, in <module>
    set(f)
TypeError: 'float' object is not iterable
dict(f)
Traceback (most recent call last):
  File "<pyshell#22>", line 1, in <module>
    dict(f)
TypeError: 'float' object is not iterable
bool(f)
True


c= 3+6j
int(c)
Traceback (most recent call last):
  File "<pyshell#27>", line 1, in <module>
    int(c)
TypeError: int() argument must be a string, a bytes-like object or a real number, not 'complex'
float(c)
Traceback (most recent call last):
  File "<pyshell#28>", line 1, in <module>
    float(c)
TypeError: float() argument must be a string or a real number, not 'complex'
str(c)
'(3+6j)'
list(c)
Traceback (most recent call last):
  File "<pyshell#30>", line 1, in <module>
    list(c)
TypeError: 'complex' object is not iterable
tuple(c)
Traceback (most recent call last):
  File "<pyshell#31>", line 1, in <module>
    tuple(c)
TypeError: 'complex' object is not iterable
set(c)
Traceback (most recent call last):
  File "<pyshell#32>", line 1, in <module>
    set(c)
TypeError: 'complex' object is not iterable
dict(c)
Traceback (most recent call last):
  File "<pyshell#33>", line 1, in <module>
    dict(c)
TypeError: 'complex' object is not iterable
bool(c)
True


s="python"
l="10"
int(s)
Traceback (most recent call last):
  File "<pyshell#39>", line 1, in <module>
    int(s)
ValueError: invalid literal for int() with base 10: 'python'
int(l)
10
float(s)
Traceback (most recent call last):
  File "<pyshell#41>", line 1, in <module>
    float(s)
ValueError: could not convert string to float: 'python'
float(l)
10.0
complex(s)
Traceback (most recent call last):
  File "<pyshell#43>", line 1, in <module>
    complex(s)
ValueError: complex() arg is a malformed string
complex(l)
(10+0j)
list(s)
['p', 'y', 't', 'h', 'o', 'n']
list(l)
['1', '0']
tuple(s)
('p', 'y', 't', 'h', 'o', 'n')
tuple(l)
('1', '0')
set(s)
{'y', 'n', 'o', 't', 'h', 'p'}
set(l)
{'1', '0'}
dict(s)
Traceback (most recent call last):
  File "<pyshell#51>", line 1, in <module>
    dict(s)
ValueError: dictionary update sequence element #0 has length 1; 2 is required
dict(l)
Traceback (most recent call last):
  File "<pyshell#52>", line 1, in <module>
    dict(l)
ValueError: dictionary update sequence element #0 has length 1; 2 is required
bool(s)
True
bool(l)
True


o=[1,2,3]
int(o)
Traceback (most recent call last):
  File "<pyshell#58>", line 1, in <module>
    int(o)
TypeError: int() argument must be a string, a bytes-like object or a real number, not 'list'
float(o)
Traceback (most recent call last):
  File "<pyshell#59>", line 1, in <module>
    float(o)
TypeError: float() argument must be a string or a real number, not 'list'
complex(o)
Traceback (most recent call last):
  File "<pyshell#60>", line 1, in <module>
    complex(o)
TypeError: complex() argument must be a string or a number, not list
str(o)
'[1, 2, 3]'
tuple(o)
(1, 2, 3)
set(o)
{1, 2, 3}
dict(o)
Traceback (most recent call last):
  File "<pyshell#64>", line 1, in <module>
    dict(o)
TypeError: object is not iterable
Cannot convert dictionary update sequence element #0 to a sequence
bool(o)
True


t=(1,2,3)
int(t)
Traceback (most recent call last):
  File "<pyshell#69>", line 1, in <module>
    int(t)
TypeError: int() argument must be a string, a bytes-like object or a real number, not 'tuple'
float(t)
Traceback (most recent call last):
  File "<pyshell#70>", line 1, in <module>
    float(t)
TypeError: float() argument must be a string or a real number, not 'tuple'
complex(t)
Traceback (most recent call last):
  File "<pyshell#71>", line 1, in <module>
    complex(t)
TypeError: complex() argument must be a string or a number, not tuple
str(t)
'(1, 2, 3)'
list(t)
[1, 2, 3]
set(t)
{1, 2, 3}
dict(t)
Traceback (most recent call last):
  File "<pyshell#75>", line 1, in <module>
    dict(t)
TypeError: object is not iterable
Cannot convert dictionary update sequence element #0 to a sequence
bool(t)
True


s={1,2,3}
int(s)
Traceback (most recent call last):
  File "<pyshell#80>", line 1, in <module>
    int(s)
TypeError: int() argument must be a string, a bytes-like object or a real number, not 'set'
float(s)
Traceback (most recent call last):
  File "<pyshell#81>", line 1, in <module>
    float(s)
TypeError: float() argument must be a string or a real number, not 'set'
complex(s)
Traceback (most recent call last):
  File "<pyshell#82>", line 1, in <module>
    complex(s)
TypeError: complex() argument must be a string or a number, not set
str(s)
'{1, 2, 3}'
list(s)
[1, 2, 3]
tuple(s)
(1, 2, 3)
set(s)
{1, 2, 3}
dict(s)
Traceback (most recent call last):
  File "<pyshell#87>", line 1, in <module>
    dict(s)
TypeError: object is not iterable
Cannot convert dictionary update sequence element #0 to a sequence
bool(s)
True



d={"name":"priya","city":"hyd"}
int(d)
Traceback (most recent call last):
  File "<pyshell#93>", line 1, in <module>
    int(d)
TypeError: int() argument must be a string, a bytes-like object or a real number, not 'dict'
float(d)
Traceback (most recent call last):
  File "<pyshell#94>", line 1, in <module>
    float(d)
TypeError: float() argument must be a string or a real number, not 'dict'
str(d)
"{'name': 'priya', 'city': 'hyd'}"
complex(d)
Traceback (most recent call last):
  File "<pyshell#96>", line 1, in <module>
    complex(d)
TypeError: complex() argument must be a string or a number, not dict
str(d)
"{'name': 'priya', 'city': 'hyd'}"
list(d)
['name', 'city']
tuple(d)
('name', 'city')
set(d)
{'name', 'city'}
bool(d)
True


b=true
Traceback (most recent call last):
  File "<pyshell#105>", line 1, in <module>
    b=true
NameError: name 'true' is not defined. Did you mean: 'True'?
>>> b=True
>>> int(b)
1
>>> float(b)
1.0
>>> complex(b)
(1+0j)
>>> str(b)
'True'
>>> list(b)
Traceback (most recent call last):
  File "<pyshell#111>", line 1, in <module>
    list(b)
TypeError: 'bool' object is not iterable
>>> tuple(b)
Traceback (most recent call last):
  File "<pyshell#112>", line 1, in <module>
    tuple(b)
TypeError: 'bool' object is not iterable
>>> 
>>> set(B)
Traceback (most recent call last):
  File "<pyshell#114>", line 1, in <module>
    set(B)
NameError: name 'B' is not defined. Did you mean: 'b'?
>>> set(b)
Traceback (most recent call last):
  File "<pyshell#115>", line 1, in <module>
    set(b)
TypeError: 'bool' object is not iterable
>>> dict(b)
Traceback (most recent call last):
  File "<pyshell#116>", line 1, in <module>
    dict(b)
TypeError: 'bool' object is not iterable
