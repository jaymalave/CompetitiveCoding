k = int(input())

for i in range(0, k):
    x = int(input())

    if (x%2 == 0 or x%4 == 0 or x%6 == 0 or x%8 == 0):
        print('5')
    if (x%5 == 0 and x%10 != 0):
        print('1')
    if (x%10 == 0 and x%5 != 0):
        print(0)
    else:
        print('-1')
