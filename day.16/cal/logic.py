'''def add(a,b):
    print(a + b)

def sub(a,b):
    print(a - b)

    
def mul(a,b):
    print(a*b)


def div(a,b):
    print(a/b)'''



data ={
    12345:{'pin':1234,'balance':5000,'history':[]},
    23456:{'pin':1234,'balance':8000,'history':[]},
    34567:{'pin':1234,'balance':7000,'history':[]},
    45678:{'pin':1234,'balance':9000,'history':[]},
    }
acc_num = None
def login(e_num,e_pin):
    if e_num in data and data[e_num]['pin']==e_pin:
        print("Login Successful")
        global acc_num
        acc_num = e_num
        return True
    else:
        print("Invalid login")
        return False
def check_balance():
    print("Current Balance",data[acc_num]['balance'])
def deposit():
    amount = int(input("Enter the deposit ammount: "))
    data[acc_num]['balance']+=amount
    data[acc_num]['history'].append(f'{amount} is deposited ++++++++')
    print('Deposit successful')
def withdraw():
    amount = int(input("Enter the withdraw ammount: "))
    if data[acc_num]['balance']>=amount:
        data[acc_num]['balance']-=amount
        data[acc_num]['history'].append(f'{amount} is withdraw --------')
        print('Withdraw Successful')
    else:
        print('Insufficient balance')
def viewtransaction():
    if data[acc_num]['history']:
        print("-----------------Transaction History--------------------")
        for i in data[acc_num]['history']:
            print(i)
        print("------------End of the history--------------")
    else:
        print("No Transactions")





























