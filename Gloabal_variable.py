#Global v/s local variable of bank system with bank_balance variable, with deposit and withdraw function.
balance = 5000
print("Current Balance: ", balance)
def deposit(amount):
    global balance                       #write "global" here because we use the global variable in the function othwer wise it becomes local variable
    balance += amount
    print("Deposited:", amount)

def withdraw(amount):
    global balance

    if amount <= balance:
        balance -= amount
        print("Withdrawn:", amount)
    else:
        print("Insufficient Balance!")

deposit(1000)
withdraw(2000)

print("Updated Balance:", balance)