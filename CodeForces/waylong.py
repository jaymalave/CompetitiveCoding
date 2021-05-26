


lst = []

n = int(input())

for i in range(0, n):
    str = input()
    lst.append(str)

for str in lst:
    if len(str) < 10:
        print(str)
    else:
        j = len(str)
        print(str[0], j-2, str[j-1])

