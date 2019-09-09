n=int(input())
array=list(map(int,input().split()))
result = 0
for i in range(len(array)-1):
  result=result^array[i]
print(result)
