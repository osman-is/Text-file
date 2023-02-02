
try:
    num1 = int(input("Please enter a number: "))
except Exception:
    print("Please enter a valid number:")
    num1 = int(input("Please enter a number: "))
try:    
    num2 = int(input("Please enter another number: "))
except Exception:
    print("Please enter a valid number:")
    num2 = int(input("Please enter another number: "))


def math_cal(num1,num2):
    while True:

        operator = input("Please enter a math operator: ")
        if operator.__contains__("+") or operator.__contains__("-"):
            result = num1 + num2 if operator == "+" else num1 - num2
            break
        elif operator.__contains__("*") or operator.__contains__("/"):
            result = num1 * num2 if operator == "*" else num1 / num2
            break
        elif operator.__contains__("**") or operator.__contains__("%"):
            result = num1 ** num2 if operator == "**" else num1 % num2
            break
        else:
            continue
    return result


print(num1)
print(num2)
print(math_cal(num1,num2))


"""
user input num1 & num2
a function that takes 2 parameters with math calculations
return the result
write to a file

Try except finally

value errors

nums = int(input(("Please enter a number: ))

prompt the user to enter a file to read from 
ensure to account for the file not to exist and prompt the user again.

"""