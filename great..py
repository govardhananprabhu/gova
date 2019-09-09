n=input()
lst=list(map(int,input().split()))
a=lst.sort()
for i in range(len(a),0,-1):
	for j in range(len(a)):
    	if(a[j]/a[i]==0):
print(a[i])
