string = input("Please enter the calculation separated by spaces.")
string = string.split()
num1 = int(string[0])
symbol = str(string[1])
num2 = int(string[2])
if symbol == "-":
    minus = num1 - num2
    print("The answer is: ", minus)

elif symbol == "+":
    plus = num1 + num2
    print("The answer is: ", plus)

elif symbol == "*":
    multiply = num1 * num2
    print("The answer is: ", multiply)

elif symbol == "/":
    divide = num1 / num2
    print("The answer is: ", divide)
