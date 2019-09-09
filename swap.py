n = int(input())
arr = [int(x) for x in input().split()]
for i in range(0,len(arr)-1,2):
	arr[i],arr[i+1] = arr[i+1],arr[i]
for i in arr:
	print(i,end=" ")
