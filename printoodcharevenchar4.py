l=list(map(str,input().split()))
for i in range(len(l)):
    if(l[i]=='the' or l[i]=='The' or l[i]=='an' or l[i]=='An' or l[i]=='a' or l[i]=='A'):
        print(l[i+1],end=" ")
