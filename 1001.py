l = [int(i) for i in input().split()]
result = l[0]+l[1]
if result < 0:
    print('-', end='')
    result = -result
if len(str(result)) <= 3:
    print(result)
else:
    temp = []
    while result:
        tempstr = str(result % 1000)
        while(len(tempstr) < 3):
            tempstr = '0'+tempstr
        temp.append(tempstr)
        result //= 1000
    temp.reverse()
    print(int(temp[0]), end=',')
    for num in temp[1:-1]:
        print(num, end=',')
    print(temp[-1])
