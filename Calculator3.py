while True:
    string = input("Please input the calculation separated by spaces")
    string = string.split()

    num1 = int(string[0])
    num2 = int(string[2])

    symbol = string[1]

    if symbol == "+": 
        calc = num1 + num2

    if symbol == "-":
        calc = num1 - num2
    
    if symbol == "/":
        calc = num1 / num2

    if symbol == "*":
        calc = num1 * num2
    
    print("The calculation is: ", calc)

    if input("Again? (Any key/n)") == "n":
        exit()
