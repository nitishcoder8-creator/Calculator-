def calculation(num1,num2):
    sign = input("enter operation(+,-,*,/) : ")
    if sign == '+':
        return num1 + num2
    elif sign == '-':
        return num1 - num2
    elif sign == '*':
        return num1 * num2
    elif sign == '/':
        return num1/num2
    else :
        return num1 * num2
while True :
    print("\n This is calculator.")
    A = int(input("enter num1 : "))
    B = int(input("enter num2 : "))
    calculated_number = calculation(A,B)
    print(calculated_number)
