k = int(input())

for i in range(0, k):
    x = int(input())

    if (x%2 == 0 or x%4 == 0 or x%6 == 0 or x%8 == 0 and x%10 != 0):
        print('5')
    elif (x%5 == 0 and x%10 != 0):
        print('1')
    elif (x%10 == 0):
        print(0)
    else:
        print('-1')
