#process take input from the user
#input :number /operands and operator
operand1=int(input("Enter first number:"))
operand2=int(input("enter second number"))
operator=str(input('Enter the operator:'))
#lets add the operands
if operator == '+':
    result=operand1 + operand2
elif operator == '-':
    result=operand1 - operand2

elif operator == '*':
    result=operand1 * operand2
elif operator == '/':
    result=operand1 / operand2
elif operator == '%':
    result=operand1 % operand2
else:
    print("wrong input")

print("the result is: ",str(result))
