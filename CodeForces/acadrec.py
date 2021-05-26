#Cindy's research project involves tracing the number of people infected by the Cordon Bleu virus, down to the minute. She has recorded the number of new cases for each of the first N minutes.
# Specifically, she knows that 0 people were infected at minute 0, and she recorded that at the ith minute, Ai more people were infected by the virus, for each i from 1 to N. It is guaranteed that the Ai are non-negative integers.

#Based on this, she constructed a second array B of N integers, the cumulative number of cases by the ith minute. That is, Bi counts the total number of people infected on or before the ith minute.

#Cindy keeps all her data in her laptop. Unfortunately, her laptop got infected by a (computer) virus and all the data in her hard drive got scrambled!
# Cindy also doesn't have any backups of her data, neither locally or on the cloud. How irresponsible! Always back up your data.

#The original array A was deleted. Cindy was able to recover the elements of B, but they were shuffled around randomly and ended up in the wrong order!

#Given the elements of B in some random order, help Cindy reconstruct the elements of the original array A, and give them in the correct order.
# It can be shown that A can always be recovered, and furthermore that this answer is unique.

#Input
#The first line of input contains a single integer N, the number of minutes that were tracked.

#The second line of input contains N space-separated integers, the elements of B in some random order.

#Output
#Output N space-separated integers A1, A2, …, AN that are consistent with the values of B given in the input.





lst = []

n = int(input())

for i in range(0, n):
    el = int(input())

    lst.append(el)

for i in range(n-1):
    for j in range(0, n-i-1):
        if lst[j] > lst[j+1]:
            lst[j], lst[j+1] = lst[j+1], lst[j]
print(lst[0])
for i in range(n-1):
    a = lst[i+1] - lst[i]
    print(a)







