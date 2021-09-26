def descOrder(scores):
    scores.sort(reverse=True)
    return scores

def countQual(pos):
    counter = 0
    for score in sortedScores:
     if score >= sortedScores[pos-1]:
        counter += 1
    return counter

lst = []
 
n = int(input("Enter number of scores"))
 
for i in range(0, n):
    ele = int(input())
    lst.append(ele) 

sortedScores = descOrder(lst)

k = int(input("Enter the k-th position"))

print(countQual(k))