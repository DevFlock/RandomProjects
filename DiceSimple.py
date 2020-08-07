import random
min = 1
max = 6


while True:
    print("Rolling Dice...")
    print("Dice 1: ", random.randint(min, max))
    print("Dice 2: ", random.randint(min, max))

    if input("Do you want to roll again? (Any key,n)") == "n":
        print("""
        -=-=-=-=-=-=-=-=-
        Hope you enjoyed!
        -=-=-=-=-=-=-=-=-
        """)
        exit()