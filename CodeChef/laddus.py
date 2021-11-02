#write a function to carry out the operation
def ladduCount():
    print("test case check")
    m = []
    laddu_count = []
    
    n = int(input())
    
    for i in range(0,n):
        laddu_count.append(1)
    
    m = list(map(int, input().split()))
     
    for i in range(1, n-1):
        if (m[i] > m[i-1]):
            laddu_count[i] = laddu_count[i-1] + 1
        else:
            pass
        
    
    if m[0] > m[1]:
        laddu_count[0] = laddu_count[1] + 1
    
    if m[n-1] > m[n-2]:
        laddu_count[n-1] = laddu_count[n-2] + 1
    
    return laddu_count
        
#driver code
if __name__ == "__main__":
    #test case count
    t = int(input())
    while(t > 0):
        ans = ladduCount()
        for i in ans:
            print(str(ans[i]) + " ", end="")
        t -= 1