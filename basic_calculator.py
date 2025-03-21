# num1 = int(input("Enter first number:"))

# num2 = int(input("Enter second number:"))

# num3 = int(input("Enter third number:"))

# operator = input("Enter Operator :")

# match operator :
#     case '+':
#         print( "sum is" ,num1+num2+num3)

#     case '-':
#         print("difference is" ,num1-num2-num3)
    
#     case '*':
#         print("product is" , num1*num2*num3)

#     case'/':
#         print("division is" , num1/num2/num3)

#     case '%':
#         print("remainder is" , num1%num2%num3)

#     case '**':
#         print("power is" , num1**num2**num3)


num1 = int(input("Enter first number:"))

num2 = int(input("Enter second number:"))

num3 = int(input("Enter third number:"))

operator = input("Enter Operator :")

match operator:
	case '+':
		print(f"sum is {num1 + num2 + num3}")
	case '-':
		print(f"difference is {num1 - num2 - num3}")
	case '*':
		print(f"product is {num1 * num2 * num3}")
	case '/':
		print(f"division is {num1 / num2 / num3}")
	case '%':
		print(f"remainder is {num1 % num2 % num3}")
	case '**':
		print(f"power is {num1 ** num2 ** num3}")
	case _:	
		print("Invalid pperator")