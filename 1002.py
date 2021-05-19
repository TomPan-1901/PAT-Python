Atemp = input().split()
Btemp = input().split()
Aexp = [int(i) for i in Atemp[1::2]]
Acoe = [float(i) for i in Atemp[2::2]]
Bexp = [int(i) for i in Btemp[1::2]]
Bcoe = [float(i) for i in Btemp[2::2]]
Aptr = 0
Bptr = 0
Cexp = []
Ccoe = []
while Aptr < len(Aexp) and Bptr < len(Bexp):
    if Aexp[Aptr] > Bexp[Bptr]:
        Cexp.append(Aexp[Aptr])
        Ccoe.append(Acoe[Aptr])
        Aptr += 1
    elif Aexp[Aptr] == Bexp[Bptr]:
        if abs(Acoe[Aptr]+Bcoe[Bptr]) > 10e-9:
            Cexp.append(Aexp[Aptr])
            Ccoe.append(Acoe[Aptr]+Bcoe[Bptr])
        Aptr += 1
        Bptr += 1
    else:
        Cexp.append(Bexp[Bptr])
        Ccoe.append(Bcoe[Bptr])
        Bptr += 1
while Aptr < len(Aexp):
    Cexp.append(Aexp[Aptr])
    Ccoe.append(Acoe[Aptr])
    Aptr += 1
while Bptr < len(Bexp):
    Cexp.append(Bexp[Bptr])
    Ccoe.append(Bcoe[Bptr])
    Bptr += 1
print(len(Cexp), end='')
if len(Cexp):
    print(" ", end='')
for i in range(len(Cexp)-1):
    print(Cexp[i], "%.1f" % Ccoe[i], end=" ")
if len(Cexp):
    print(Cexp[-1], "%.1f" % Ccoe[-1])
