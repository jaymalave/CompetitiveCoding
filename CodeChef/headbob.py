n = int(input())

gestures = []

for i in range(0, n):
    gest = input()
    gestures.append(gest)

fingest = list(set(gestures))

if len(fingest) == 3:
    print("INDIAN")
elif len(fingest) == 2:
    if fingest[0] == 'I' or fingest[0] == 'I': 
        print("INDIAN")
    else: 
        print("NOT SURE") 
elif len(fingest) == 1:
     if fingest[0] == 'I':
         print("INDIAN")
     else:
         print("NOT SURE")