n = int(input())
a = int(input())

def checkA():
    if n > 1:
        for i in range(2, n):
            if n % i == 0:
                a = 0
                break
            else:
                a = 1
    else:
        a = 0
    return a


def checkB():
    if a > 1:
        for i in range(2, n):
            if a % i == 0:
                b = 0
                break
            else:
                b = 1
    else:
        b = 0
    return b




checkA()
checkB()

if checkA == 1 and checkB == 1:
    print("The numbers are co-prime")
else:
    print("The numbers are not co-prime")
