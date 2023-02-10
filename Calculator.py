number_1 = int(input("Enter number 1 :"))
operator = input("Enter operator (+, -, *. /, %) :")
number_2 = int(input("Enter number 2 :"))
if operator == "+":
    print(number_1 + number_2)
elif operator == "-":
    print(number_1 - number_2)
elif operator == "*":
    print(number_1 * number_2)
elif operator == "/":
    print(number_1 / number_2)
elif operator == "%":
    print(number_1 % number_2)
else :
    print("OPERATOR INVALID")    