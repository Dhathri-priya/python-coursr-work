'''
import logic

logic.add(2,6)
logic.sub(10,6)
logic.mul(4,5)
logic.div(6,3)


import logic as lg
lg.add(2,6)
lg.sub(10,6)
lg.mul(4,5)
lg.div(6,3)


from logic import add,mul
add(2,6)
mul(3,5)


from logic import *


add(2,6)
sub(10,6)
mul(4,5)
div(6,3)
'''

from logic import *

acc_num = int(input("enter thr account number:"))
pin = int(input("Enter the pin:"))

if login(acc_num,pin):
    print("Welcome to the ATM")

    while True:
        print("[C]heck balance")
        print('[D]eposit')
        print('[w]ithdraw')
        print('[v]iew History')
        print('[E]xit')

        ch = input("Enter the choice: ").upper()
        if ch=='C':
            check_balance()
        elif ch=='D':
            deposit()
        elif ch=='W':
            withdraw()
        elif ch=='V':
            viewtransaction()
        elif ch=='E':
             print("Thankyou")
             break
        else:
            print("Enter the valid input")
    

























































