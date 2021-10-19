count = 0
actual_list = []


def inputList():
    n = int(input())
    for i in range(0, n):
        a = int(input())
        actual_list.append(a)
    return actual_list

def maxIndex(lst):
    if len(lst) == 0:
        return 0
    max_val = max(lst)
    max_index = lst.index(max_val)
    return max_index

def findMaxAndFill(newA, m):
    global count
    global actual_list

    if m == 0:
       return count
    
    for i in range(0, m):
        count += newA[m] - newA[i]
    return findMaxAndFill(newA[m+1:], maxIndex(newA[m+1:]))

actual_list = inputList()
print(findMaxAndFill(actual_list, maxIndex(actual_list)))