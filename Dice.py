import random

randomnumber = random.randint(1, 6)

if randomnumber == 1:
    print(""" 
    
      •
    
    """)

elif randomnumber == 2:
    print("""
    • 
    
        •
    """)

elif randomnumber == 3:
    print("""
    •
      •
        •
    """)

elif randomnumber == 4:
    print("""
    •   •
    
    •   •
    """)

elif randomnumber == 5:
    print("""
    •   •
      •   
    •   •
    """)

else:
    print("""
    •   •
    •   •
    •   •
    """)


print ("Your number is:", randomnumber)