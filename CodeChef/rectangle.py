#set is used to remove duplicate elements 
init = []
for i in range(0, 4):
    x = int(input())
    init.append(x)

final = list(set(init))
if len(final) == 2:
    print("Yes")
else:
    print("No")