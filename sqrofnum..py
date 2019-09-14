n=int(input())
b=0
d=str(n)
f=len(d)
for i in str(n):
          a=int(i)*int(i)
          for j in range(f-1):
                    b=b+a
print(b)
