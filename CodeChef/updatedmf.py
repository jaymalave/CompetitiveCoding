def maxFill(arr, n):
	fill = 0
	
	for i in range(1, n-1):
		left = arr[i];
		for j in range(i):
			left = max(left, arr[j])
			
		right = arr[i]
		for j in range(i+1 , n):
			right = max(right, arr[j])
			
		fill = fill + (min(left, right) - arr[i])

	return fill


arr = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]
print(maxFill(arr, len(arr)))
	
