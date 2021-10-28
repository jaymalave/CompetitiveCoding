#write a function to carry out the operation
def ladduCount():
    print("test case check")
    m = []
    l = len(m)
    laddu_count = []
    
    n = int(input())
    
    for i in range(0,n):
        laddu_count.append(1)
    
    for i in range(0, n):
      ele = int(input())
      m.append(ele)
     
    for i in range(1, n-1):
        if (m[i] > m[i-1] and m[i] < m[i+1]) or (m[i] < m[i-1] and m[i] > m[i+1]):
            laddu_count[i] += 1
        elif (m[i] > m[i-1] and m[i] > m[i+1]):
            laddu_count[i] += 2
        elif (m[i] < m[i-1] and m[i] < m[i+1]):
            pass
    
    if m[0] > m[1]:
        laddu_count[0] += 1
    
    if m[l] > m[l-1]:
        laddu_count[l] += 1
    
    return laddu_count
        
#driver code
if __name__ == "__main__":
    #test case count
    t = int(input())
    while(t > 0):
        print(ladduCount())
        t -= 1