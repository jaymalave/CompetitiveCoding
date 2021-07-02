h = int(input())
cc = float(input())
ts = int(input())

if h > 50 and cc < 0.7 and ts > 5600:
    print("10")
elif h > 50 and cc < 0.7 and ts < 5600:
    print("9")
elif h < 50 and cc < 0.7 and ts > 5600:
    print("8")
elif h > 50 and cc > 0.7 and ts > 5600:
    print("7")
elif h > 50 and cc > 0.7 and ts < 5600:
    print("6")
elif h < 50 and cc < 0.7 and ts < 5600:
    print("6")
elif h < 50 and cc > 0.7 and ts > 5600:
    print("6")
else: 
    print("5")
