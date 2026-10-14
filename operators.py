#Arthimetic operators Program
def calculator():
    a = int(input("Enter first num: "))
    b = int(input("Enter second num: "))
    operator = input("Enter the operator +,-,*,/,%: ")

    if operator == "+":
        print(a+b)
    elif operator == "-":
        print(a-b)
    elif operator == "*":
        print(a*b)
    elif operator == "/":
        print(a/b)
    elif operator == "%":
        print(a%b)
    else:
        print("   INVALID OPERATOR   ")

calculator()
