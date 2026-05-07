Python 3.14.4 (tags/v3.14.4:23116f9, Apr  7 2026, 14:10:54) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
>>> res= [i for i in range(1,11)]
>>> res
[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
>>> res =[i*2 for i in range(1,11)]
>>> res
[2, 4, 6, 8, 10, 12, 14, 16, 18, 20]
>>> res=[i*3 for i in range(1,11)]
>>> res
[3, 6, 9, 12, 15, 18, 21, 24, 27, 30]
>>> res = [i+10 for i in range(1,11)]
>>> res
[11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
>>> res=[i for i in range(10,101,10)]
>>> res
[10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
>>> res=[i for i in range(10,101,10) if i%20]
>>> res
[10, 30, 50, 70, 90]
>>> res=[i for i in range(10,101,10) if i%20==0]
>>> res
[20, 40, 60, 80, 100]
>>> res=[i if i%2==0 else 0 for i in range(1,11)]
>>> res
[0, 2, 0, 4, 0, 6, 0, 8, 0, 10]
>>> s='Python Programming language'
>>> vol='aeiouAEOIU'
>>> res
[0, 2, 0, 4, 0, 6, 0, 8, 0, 10]
>>> s
'Python Programming language'
>>> res= [i for i in s]
>>> res
['P', 'y', 't', 'h', 'o', 'n', ' ', 'P', 'r', 'o', 'g', 'r', 'a', 'm', 'm', 'i', 'n', 'g', ' ', 'l', 'a', 'n', 'g', 'u', 'a', 'g', 'e']
>>> res = ['*' if i in vol else i for i in s]
>>> res
['P', 'y', 't', 'h', '*', 'n', ' ', 'P', 'r', '*', 'g', 'r', '*', 'm', 'm', '*', 'n', 'g', ' ', 'l', '*', 'n', 'g', '*', '*', 'g', '*']
>>> ''.join(res)
'Pyth*n Pr*gr*mm*ng l*ng**g*'
>>> ' '.join(res)
'P y t h * n   P r * g r * m m * n g   l * n g * * g *'
>>> '-'.join(res)
'P-y-t-h-*-n- -P-r-*-g-r-*-m-m-*-n-g- -l-*-n-g-*-*-g-*'
