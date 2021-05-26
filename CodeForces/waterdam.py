n = int(input())
lst1 = []
lst2 = []
sum1 = 0
sum2 = 0

for i in range(n):
    x = int(input())
    lst1.append(x)
    y = int(input())
    lst2.append(y)

for i in lst2:
    sum2 = sum2 + i
    if sum2 >= 1000:
        sum1 = int(sum2/1000)
        sum2 = sum2%1000
    else:
        pass



for i in lst1:
    sum1 = sum1 + i
print(sum1)

print(sum2)










