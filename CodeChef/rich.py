def main():
 n = int(input())

 for i in range(0, n):
    a = int(input())
    b = int(input())
    x = int(input())

    ans = int((b-a)/x)

    print(ans)

if __name__=="__main__":
    main()