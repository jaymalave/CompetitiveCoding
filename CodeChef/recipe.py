n = int(input())

ings = []

for i in range(0, n):
     ing = int(input())
     ings.append(ing)

ings.sort()

for i in range(0, len(ings)):
    if ings[i]%ings[0] != 0:
        print(ings)
        exit()

fin = []


for i in range(0, len(ings)):
    finel = ings[i]/ings[0]
    fin.append(int(finel))
print(fin)