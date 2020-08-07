while True:
    fall_in_feet = 16*float(input("How many seconds did it take to fall?"))**2

    print("The answer is: ", fall_in_feet*0.3048, "meters.")

    if input("Do you want to run again? (y/n)") == "n":
        exit(print("\n \n Hope to see you again! \n \n"))
