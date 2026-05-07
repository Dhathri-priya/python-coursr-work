'''
import sys
#print(sys.argv)
#print(sys.path)
#print(sys.version)

print("start")
sys.exit()
print("End")

import platform
print(platform.system())
print(platform.release())
print(platform.processor())


import math

print(math.pi)
print(math.e)
print(math.sqrt(64))
print(math.pow(3,3))
print(round(13.2))
print(round(13.6))
print(math.ceil(13.2))
print(math.ceil(13.6))
print(math.ceil(13.0001))
print(math.ceil(13.999999))

print(math.floor(13.2))
print(math.floor(13.6))
print(math.floor(13.00001))
print(math.floor(13.99999))

import math
print(math.gcd(30,20))
print(math.log(2,2))
print(math.sin(60))
print(math.tan(60))
print(math.cos(60))

print(math.degrees(150))
print(math.radians(150))


import random

print(random.random())
print(random.randint(1,6))
print(random.uniform(1,6))

l = ['java','python','ai','ml']

print(random.choice(l))
print(random.choice(l,k=2))


print("Befor:",l)
random.shuffle(l)
print("After:",1)


import random

random.seed(40)
print(random.random())
print(random.randint(1,6))
print(random.uniform(1,6))

l = ['java','python','ai','ml']

print(random.choice(l))
print(random.choices(l,k=2))


print("Befor:",l)
random.shuffle(l)
print("After:",1)


import collections

s = 'python programming'
l=[1,2,3,4,5,6,7,56,4,4,3,2,3,34,5,6,6,4,3,2,22,2]
text = 'The os module provides functions to int'
print(collections.Counter(text.split()))
print(collections.Counter(s))
print(collections.Counter(l))


import collections
s='python programming'
d = collections.defaultdict(str)
for i in s:
    d[i]+=str(1)
print(d)


import collections488888888888888888888888888888888888888

d = collections.deque([])
d.append(10)
d.append(20)
d.append(30)
d.popleft()
d.popleft()
d.append(80)
d.append(90)'''

import itertools

print(list(itertools.combinations('ABC', 2)))
print(list(itertools.permutations('ABC',2)))










































