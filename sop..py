n = input()
l = []
for i in n:
  l.append(i)
sum = 0
j = 0
for i in range(0,len(n)):
  sum += (int(l[i])**j)
  j += 1
print(sum)
