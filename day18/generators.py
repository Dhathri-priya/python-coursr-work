'''from datetime import date,time,datetime,timedate
print(date(2026,11,31))

print(time(23,6,50))
print(time(23,6,50).hour)
print(time(23,6,50).minute)
print(time(23,6,50).second)

now = datetime.now()
print(now.strftime('%d-%m-%Y'))
print(now.strftime('%d/%m/%Y'))
print(now.strftime('%d/%m/%Y %H:%M:%S'))
print(now.strftime('%d/%m/%Y %I:%M:%S'))
print(now.strftime('%d/%m/%Y %H:%M:%S %p'))
print(now.strftime('%d/%m/%Y %H:%M:%S'))


t_15 = now - timedelta(days=60)


def reels():
    r = ['1..100','101..200','201..300','301..400']
    for i in r:
        yield i
scroll = reels()
print(next(scroll))
print(next(scroll))
print(next(scroll))
'''
def reels():
    yield 1
    yield 2
    yield 3
    yield 4
scroll=reels()
print(next(scroll))
print(next(scroll))
print(next(scroll))
print(next(scroll))
print(next(scroll))
print(next(scroll))
print(next(scroll))
print(next(scroll))
print(next(scroll))
print(next(scroll))
print(next(scroll))
print(next(scroll))
