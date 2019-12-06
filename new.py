n=int(input())
l=list(map(int,input().split()))
l1=[]
l2=[]
l3=[]
for i in range(n+1):
      l2.append(l[i])
for i in range(n+1):
      k=max(l2)
      l1.append(k)
      l2.remove(k)
for i in range(n+1):
      l3.append(l.index(l1[i]))
print(*l3)
   
