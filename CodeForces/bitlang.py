x = int(input())

b = x

for i in range(x):

   a = input()

   if a == "X++":
       x += 1
   elif a == "X--":
       x -= 1



print(x)