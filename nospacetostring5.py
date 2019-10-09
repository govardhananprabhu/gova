s,b=input().split()
b=int(b)
s1=s[::-b]
s2=s1[::-1]
for i in s2:
    print(i,end=" ")
