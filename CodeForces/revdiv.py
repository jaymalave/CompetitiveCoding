def revNo():
    n = 4562
    rev = 0

    while (n > 0):
        a = n % 10
        rev = rev * 10 + a
        n = n / 10

    print(rev)


revNo()

lst = []

while (rev > 0):
    a = rev % 10
    rev = rev / 10
    lst.append(a)

for a in lst:
    if n % a == 0:
        print(a)
    else:
        pass