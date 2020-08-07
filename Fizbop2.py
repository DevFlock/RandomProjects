loop = 1
num1 = 3
num2 = 5
loopn = int(input("How many numbers down?")) + 1

while loop < loopn:

    if loop % num1 == 0 and loop % num2 == 0:
        print("Fizbop")

    elif loop % num1 == 0:
       print("Fiz")
    
    elif loop % num2 == 0:
        print("Bop")

    else:
        print(loop)
    
    loop += 1