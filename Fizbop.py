t3 = 0
t5 = 0
tt3 = []
tt5 = []
times3 = 1
times5 = 1
x = 0
fizbop = [15, 30, 45, 60]

while times3 < 50:
    t3 = times3 * 3
    tt3.append(t3)
    times3 += 1

while times5 < 50:
    t5 = times5 * 5
    tt5.append(t5)
    times5 += 1


while x < 50:
    x += 1
    
    if x in fizbop:
        print("Fizbop")
    
    elif x in tt3:
        print("Fiz")
    
    elif x in tt5:
        print("Bop")

    else:
        print(x)
