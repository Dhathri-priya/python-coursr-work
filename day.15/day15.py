''' equal(s1,s2):
    if s1==s2:
        return "Equal"
    else:
        return "Not equal"
res = lambda s1,s2: "Equal" if s1==s2 else "Not equal"
s1="Python"
s2 = "lang"
print(res(s1,s2),equal(s1,s2))

res = lambda ch: "Alp" if ch.isalpha() else "Not alp"
print(res('12'))
res = lambda num: num **2
print((res(2)))
res = lambda name: f'thankyou {name} for choosing python'
print(res('Asif'))
l = [1,2,3,4,5,6,7]
for i in range(len(l)):
    l[i]**=2
print(l)
res = list(map(lambda i:i**2,1))
print(res)


l=['asif','priya','yaswanth','nagaraju','saikiran']
res=list(map(lambda i:i.upper(),l))
print(res)

vol='aeiouAEIOU'
res = lambda s: "Starts with vol" if s[0] in vol else "Not start"
print(res('asif'))

res= lambda s: s.split('@')[-1]
print(res("sowmya@codegnan.com"))

l=[1,2,3,4,5,6,7,5,65,23,]
res=list(filter(lambda i: i%3==0,l))
print(res)



l= ['as','of','too','like']
res= list(filter(lambda i: len(i)>3,1))

print(res)


from functools import reduce
l=[1,2,3,4,5,7,8]

res = reduce(lambda sum,i: sum+i,l)
print(res)'''





















































