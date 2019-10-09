s=input()
x=input()
if x in s:
    s2=s.replace(x,"")
    print(s2.replace(" ",""))
else:
    print(s)
