import os

type = input("Which converter do you want? (k/m)")

if type == "k":
    kilo = int(input("How many kilometers?"))
    final = kilo * 0.62137119223733
    print("Your answer is: ", final)

elif type == "m":
    miles = int(input("How many miles?"))
    final = miles * 1.609344
    print
    print("Your answer is: ", final)



q = input("Do you want to do this again? (y/n)")

if q == "y":
    os.system('python k_to_m.py')
    exit()
    
else:
    exit()

