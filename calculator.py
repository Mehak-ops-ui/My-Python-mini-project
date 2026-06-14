print("==============CALCULATOR===============")

num1 = float(input("Enter num1 = "))
operator = input("Enter operator  (+ , - , * , / ) =  ")
num2 = float(input("Enter num2 = "))

if operator == "+" :
    result = num1 + num2
    print("The result is = ",result)
elif operator == "-":
    result = num1 - num2
    print("The result is = ",result)
elif operator == "*":
    result = num1 * num2
    print("The result is = ",result)
elif operator == "/":
    if num2==0:
        print("Error: Division by zero is not possible")
    else:
     result = num1 / num2
    print("The result is = ",result)

else :
    print("Invalid operator!!!*******")


